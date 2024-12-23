
'''corrija:
	*As msicas do nivel 1 e game over
	*a velocidade do jogador
	*a forma de input dos controles
	*o som de quando vc encosta no inimigo'''
#"Rect" game (adaptação do jogo da cobrinha)
import pygame
from pygame.locals import *
from sys import exit
from random import randint
pygame.init()

#informacoes dos textos que serao inseridos no jogo
fonte = pygame.font.SysFont('arial', 30, True, False)
fonte2 = pygame.font.SysFont('arial', 100, True, False)

#parametros para o tamanho da tela
largura = 1280
altura = 720
escala = 2
tempo = pygame.time.Clock()
FPS = 30
nivel = 0
pontos = 0
letra = 15
#posicao do bloco do jogador
x = largura/2
y = altura/2

#cor 
r,g,b = 25,100,70
yelo = 255
txt_r,txt_g,txt_b = 255,000,255

#coordenadas dos elementos
tx, ty = 40, 40
rx, ry = randint(10,1000), randint(10,600)
RX, RY = randint(0,1000), randint(0,600)
inmg_largura, inmg_altura = 64, 72
RX2, RY2 = randint(0,1000), randint(0,600)
RX3,RY3 = randint(0,900), randint(0,600)
rd, re, rc, rb=0, 0, 0, 0
rf, gf, bf, rl = 255,255,255, 0

pressD, pressA, pressW, pressS = False, False, False, False
damage = 1
aceleracao = 0
vel=5
comido=False
var = 20
musica = ["sounds/gameoversound.mp3", "sounds/fundo.mp3", "sounds/fundo2.mp3", "sounds/fundo3.mp3"]
tela = pygame.display.set_mode((largura,altura))

width = tela.get_width()
height = tela.get_height()

#reprodução da musica

######################################################################
while True:
	while pressD:
		pressW, pressA, pressS, pressD = False, False, False, False
		x = x + aceleracao
	while pressA:
		pressW, pressA, pressS, pressD = False, False, False, False
		x = x - aceleracao
	while pressW:
		pressW, pressA, pressS, pressD = False, False, False, False
		y = y - aceleracao
	while pressS:
		pressW, pressA, pressS, pressD = False, False, False, False
		y = y + aceleracao

	#frames por segundo da animação
	tempo.tick(FPS)
	aceleracao=5
	#limpa a tela quando os objetos se movem
	tela.fill((rf,gf,bf))
	
	#mensagem que sera exibida na tela
	msg = f'pontos: {pontos}'
	texto_form = fonte.render(msg, True, (txt_r,txt_g,txt_b))

	##############################################################

	#definindo os controles de movimentacao do bloco verde
	ct_up = f'A'
	control_up = fonte.render(ct_up, False, (255,255,0))
	ct_right = f'B'
	control_right = fonte.render(ct_right, False, (yelo,yelo,0))
	
	ct_down = f'C'
	control_down = fonte.render(ct_down, False, (yelo,yelo,0))
	
	ct_left = f'D'
	control_left = fonte.render(ct_left, False, (yelo,yelo,0))
			
			
	direita= pygame.draw.circle(tela, (rd,0,0), (1200,300), 30)
	esquerda= pygame.draw.circle(tela, (re,0,0), (1100,300), 30)
	cima= pygame.draw.circle(tela, (rc,0,0), (1150,250), 30)
	baixo= pygame.draw.circle(tela, (rb,0,0), (1150,350), 30)
	
	
	#linha que separa a tela dos objetos com a tela dos controles
	linha= pygame.draw.line(tela, (rl,0,0), (1000,-40), (1000,750), 5)
	
	#criando os nossos atores no jogo(voce, a maçã e o inimigo)
	rect_voce = pygame.draw.rect(tela, (r,g,b), (x,y,tx,ty))
	
	rect_maca = pygame.draw.rect(tela, (255,0,0), (rx,ry,32,32))

	RECT_inimigo = pygame.draw. rect(tela, (0, 50, 200), (RX,RY, inmg_largura,inmg_altura))

##############################################################################

	#voce cruza a linha
	if rect_voce.colliderect(linha):
		x = x - 5
		
	#voce come a maçã
	if rect_voce.colliderect(rect_maca):
		rx = randint(10,978)
		ry = randint(10,600)
		pontos=pontos + 1
		aceleracao=aceleracao+2
		comido = True
		som = pygame.mixer.Sound("sounds/not_zap.ogg")
		som.play()
		som.set_volume(0.1)
		
	#voce encosta no inimigo
	if rect_voce.colliderect(RECT_inimigo):
		pontos = pontos -damage
		RX=randint(10,970)
		RY=randint(10,640)
		dano = pygame.mixer.Sound("sounds/damage.wav")
		dano.play()
		dano.set_volume(0.8)
	
#############################################################################
	#fases
	if pontos < 5 and nivel == 0:
		pygame.mixer.music.load(musica[1])
		pygame.mixer.music.play(-1)
		pygame.mixer.music.set_volume(0.5)
		rf,gf,bf = 255, 255, 255
		yelo = 255
		txt_r,txt_g,txt_b =255,0,255
		
		
	if pontos>=5 and nivel ==0:
		nivel=nivel+1
		pontos = 0
		pygame.mixer.music.stop()
		pygame.mixer.music.load(musica[2])
		pygame.mixer.music.play(-1)
		pygame.mixer.music.set_volume(0.5)
		
	if pontos>=5 and nivel ==1:
		nivel = nivel+1
		pontos = 0
		pygame.mixer.music.stop()
		pygame.mixer.music.load(musica[3])
		pygame.mixer.music.play(-1)
		pygame.mixer.music.set_volume(0.5)
		
	if pontos ==5 and nivel ==2:
		fonte_gw = pygame.font.SysFont('arial', 100, True, False)
		pygame.mixer.music.stop()
		nivel = 3
		
	#nova fase
	if nivel >= 1:
		damage=2
		rf, gf, bf = 200, 200, 255
		rd, re, rc, rb, rl = 0,0,0,0,0
		RECT_inimigo2 = pygame.draw.rect(tela, (0, 50, 200), (RX2,RY2, inmg_largura,inmg_altura))
		RX2, RY2 = RX2+randint(-20,20), RY2+randint(-20,20)
		if rect_voce.colliderect(RECT_inimigo2):
			pontos = pontos -damage
			RX2=randint(10,750)
			RY2=randint(10,1250)
			dano = pygame.mixer.Sound("sounds/damage.wav")
			dano.play()
			dano.set_volume(0.6)

		if RECT_inimigo2.colliderect(linha):
			RX2 = RX2 - 90
		if RY2 >= altura - 90:
			RY2 = RY2 - 90
		if RX2 <= 0:
			RX2 = RX2 + 90
		if RY2 <= 0:
			RY2 = RY2 + 90
			
	#nova fase
	if nivel >=2:
		damage=3
		rf,gf,bf = 0,0,0
		rd,re,rc,rb,rl =255,255,255,255,255
		RECT_inimigo3 = pygame.draw.rect(tela, (0, 50, 200), (RX3,RY3, inmg_largura,inmg_altura))
		RX3, RY3 = RX3+randint(-40,40), RY3+randint(-30,30)
		if rect_voce.colliderect(RECT_inimigo3):
			RX3,RY3 = randint(0,950), randint(0,1380)
			pontos = pontos -damage
			dano = pygame.mixer.Sound("sounds/damage.wav")
			dano.play()
			dano.set_volume(0.6)

		if RECT_inimigo3.colliderect(linha):
			RX3 = RX3 - 90
		if RY3 >= altura - 90:
			RY3 = RY3 - 90
		if RX3 <= 0:
			RX3 = RX3 + 90
		if RY3 <= 0:
			RY3 = RY3 + 90

# condicao para que a tela de game over seja aberta
	if pontos < 0:
		pontos = -301
		nivel = -1
		pygame.mixer.music.stop()
		pygame.mixer.music.load(musica[0])
		pygame.mixer.music.play(1)
		pygame.mixer.music.set_volume(1)


###############################################################################
					
	#tela de game win
	if nivel ==3:
		rd,re,rc,rb,rl = 0,0,0,0,0
		som_gamewin=pygame.mixer.Sound("sounds/gamewin.ogg")
		som_gamewin.play()
		som_gamewin.set_volume(0.8)
		x,y,rx,ry,RX,RY,RX2,RY2 = 0,0,900,0,900,900,0,900
		rf,gf,bf = 255,255,255
		gw = f'GAME WIN!'
		sgw=f'Congradulations!!!'
		texto_gw = fonte_gw.render(gw,True, (100,100,255))
		texto_sgw= fonte.render(sgw,True, (100,100,255))
		tela.blit(texto_gw, (largura/2-300, altura/2-300))
		tela.blit(texto_sgw, (largura/2-300, altura/2-150))
	#tela de game over
	if nivel == -1:
		x,y,rx,ry,RX,RY,RX2,RY2 = 0,0,900,0,900,900,0,900
		rf,gf,bf = 0,0,0
		txt_r,txt_g,txt_b = 0,0,0
		yelo = 0
		go = f'GAME OVER!'
		#para reiniciar o jogo
		reinit = f'press "A" to restart'
		texto_reinit = fonte.render(reinit, True, (255,0,0))
		texto_formato = fonte2.render(go, True, (255,0,0))
		tela.blit(texto_formato, (largura/2 - 300,altura/2 -150))
		tela.blit(texto_reinit, (largura/2 -120, altura/2))
		
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == K_a:
					nivel = 0
					pontos = 0
					rx, ry = randint(10, 1000), randint(10, 600)
					RX, RY = randint(0, 1000), randint(0, 600)
					'''pygame.mixer.music.load(musica[1])
					pygame.mixer.music.play(1)
					pygame.mixer.music.set_volume(0.8)'''

			if event.type == pygame.MOUSEBUTTONDOWN:
				if cima.collidepoint(event.pos):
					nivel = 0
					pontos =0
					rx, ry = randint(10, 1000), randint(10, 600)
					RX, RY = randint(0, 1000), randint(0, 600)
					pygame.mixer.music.load(musica[1])
					pygame.mixer.music.play(-1)

		
	#controles de movimento
	for event in pygame.event.get():
	#CLIQUES
		if event.type == pygame.MOUSEBUTTONDOWN:
	
			if direita.collidepoint(event.pos):
				pressD = True
				
					
			if esquerda.collidepoint(event.pos):
				pressA = True
				
				
			if cima.collidepoint(event.pos):
				pressW = True
				
			
			if baixo.collidepoint(event.pos):
				pressS = True


	#TECLADO
		if pygame.key.get_pressed()[K_d] or pygame.key.get_pressed()[K_RIGHT]:
			pressD = True

		if pygame.key.get_pressed()[K_a] or pygame.key.get_pressed()[K_LEFT]:
			pressA = True

		if pygame.key.get_pressed()[K_w] or pygame.key.get_pressed()[K_UP]:
			pressW = True

		if pygame.key.get_pressed()[K_s] or pygame.key.get_pressed()[K_DOWN]:
			pressS = True
####################condição dos controles ativarem
	'''while pressD:
		pressW, pressA, pressS, pressD = False, False, False, False
		x = x + aceleracao
	while pressA:
		pressW, pressA, pressS, pressD = False, False, False, False
		x = x - aceleracao
	while pressW:
		pressW, pressA, pressS, pressD = False, False, False, False
		y = y - aceleracao
	while pressS:
		pressW, pressA, pressS, pressD = False, False, False, False
		y = y + aceleracao'''

######################################################
	if ry>= 1360:
		ry = 0
		RX, RY = RX+randint(-20,20), RY+randint(-40,50)
	
	
	#para impedir que o bloco do jogador ultrapasse a tela do jogo
	if x < 0:
		x=x+32
	if y < 0:
		y=y+32
	if y >= altura-32:
		y=y-20
	
		
	#para impedir que o bloco inimigo ultrapasse a tela do jogo
	if RECT_inimigo.colliderect(linha):
		RX=RX-90
	if RY >=altura-90:
		RY=RY-90
	if RX <=0:
		RX=RX+90
	if RY<=0:
		RY=RY+90
		
	#O inimigo começa a se movimentar assim que voce come a primeira maçã
	if comido == True:
		RX = RX+randint(-var,var)
		RY = RY+randint(-var,var)
		

	#mostra os objetos na tela
	tela.blit(control_right, (1200-letra,300-letra))
	tela.blit(control_left, (1100-letra,300-letra))
	tela.blit(control_up, (1150-letra,250-letra))
	tela.blit(control_down, (1150-letra,350-letra))
	tela.blit(texto_form, (1080,45))
	pygame.display.flip()
	
	
	#codigos fontes retirados de https://youtube.com/@joaotinti5293 curso de pygame com Joao Tini