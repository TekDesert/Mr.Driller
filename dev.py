import pygame, time
from pygame.locals import *
from random import *

pygame.init()

# Variables Pygame

white = (255, 255, 255)
crystal = (162,162,162)
black  = (0, 0, 0)
rose = (236,28,115)
red = pygame.Color('#ff0000')
green  = pygame.Color('#00ff62')
blue  = pygame.Color('#0026ff')
yellow = (222,207,4)
width = 800
height = 600
clock = pygame.time.Clock()
pop_block = pygame.mixer.Sound("Music/pop_block.wav")

# Images

walkRight = [pygame.image.load('Driller/droite1.png'), pygame.image.load('Driller/droite2.png'),
			 pygame.image.load('Driller/droite3.png'),pygame.image.load('Driller/droite4.png'),
			 pygame.image.load('Driller/droite5.png'), pygame.image.load('Driller/droite6.png'),
			 pygame.image.load('Driller/droite7.png'), pygame.image.load('Driller/droite8.png'),
			 pygame.image.load('Driller/droite9.png')]
walkLeft = [pygame.image.load('Driller/gauche1.png'), pygame.image.load('Driller/gauche2.png'),
			pygame.image.load('Driller/gauche3.png'),pygame.image.load('Driller/gauche4.png'),
			pygame.image.load('Driller/gauche5.png'),pygame.image.load('Driller/gauche6.png'),
			pygame.image.load('Driller/gauche7.png'),pygame.image.load('Driller/gauche8.png'),
			pygame.image.load('Driller/gauche9.png')]

fall = [
	pygame.image.load('Driller/fall.png'),
	pygame.image.load('Driller/fall1.png')
]

centre = pygame.image.load('Driller/centre.png')

blocks = [
	pygame.image.load("Blocks/block_jaune.png"),
	pygame.image.load("Blocks/block_vert.png"),
	pygame.image.load("Blocks/block_bleu.png"),
	pygame.image.load("Blocks/block_rouge.png"),
	pygame.image.load("Blocks/block_blanc.png"),
	pygame.image.load("Blocks/block_crystal.png"),
	pygame.image.load("Blocks/block_niveau.png")
]


blocks_fissure = [
	pygame.image.load("Blocks/block.png"),
	pygame.image.load("Blocks/block1.png"),
	pygame.image.load("Blocks/block2.png"),
	pygame.image.load("Blocks/block3.png"),
	pygame.image.load("Blocks/block4.png"),
	pygame.image.load("Blocks/block5.png")
]
image_drill_left = pygame.image.load("Driller/drill_left.png")
image_drill_right = pygame.image.load("Driller/drill_right.png")
image_drill_down = pygame.image.load("Driller/drill_down.png")

oxy_display = pygame.image.load("Blocks/oxy_display.png")
capsule = pygame.image.load("Blocks/capsule_oxygene.png")
dead_crash = pygame.image.load("Driller/ecraser.png")
dead_air = pygame.image.load("Driller/asph.png")
ange = pygame.image.load("Driller/ange.png")
depth_display = pygame.image.load("Blocks/depth.png")
score_display = pygame.image.load("Blocks/score.png")
level_display = pygame.image.load("Blocks/level.png")
air_display = pygame.image.load("Blocks/air.png")
air_support_display=pygame.image.load("Blocks/air_support.png")
air_pourcent_display = pygame.image.load("Blocks/pourcent.png")
lives_display = pygame.image.load("Blocks/lives.png")



# Variables Globales

drill_left = False
drill_right = False
compteur_drill = 0

temps_recuperer = 0

cologne = 12
ligne = 35

game_over = False
surface = pygame.display.set_mode( (width,height) )
pygame.display.set_caption("Projet DEV")
obstacles = [[None]*cologne for l in range(ligne) ]

x = 100
y = 5
gravity = 5
left = False
right = False
walkCount = 0
fallCount = 0
pourcentage = 100
points = 0
profondeur = 0
GameOver = False
Death = 0
death_depth = []
CountDeath = 3
Capsule_Air = 10
name_list = []

# SP

def saisie():
	global name_list
	running = True
	play = False
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == KEYDOWN:
				if event.key == K_RETURN:
					running = False
					play = True
			if event.type == pygame.KEYDOWN and len(name_list) != 30:
				if event.key == pygame.K_a:
					name_list.append("q")
				elif event.key == pygame.K_b:
					name_list.append("b")
				elif event.key == pygame.K_c:
					name_list.append("c")
				elif event.key == pygame.K_d:
					name_list.append("d")
				elif event.key == pygame.K_e:
					name_list.append("e")
				elif event.key == pygame.K_f:
					name_list.append("f")
				elif event.key == pygame.K_g:
					name_list.append("g")
				elif event.key == pygame.K_h:
					name_list.append("h")
				elif event.key == pygame.K_i:
					name_list.append("i")
				elif event.key == pygame.K_j:
					name_list.append("j")
				elif event.key == pygame.K_k:
					name_list.append("k")
				elif event.key == pygame.K_l:
					name_list.append("l")
				elif event.key == pygame.K_SEMICOLON:
					name_list.append("m")
				elif event.key == pygame.K_n:
					name_list.append("n")
				elif event.key == pygame.K_o:
					name_list.append("o")
				elif event.key == pygame.K_p:
					name_list.append("p")
				elif event.key == pygame.K_q:
					name_list.append("a")
				elif event.key == pygame.K_r:
					name_list.append("r")
				elif event.key == pygame.K_s:
					name_list.append("s")
				elif event.key == pygame.K_t:
					name_list.append("t")
				elif event.key == pygame.K_u:
					name_list.append("u")
				elif event.key == pygame.K_v:
					name_list.append("v")
				elif event.key == pygame.K_w:
					name_list.append("z")
				elif event.key == pygame.K_x:
					name_list.append("x")
				elif event.key == pygame.K_y:
					name_list.append("y")
				elif event.key == pygame.K_z:
					name_list.append("w")
				elif event.key == pygame.K_SPACE:
					name_list.append(" ")
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_BACKSPACE and len(name_list) > 0:
					name_list.pop(-1)

		#surface.fill( (0,0,0) )
		ecran_saisie = pygame.image.load("Screens/EnterNameBetter.png")
		ecran_saisie = pygame.transform.scale(ecran_saisie, (width, height))
		surface.blit(ecran_saisie,(0,0))

		string = ''.join(name_list)
		font = pygame.font.Font("Screens/monospace.ttf" , 40)
		texte = font.render(string , True , (0,0,0))
		rectangle = texte.get_rect()

		rectangle.topleft  = (150,130)

		surface.blit(texte,rectangle)

		pygame.display.update()
		clock.tick(60)

	return play , string

def air():
	global pourcentage , GameOver , Death , x , death_depth
	pos_x = 620
	pos_y = 300
	font = pygame.font.Font("freesansbold.ttf", 30)

	if pourcentage <= 0:
		GameOver = True
		Death = 1

	if pourcentage > 100:
		pourcentage = 100

	text_temps = font.render(str(pourcentage), True, white)


	list_rotato = [oxy_display for loop in range(pourcentage)]

	surface.blit(text_temps, (pos_x+80, pos_y+40))
	surface.blit(air_display,(pos_x-20,pos_y-50))
	surface.blit(air_support_display,(pos_x-8,pos_y-3))
	surface.blit(air_pourcent_display,(pos_x+135,pos_y+40  ))
	longueur_barre = 0

	for k in list_rotato:
		surface.blit(k, (pos_x + longueur_barre, pos_y))
		longueur_barre += 1.5

def score(points):
	pos_x = 620
	pos_y = 150
	font = pygame.font.Font("freesansbold.ttf", 30)

	pygame.draw.circle(surface,rose,(pos_x,pos_y+20),10,0)
	pygame.draw.circle(surface,rose,(pos_x+30,pos_y+20),10,0)

	text_score = font.render(str(points), True, white)
	text = font.render("PTS", True, rose)

	surface.blit(text_score, (pos_x+80, pos_y+30))
	surface.blit(text, (pos_x+100, pos_y+60))
	surface.blit(score_display,(pos_x-20,pos_y-30))

def depth(profondeur):
	pos_x = 620
	pos_y = 50
	font = pygame.font.Font("freesansbold.ttf", 30)

	pygame.draw.circle(surface, yellow, (pos_x, pos_y), 10, 0)
	pygame.draw.circle(surface, yellow, (pos_x + 30, pos_y), 10, 0)

	text_score = font.render(str(profondeur), True, white)
	text = font.render("FT", True, yellow)

	surface.blit(text_score, (pos_x + 80, pos_y))
	surface.blit(text, (pos_x + 100, pos_y + 30))
	surface.blit(depth_display,(600,0))

def lives(DeathCount):
	pos_x = 560
	pos_y = 400
	font = pygame.font.Font("freesansbold.ttf", 30)

	text_score = font.render(str(DeathCount), True, white)
	text = font.render("x", True, red)

	surface.blit(text_score, (pos_x + 180, pos_y+32))
	surface.blit(text, (pos_x + 150, pos_y+30))
	surface.blit(ange,(pos_x + 80, pos_y+5))
	surface.blit(lives_display,(600,pos_y-25))

def levels():	
	pos_x=600
	pos_y= 480

	font = pygame.font.Font("freesansbold.ttf", 30)

	text_level = font.render(str(level), True, white)

	surface.blit(text_level, (pos_x+50 , pos_y+50))

	surface.blit(level_display,(pos_x,pos_y))

def chrono(seconds):
	time.sleep(1)
	return (seconds + 1)

def intro():
	pygame.mixer.music.load("Intro/intro_music.mp3")  # je rapporte la musique
	pygame.display.flip()
	font = pygame.font.Font(None, 24)
	clock = pygame.time.Clock()
	seconds = 0
	nextimg = 1

	''' Chargement des images et choix de la premiere image'''

	images = [
		pygame.image.load("Intro/Start_screen1.png"),
		pygame.image.load("Intro/Start_screen2.png"),
		pygame.image.load("Intro/Start_screen3.png"),
		pygame.image.load("Intro/Start_screen4.png"),
		pygame.image.load("Intro/Start_screen5.png"),
		pygame.image.load("Intro/Start_screen6.png"),
		pygame.image.load("Intro/Start_screen7.png"),
		pygame.image.load("Intro/Start_screen8.png")
	]

	pygame.mixer.music.play(0)  # On lance la musique

	running = True
	play = False
	while running:
		seconds = chrono(seconds)  # on lance le chrono
		if seconds > 0 and seconds % 3 == 0:  # tout les trois secondes on change d'images
			nextimg += 1

		if nextimg <= len(images):
			choix_image = images[nextimg-1]
			choix_image = pygame.transform.scale(choix_image, (width, height))

		text_temps = font.render(str(seconds) + " seconds since start", 1,(255, 255, 255))  # petite indicateur de temps
		surface.blit(choix_image, (0, 0))
		surface.blit(text_temps, (0, 0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == KEYDOWN:
				if event.key == K_SPACE:
					running = False
					play = True
		pygame.display.update()
		clock.tick(60)

	return play



def initialise():
	global obstacles

	x_cube = 0
	hauteur = y+200
	caps = Capsule_Air
	for i in range(0,ligne-5):
		for j in range(cologne):
			if caps != 0:
				square_type = randint(1,8)
			else:
				square_type = randint(1,7)

			if square_type == 8:
				caps -= 1

			square = pygame.Rect(x_cube, hauteur, 50, 50)
			if square_type == 5:
				obstacles[i][j] = [square, square_type,0,0]
			elif square_type == 7:
				obstacles[i][j] = [square, square_type,0]
			else:
				obstacles[i][j] = [square, square_type]
			cpt = 3
			while cpt >= 3:
				cpt = 0
				for k in range(j - 1, j - 4, -1):
					if k >= 0:
						if obstacles[i][k] != None:
							if (obstacles[i][k])[1] == (obstacles[i][j])[1]:
								cpt += 1
				for l in range(i - 1, i - 4, -1):
					if l >= 0:
						if obstacles[l][j] != None:
							if (obstacles[l][j])[1] == (obstacles[i][j])[1]:
								cpt += 1
				if cpt >= 3:
					square_type = randint(1, 7)
					if square_type == 5:
						obstacles[i][j] = [square, square_type, 0, 0]
					elif square_type == 7:
						obstacles[i][j] = [square, square_type, 0]
					else:
						obstacles[i][j] = [square, square_type]

			x_cube += 50
		x_cube = 0
		hauteur += 50

	hauteur += 400
	for i in range(ligne-5 , ligne):
		for j in range(cologne):
			square = pygame.Rect(x_cube, hauteur, 50, 50)
			obstacles[i][j] = [square , 9]
			x_cube += 50
		x_cube = 0
		hauteur += 50

def draw():
	global collision_vertical , x , y , obstacles
	surface.fill(black)
	pygame.draw.line(surface, white, (600, 0), (600, height))

	pygame.draw.line(surface, rose, (600, 125), (width, 125))
	pygame.draw.line(surface, rose, (600, 250), (width, 250))
	pygame.draw.line(surface, rose, (600, 375), (width, 375))
	pygame.draw.line(surface, rose, (600, 500), (width, 500))

	for i in range(ligne):
		for j in range(cologne):
			if obstacles[i][j] != None:

				if (obstacles[i][j])[1] == 1:
					#pygame.draw.rect(surface, red, (obstacles[i][j])[0])
					surface.blit( blocks[3] ,  (obstacles[i][j])[0])
				elif (obstacles[i][j])[1] == 2:
					#pygame.draw.rect(surface, blue, (obstacles[i][j])[0])
					surface.blit( blocks[2] ,  (obstacles[i][j])[0])
				elif (obstacles[i][j])[1] == 3:
					#pygame.draw.rect(surface, yellow, (obstacles[i][j])[0])
					surface.blit( blocks[0] ,  (obstacles[i][j])[0])
				elif (obstacles[i][j])[1] == 4:
					#pygame.draw.rect(surface, green, (obstacles[i][j])[0])
					surface.blit( blocks[1] ,  (obstacles[i][j])[0])
				elif (obstacles[i][j])[1] == 5:
					surface.blit(blocks_fissure[ (obstacles[i][j])[2] ], (obstacles[i][j])[0])
				elif (obstacles[i][j])[1] == 6:
					#pygame.draw.rect(surface, white, (obstacles[i][j])[0])
					surface.blit(blocks[4], (obstacles[i][j])[0])
				elif (obstacles[i][j])[1] == 7:
					#pygame.draw.rect(surface, crystal, (obstacles[i][j])[0])
					surface.blit(blocks[5], (obstacles[i][j])[0])
				elif (obstacles[i][j])[1] == 8:
					surface.blit(capsule, (obstacles[i][j])[0])
				else:
					surface.blit(blocks[6], (obstacles[i][j])[0])



def move():
	global walkCount , fallCount ,x, y , liste_blocks , compteur_drill , GameOver , Death , second_death , obstacles \
		, death_depth

	if walkCount + 1 >= 27:
		walkCount = 0
	if fallCount+1 == 6:
		fallCount = 0
	if Death == 2:
		if second_death >= 100:
			image_ange = ange
			image_ange = pygame.transform.scale(image_ange, (55, 55))
			surface.blit(image_ange, (x - 10, y - 10))
		else:
			image_death = dead_crash
			image_death = pygame.transform.scale(image_death, (55, 55))
			surface.blit(image_death, (x - 10, y - 10))
	elif Death == 1:
		if second_death >= 100:
			image_ange = ange
			image_ange = pygame.transform.scale(image_ange, (55, 55))
			surface.blit(image_ange, (x - 10, y - 10))
		else:
			image_air = dead_air
			image_air = pygame.transform.scale(image_air, (55, 55))
			surface.blit(image_air, (x - 10, y - 10))

	elif not collision_horizontal:
		image_fall = pygame.transform.scale(fall[fallCount // 3], (55, 55))
		surface.blit(image_fall, (x - 10, y - 10))
		fallCount += 1
		y += gravity

	elif compteur_drill != 0:
		if drill_right and not drill_left:
			image_d_right = image_drill_right
			image_d_right = pygame.transform.scale(image_d_right, (55, 55))
			surface.blit(image_d_right, (x - 10, y - 10))
		elif not drill_right and drill_left:
			image_d_left = image_drill_left
			image_d_left = pygame.transform.scale(image_d_left, (55, 55))
			surface.blit(image_d_left, (x - 10, y - 10))
		else:
			image_d_down = image_drill_down
			image_d_down = pygame.transform.scale(image_d_down, (55, 55))
			surface.blit(image_d_down, (x - 10, y - 10))
		compteur_drill -= 1
	else:
		if left == True:
			image_left = walkLeft[walkCount//3]
			image_left = pygame.transform.scale(image_left, (55, 55))
			surface.blit(image_left , (x-10,y-10))
			walkCount += 1
		elif right == True:
			image_right = walkRight[walkCount // 3]
			image_right = pygame.transform.scale(image_right, (55, 55))
			surface.blit(image_right , (x-10,y-10))
			walkCount += 1
		else:
			image_centre = pygame.transform.scale(centre, (55, 55))
			surface.blit(image_centre, (x - 10, y - 10))

	for element in liste_blocks:
		square = element[0]
		compteur = element[1]
		seconds_gravity = element[2]
		if compteur == 50:
			i,j = element[5] , element[3]
			destruction_block(i,j)
			liste_blocks.remove(element)
		else:
			if compteur == 0:
				if seconds_gravity == 100:
					square.x = element[3]*50
					square.y += gravity
					element[1] += gravity
				else:
					if seconds_gravity % 5 == 0:
						if element[4] == -2:
							element[4] = 2
						else:
							element[4] = -2
						square.x += element[4]
			else:
				square.y += gravity
				element[1] += gravity
				i,j =  element[5] , element[3]
				if obstacles[i][j] != None:
					if (obstacles[i][j])[1] != 8:
						if (square.bottom-5 > driller.top and ( square.left-5 < driller.left < square.right-5 or
						square.left+5 < driller.right < square.right+5) ):
							GameOver = True
							Death = 2
							death_depth = [i,j]


def events():
	global left , right , x , y , walkCount , collision_vertical_right , collision_vertical_left , drill_right , drill_left

	keys = pygame.key.get_pressed()

	if compteur_drill == 0:
		if not GameOver:
			if keys[pygame.K_LEFT] and x > 5:
				if not collision_vertical_left:
					x -= 5
				left = True
				right = False
				drill_right = False
				drill_left = False
			elif keys[pygame.K_RIGHT] and x < 560:
				if not collision_vertical_right:
					x += 5
				drill_right = False
				drill_left = False
				right = True
				left = False
			else:
				right = False
				left = False
				drill_left = False
				drill_right = False
				walkCount = 0

	if jump == True:
		if not GameOver:
			if keys[pygame.K_SPACE]:
				y -= 55

def collisions_player():
	global collision_vertical_right , collision_vertical_left , collision_horizontal , x,y , jump , obstacles ,\
		drill_ticker , drill_right , drill_left , compteur_drill , pourcentage , points , profondeur , death_depth

	keys = pygame.key.get_pressed()
	liste = []
	for i in range(ligne):
		for j in range(cologne):
			if obstacles[i][j] != None:
				square = (obstacles[i][j])[0]
				if driller.colliderect(square):
					if y == square.y - 45:
						collision_horizontal = True
						liste.append((i,j))
						profondeur = ( ligne*(level-1) ) + i
					else:
						jmp = False
						if x == square.x + 45:
							if (obstacles[i][j])[1] != 8:
								collision_vertical_left = True
								if (obstacles[i][j])[1] == 7:
									if (obstacles[i][j])[2] == 0:
										(obstacles[i][j])[2] += 1
								if not GameOver:
									if keys[pygame.K_q] and drill_ticker == 0:
										collisions_blocks(i, j)
										drill_left = True
										drill_right = False
										compteur_drill = 20
										drill_ticker = 20

								if i != 0:
									if (obstacles[i - 1][j]) != None:
										if (obstacles[i - 1][j ])[1] != 8:
											if (obstacles[i - 1][j])[0].bottom + 5 == driller.top:
												jmp = True
									if (obstacles[i - 1][j+1]) != None:
										if (obstacles[i - 1][j+1])[1] != 8:
											if (obstacles[i - 1][j+1])[0].bottom + 5 == driller.top:
												jmp = True
									if jmp == False:
										jump = True
								else:
									jump = True
							else:
								obstacles[i][j] = None
								points += 1
								pourcentage += 20

						if x == square.x - 35:
							if (obstacles[i][j])[1] != 8:
								collision_vertical_right = True
								if (obstacles[i][j])[1] == 7:
									if (obstacles[i][j])[2] == 0:
										(obstacles[i][j])[2] += 1
								if not GameOver:
									if keys[pygame.K_e] and drill_ticker == 0:
										drill_ticker = 20
										collisions_blocks(i, j)
										drill_right = True
										drill_left = False
										compteur_drill = 20

								if i != 0:
									if (obstacles[i-1][j]) != None:
										if (obstacles[i - 1][j])[1] != 8:
											if (obstacles[i-1][j])[0].bottom+5 == driller.top:
												jmp = True
									if (obstacles[i-1][j-1]) != None:
										if (obstacles[i - 1][j - 1])[1] != 8:
											if (obstacles[i-1][j-1])[0].bottom+5 == driller.top:
												jmp = True
									if jmp == False:
										jump = True
								else:
									jump = True
							else:
								obstacles[i][j] = None
								points += 1
								pourcentage += 20

	for element in liste:
		i = element[0]
		j = element[1]
		if obstacles[i][j] != None:
			square = (obstacles[i][j])[0]
			if len(liste) == 2:
				if square.x+15 == x:
					if Death == 1:
						death_depth = [i,j]
						x -= 5
					if (obstacles[i][j])[1] != 8:
						if (obstacles[i][j])[1] == 7:
							if (obstacles[i][j])[2] == 0:
								(obstacles[i][j])[2] += 1
						if not GameOver:
							if keys[pygame.K_w]: # Right
								if obstacles[i][j] != None:
									collisions_blocks(i, j)
									x -= 5
									drill_ticker = 20
									drill_right = True
									drill_left = False
									compteur_drill = 20
					else:
						obstacles[i][j] = None
						points += 1
						pourcentage += 20

				elif square.x-5 == x:
					if Death == 1:
						death_depth = [i, j]
						x += 5
					if (obstacles[i][j])[1] != 8:
						if (obstacles[i][j])[1] == 7:
							if (obstacles[i][j])[2] == 0:
								(obstacles[i][j])[2] += 1
						if not GameOver:
							if keys[pygame.K_w]: # Left
								if obstacles[i][j] != None:
									collisions_blocks(i, j)
									x += 5
									drill_right = False
									drill_right = True
									drill_ticker = 20
									compteur_drill = 20
					else:
						obstacles[i][j] = None
						points += 1
						pourcentage += 20
			else:
				if Death == 1:
					death_depth = [i, j]
				if (obstacles[i][j])[1] != 8:
					if (obstacles[i][j])[1] == 7:
						if (obstacles[i][j])[2] == 0:
							(obstacles[i][j])[2] += 1
					if not GameOver:
						if keys[pygame.K_w]: # Down
							if obstacles[i][j] != None and drill_ticker == 0:
								drill_ticker = 20
								collisions_blocks(i, j)
								drill_right = False
								drill_right = False
								compteur_drill = 20
				else:
					obstacles[i][j] = None
					points += 1
					pourcentage += 20

def gravity_blocks():
	global obstacles , gravity , liste_blocks
	liste = []

	for i in range(1 , ligne):
		for j in range(0,cologne):
			if obstacles[i][j] == None and obstacles[i-1][j] != None:
				liste.append( (i-1 , i , j) )

	for element in liste:
		i = element[1]
		i_1 = element[0]
		j = element[2]
		j_sup = j+1
		if (obstacles[i_1][j])[1] != 6:
			continue_sup = False
			while j_sup < cologne and i_1+1 < ligne:
				if obstacles[i_1][j_sup] != None:
					if (obstacles[i_1][j])[1] == (obstacles[i_1][j_sup])[1]:
						if obstacles[i_1+1][j_sup] != None:
							continue_sup = True
							break
					else:
						break
				else:
					break
				j_sup += 1
			if continue_sup:
				continue

			j_inf = j-1
			continue_inf = False
			while j_inf < cologne and i_1 + 1 < ligne:
				if obstacles[i_1][j_inf] != None:
					if (obstacles[i_1][j])[1] == (obstacles[i_1][j_inf])[1]:
						if obstacles[i_1 + 1][j_inf] != None:
							continue_inf = True
							break
					else:
						break
				else:
					break
				j_inf -= 1
			if continue_inf:
				continue

		obstacles[i][j] = obstacles[i_1][j]
		obstacles[i_1][j] = None
		liste_blocks.append( [ (obstacles[i][j])[0] , 0 , 0 , j , 2, i ] )



def collisions_blocks(i,j):
	global obstacles , points , NextLevel

	if (obstacles[i][j])[1] == 9:
		NextLevel = True

	elif (obstacles[i][j])[1] != 8:
		liste = [ (i,j) ]
		compteur = 1
		while compteur != 0:
			compteur = 0
			for element in liste:
				position_i = element[0]
				position_j = element[1]
				i_sup = position_i + 1
				i_inf = position_i - 1
				j_sup = position_j + 1
				j_inf = position_j - 1
				if i_sup < ligne and obstacles[i_sup][position_j] != None:
					if (i_sup , position_j) not in liste:
						if (obstacles[position_i][position_j])[1] == (obstacles[i_sup][position_j])[1]:
							liste.append((i_sup, position_j))
							compteur += 1

				if i_inf >= 0 and obstacles[i_inf][position_j] != None:
					if (i_inf , position_j) not in liste:
						if (obstacles[position_i][position_j])[1] == (obstacles[i_inf][position_j])[1]:
							liste.append((i_inf, position_j))
							compteur += 1

				if j_sup < cologne and obstacles[position_i][j_sup] != None:
					if (position_i,j_sup) not in liste:
						if (obstacles[position_i][position_j])[1] == (obstacles[position_i][j_sup])[1]:
							liste.append((position_i, j_sup))
							compteur += 1

				if j_inf >= 0 and obstacles[position_i][j_inf] != None:
					if (position_i,j_inf) not in liste:
						if (obstacles[position_i][position_j])[1] == (obstacles[position_i][j_inf])[1]:
							liste.append((position_i, j_inf))
							compteur += 1

		pop_block.play()

		for element in liste:
			i = element[0]
			j = element[1]
			if len(obstacles[i][j]) == 4:
				if (obstacles[i][j])[2] < 5:
					(obstacles[i][j])[2] += 1
			else:
				obstacles[i][j] = None
				points += 1

def destruction_block(i,j):
	global obstacles , merge_blocks , pourcentage , points

	liste = [(i, j)]
	compteur = 1
	cpt_global = 1
	while compteur != 0:
		compteur = 0
		for element in liste:
			position_i = element[0]
			position_j = element[1]
			i_sup = position_i + 1
			i_inf = position_i - 1
			j_sup = position_j + 1
			j_inf = position_j - 1
			if obstacles[position_i][position_j] != None:
				if i_sup < ligne and obstacles[i_sup][position_j] != None:
					if (i_sup, position_j) not in liste:
						if (obstacles[position_i][position_j])[1] == (obstacles[i_sup][position_j])[1]:
							liste.append((i_sup, position_j))
							compteur += 1
							cpt_global += 1

				if i_inf >= 0 and obstacles[i_inf][position_j] != None:
					if (i_inf, position_j) not in liste:
						if (obstacles[position_i][position_j])[1] == (obstacles[i_inf][position_j])[1]:
							liste.append((i_inf, position_j))
							compteur += 1
							cpt_global += 1

				if j_sup < cologne and obstacles[position_i][j_sup] != None:
					if (position_i, j_sup) not in liste:
						if (obstacles[position_i][position_j])[1] == (obstacles[position_i][j_sup])[1]:
							liste.append((position_i, j_sup))
							compteur += 1
							cpt_global += 1

				if j_inf >= 0 and obstacles[position_i][j_inf] != None:
					if (position_i, j_inf) not in liste:
						if (obstacles[position_i][position_j])[1] == (obstacles[position_i][j_inf])[1]:
							liste.append((position_i, j_inf))
							compteur += 1
							cpt_global += 1
	if cpt_global >= 4:
		pop_block.play()
		for element in liste:
			i1 = element[0]
			j1 = element[1]
			points += 1
			if len(obstacles[i1][j1]) == 4:
				surface.blit(blocks_fissure[5], (obstacles[i1][j1])[0])
				obstacles[i1][j1] = None
			else:
				obstacles[i1][j1] = None


def save():
	fopen = open("Save/sauvegarde.txt","a")
	fopen.close()

	fichier = open("Save/sauvegarde.txt","r")
	ecraser = False
	list_name = []
	lines = fichier.readlines()

	if len(lines) != 0:
		for user in lines:
			for i in range(len(user)):
				if user[i] == ':':
					list_name.append([user[0:i-1] , int(user[i+1:])])
					
		for element in list_name:
			if username == element[0]:
				ecraser = True
				if points > element[1]:
					list_name.remove(element)
					list_name.append([username,points])


		fic = open("Save/sauvegarde.txt","w")

		for element in list_name:
			fic.write(element[0]+' : '+str(element[1])+'\n')

		fic.close()

	fichier.close()


	if not ecraser:

		fichier = open('Save/sauvegarde.txt' , 'a')

		fic = open('Save/sauvegarde.txt' , 'r')
		ligne = fic.readline()

		if len(ligne) != 0:
			fichier.write("\n"+username+" : "+str(points))
		else:
			fichier.write(username+" : "+str(points))
		
		fic.close()
		fichier.close()
	
def load():
	global game_over

	fichier = open("Save/sauvegarde.txt" , "r")

	liste_trie = []

	lignes = fichier.readlines()

	for ligne in lignes:
		for i in range(len(ligne)):
			if ligne[i] == ':':
				liste_trie.append( [ligne[0:i],int(ligne[i+1:])] )


	cpt = 1
	while cpt != 0:
		cpt = 0
		for i in range(len(liste_trie)-1):
			element_1 = liste_trie[i]
			element_2 = liste_trie[i+1]
			if element_1[1] < element_2[1]:
				temp = element_1
				liste_trie[i] = element_2
				liste_trie[i+1] = temp
				cpt += 1

	fichier.close()

	for event in pygame.event.get():
		if event.type == QUIT:
			game_over = True

	pos_x , pos_y = 250,150
	surface.fill(black)

	img = pygame.image.load("Screens/HighScore.png")
	surface.blit(img , (250,-50))

	font = pygame.font.Font("Screens/monospace.ttf",30)

	texte , texte1 = font.render("Name" , True , green) , font.render("Score" , True , green)
	rectangle , rectangle1 = texte.get_rect() , texte1.get_rect()
	rectangle.topleft = (pos_x , pos_y)
	rectangle1.topleft = (pos_x+250,pos_y)

	surface.blit(texte , rectangle)
	surface.blit(texte1,rectangle1)

	pos_y +=50

	for element in liste_trie:
		texte = font.render(element[0] ,True,white)
		texte1 = font.render(str(element[1]),True,white)
		rectangle = texte.get_rect()
		rectangle1 = texte1.get_rect()
		rectangle.topleft = (pos_x,pos_y)
		rectangle1.topleft = (pos_x+250,pos_y)
		surface.blit(texte , rectangle)
		surface.blit(texte1,rectangle1)
		pos_y += 50

def pause():
	global Paused , game_over

	if Paused == 1:
		paused = True
		font = pygame.font.Font("freesansbold.ttf",40)
		texte = font.render("Paused",True,white)
		rectangle = texte.get_rect()
		rectangle.topleft = (200,50)
		while paused:
			pygame.draw.rect(surface,black,rectangle,0)
			surface.blit(texte,rectangle)
			for event in pygame.event.get():
				if event.type == QUIT:
					paused = False
					game_over = True
				if event.type == KEYDOWN:
					if event.key == K_p:
						paused = False
						Paused += 1
						if Paused == 2:
							Paused = 0
			pygame.display.update()


def lose(second):
	global y , GameOver , pourcentage , Death , CountDeath

	if second == 80:
		if len(death_depth) != 0:
			i,j = death_depth[0],death_depth[1]
			for k in range(i, -1, -1):
				obstacles[k][j] = None
	if second >= 100:
		y -= gravity
		if second == 200:
			GameOver = False
			pourcentage = 100
			Death = 0
			CountDeath -= 1

def gameover(death_screen):
	global game_over

	for event in pygame.event.get():
		if event.type == QUIT:
			game_over = True

	if death_screen == 0:
		pygame.mixer.music.stop()
		pygame.mixer.music.load("Music/GameOver.wav")
		pygame.mixer.music.play(0)

	img = pygame.image.load("Screens/GameOver.jpg")
	img = pygame.transform.scale(img, (width, height))
	surface.blit(img , (0,0))


def win(win_screen):
	global game_over

	for event in pygame.event.get():
		if event.type == QUIT:
			game_over = True

	if win_screen == 0:
		pygame.mixer.music.stop()
		pygame.mixer.music.load("Music/WinTheme.wav")
		pygame.mixer.music.play(0)

	surface.fill(black)
	img = pygame.image.load("Screens/Win.jpg")
	img = pygame.transform.scale(img, (width, height-200))
	surface.blit(img , (0,200))	

	message = "Congratulations !!"
	message1 = "Game Completed"
	font = pygame.font.Font("freesansbold.ttf",50)
	texte = font.render(message,True,white)
	texte1 = font.render(message1,True,white)
	rectangle = texte.get_rect()
	rectangle.topleft = (200,50)
	rectangle1 = texte1.get_rect()
	rectangle1.topleft = (200,120)

	surface.blit(texte , rectangle)
	surface.blit(texte1 , rectangle1)


def main():
	global game_over , collision_horizontal , collision_vertical_left , collision_vertical_right , jump , driller,\
		x, y , obstacles , drill_ticker , liste_blocks , merge_blocks , pourcentage , points , second_death , CountDeath , Capsule_Air , NextLevel , level , Paused
	drill_ticker , second = 0 , 0
	liste_blocks = []
	merge_blocks = []
	second_death = 0
	driller , level = 1 , 1
	pygame.mixer.music.load("Music/main.mp3")
	pygame.mixer.music.play(-1)
	NextLevel = False
	cpt_save , Paused= 0 , 0
	death_screen , win_screen = 0,0 

	while not game_over:
		clock.tick(60)

		if CountDeath != 0 and level != 11:
			collision_horizontal = False
			collision_vertical_left = False
			collision_vertical_right = False
			jump = False

			if NextLevel:
				initialise()
				level += 1
				pourcentage = 100
				points += 10
				Capsule_Air -= 1
				NextLevel = False

			driller = pygame.Rect(x, y, 40, 50)

			for event in pygame.event.get():
				if event.type == QUIT:
					game_over = True
				if event.type == KEYDOWN:
					if event.key == K_p:
						Paused += 1

			if drill_ticker > 0:
				drill_ticker -= 1

			if not GameOver:
				second_death = 0
				second += 1
				if second == 60:
					second = 0
					pourcentage -= 1
				if y >= 300:
					y -= 50
					for i in range(ligne):
						for j in range(cologne):
							if obstacles[i][j] != None:
								(obstacles[i][j])[0].y -= 50
				if y <= 100:
					y += 50
					for i in range(ligne):
						for j in range(cologne):
							if obstacles[i][j] != None:
								(obstacles[i][j])[0].y += 50
			else:
				second_death += 1
				lose(second_death)

			for element in liste_blocks:
				element[2] += 1
			for i in range(ligne):
				for j in range(cologne):
					if obstacles[i][j] != None:
						if len(obstacles[i][j]) == 4:
							if (obstacles[i][j])[2] == 5:
								(obstacles[i][j])[3] += 1
								if (obstacles[i][j])[3] == 20:
									obstacles[i][j] = None
									pourcentage -= 20
									points += 1
					if obstacles[i][j] != None:
						if (obstacles[i][j])[1] == 7:
							if (obstacles[i][j])[2] >= 1:
								(obstacles[i][j])[2] += 1
								if (obstacles[i][j])[2] == 500:
									obstacles[i][j] = None
									pop_block.play()
			draw()
			air()
			collisions_player()
			gravity_blocks()
			move()
			events()
			score(points)
			depth(profondeur)
			lives(CountDeath)
			levels()
			pause()
		else:
			if cpt_save == 0:
				save()
				cpt_save += 1
			if CountDeath == 0 and death_screen < 100:
				gameover(death_screen)
				death_screen += 1
			elif level == 11 and win_screen < 100:
				win(win_screen)
				win_screen += 1
			else:
				load()
		pygame.display.update()
	pygame.quit()

# Lancemant :

launch , username = saisie()

if launch == True:
	play = intro()
	if play == True:
		pygame.mixer.music.stop()
		initialise()
		main()

	else:
		pygame.quit()
else:
	pygame.quit()

