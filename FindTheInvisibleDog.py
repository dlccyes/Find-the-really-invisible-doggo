import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1080, 600))
done = False
generate_new_xy = True

def dis(x,y,a,b):
	'''(x,y) to (a,b) distance'''
	return ((x-a)**2+(y-b)**2)**(1/2)

while not done:
	pygame.time.delay(140)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	if generate_new_xy == True:
	    x = random.randint(1,1080)
	    y = random.randint(1,600)
	    print('(x,y)=({x},{y})'.format(x=x,y=y))
	    generate_new_xy = False
	mouse_pos = pygame.mouse.get_pos()
	if dis(mouse_pos[0],mouse_pos[1],x,y) <= 100:
		pygame.mixer.music.load('niao.mp3')
		pygame.mixer.music.play(0)
		if dis(mouse_pos[0],mouse_pos[1],x,y) <= 30:
			if pygame.mouse.get_pressed()[0] == 1:
				pygame.mixer.music.load('masterdoggo.mp3')
				pygame.mixer.music.play(0)
				print('YOU FOUND ME!!!!!')
				pygame.time.delay(4000)
				generate_new_xy = True
	elif 100 < dis(mouse_pos[0],mouse_pos[1],x,y) <= 400:
		pygame.mixer.music.load('niaoooo.mp3')
		pygame.mixer.music.play(0)
	else:
		pygame.mixer.music.load('urrrooo.mp3')
		pygame.mixer.music.play(0)
