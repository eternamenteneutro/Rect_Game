#Dupla: Daniel e Mariana, 1.18.1M

#"Rect" game (adaptação do jogo da cobrinha)
#dimensoes feitas para formato de celular e não de computador:)

#usamos a biblioteca do pygame para a produção
import pygame
from pygame.locals import *
from sys import exit
import random
from random import randint

pygame.init()

#informacoes dos textos que serao inseridos no jogo
fonte = pygame.font.SysFont('arial', 55, True, False)
fonte2 = pygame.font.SysFont('arial', 100, True, False)

#variaveis
pontos = 0

#parametros para o tamanho da tela
largura = 1000
altura = 2000

tempo = pygame.time.Clock()
FPS = 18

#posicao do bloco do jogador
x = largura/2
y = altura/2

#cor 
r,g,b = 25,100,70
yelo = 255
txt_r,txt_g,txt_b = 255,000,255

tx, ty = 40, 40
rx, ry = randint(10,800), randint(10,1200)

dez=10
RX, RY = randint(0,1000), randint(0,1395)
inmg_largura, inmg_altura = 80, 90
RX2, RY2 = randint(0,1000), randint(0,1395)
RX3,RY3 = randint(0,900), randint(0,1395)
rd, re, rc, rb=0, 0, 0, 0
rf, gf, bf, rl = 255,255,255, 0

tocado = False
nivel = 0
damage = 1
aceleracao = 0
vel=5
comido=False
var = 30
musica2 = "fundo2.mp3"
musica = "fundo.mp3"
tela = pygame.display.set_mode((largura,altura))

width = tela.get_width()
height = tela.get_height()

#speed = [4, 4]


#reprodução da musica
pygame.mixer.music.load(musica)
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)

while True:
	
	#frames por segundo da animação
	tempo.tick(FPS)
	
	#limpa a tela quando os objetos se movem
	tela.fill((rf,gf,bf))
	
	#mensagem que sera exibida na tela
	msg = f'pontos: {pontos}'
	texto_form = fonte.render(msg, True, (txt_r,txt_g,txt_b))
	
	#definindo os controles de movimentacao do bloco verde
	ct_up = f'A'
	control_up = fonte.render(ct_up, False, (255,255,0))
	ct_right = f'B'
	control_right = fonte.render(ct_right, False, (yelo,yelo,0))
	
	ct_down = f'C'
	control_down = fonte.render(ct_down, False, (yelo,yelo,0))
	
	ct_left = f'D'
	control_left = fonte.render(ct_left, False, (yelo,yelo,0))
			
			
	direita= pygame.draw.circle(tela, (rd,0,0), (750,1750), 80)
	esquerda= pygame.draw.circle(tela, (re,0,0), (450,1750), 80)
	cima= pygame.draw.circle(tela, (rc,0,0), (600,1600), 80)
	baixo= pygame.draw.circle(tela, (rb,0,0), (600,1900), 80)
	
	
	#linha que separa a tela dos objetos com a tela dos controles
	linha= pygame.draw.line(tela, (rl,0,0), (-20,1400), (1200,1400), 5)
	
	#criando os nossos atores no jogo(voce, a maçã e o inimigo)
	rect_voce = pygame.draw.rect(tela, (r,g,b), (x,y,tx,ty))
	
	rect_maca = pygame.draw.rect(tela, (255,0,0), (rx,ry,40,40))

	RECT_inimigo = pygame.draw. rect(tela, (0, 50, 200), (RX,RY, inmg_largura,inmg_altura))
	
	#eventos se voce cruza a linha
	if rect_voce.colliderect(linha):
		y = y-8
		
	#eventos se voce comer a maçã
	if rect_voce.colliderect(rect_maca):
		rx = randint(10,980)
		ry = randint(10,1380)
		pontos=pontos + 1
		aceleracao=aceleracao+2
		comido = True
		som = pygame.mixer.Sound("notificação do zap.ogg")
		som.play()
		som.set_volume(0.1)
		
	#eventos se voce encostar no inimigo
	if rect_voce.colliderect(RECT_inimigo):
		pontos = pontos -damage
		RX=randint(10,750)
		RY=randint(10,1250)
		dano = pygame.mixer.Sound("damage.wav")
		dano.play()
		dano.set_volume(0.6)
	
		
	#fases
	if pontos ==-365:
		pygame.mixer.music.stop()
		pygame.mixer.music.load(musica)
		pygame.mixer.music.play(-1)
		pygame.mixer.music.set_volume(0.2)
		pontos =0
	if nivel == 0:
		rf,gf,bf = 255, 255, 255
		yelo = 255
		txt_r,txt_g,txt_b =255,0,255
		
		
		
	if pontos>=10 and nivel ==0:
		nivel=nivel+1
		pontos = 0
		pygame.mixer.music.stop()
		pygame.mixer.music.load("fundo3.mp3")
		pygame.mixer.music.play(-1)
		pygame.mixer.music.set_volume(0.2)
		
	if pontos>=20 and nivel ==1:
		nivel = nivel+1
		pygame.mixer.music.stop()
		pygame.mixer.music.load("fundo2.mp3")
		pygame.mixer.music.play(-1)
		pygame.mixer.music.set_volume(0.3)
		
	if pontos ==50 and nivel ==2:
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
			dano = pygame.mixer.Sound("damage.wav")
			dano.play()
			dano.set_volume(0.6)
			
		if RECT_inimigo2.colliderect(linha):
			RY2=RY2-80
		if RX2 >=largura:
			RX2=RX2-90
		if RX2 <=0:
			RX2=RX2+90
		if RY2<=0:
			RY2=RY2+80
			
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
			dano = pygame.mixer.Sound("damage.wav")
			dano.play()
			dano.set_volume(0.6)
		
		if RECT_inimigo3.colliderect(linha):
			RY3=RY3-100
		if RX3 >=largura:
			RX3=RX3-100
		if RX2 <=0:
			RX3=RX3+100
		if RY3<=0:
			RY3=RY3+100
					
					
					
	#tela de game win
	if nivel ==3:
		rd,re,rc,rb,rl = 0,0,0,0,0
		som_gamewin=pygame.mixer.Sound("gamewin.ogg")
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
	if nivel ==-1:
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
		tela.blit(texto_reinit, (largura/2 -300, altura/2))
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				if cima.collidepoint(event.pos):
					nivel = 0
					pontos =-365


#condicao para que a tela de game over seja aberta
	if pontos<0 and pontos >-300:
		gameover=pygame.mixer.music
		gameover.load("gameoversound.mp3")
		gameover.play(1)
		gameover.set_volume(0.5)
		pontos = -1000
		nivel = -1
	
	
		
		
	for event in pygame.event.get():
    
    
	#movimento dos controles
		if event.type == pygame.MOUSEBUTTONDOWN:
	
			if direita.collidepoint(event.pos):
				x=x+aceleracao
				aceleracao=20
				
					
			if esquerda.collidepoint(event.pos):
				x=x-aceleracao
				aceleracao=20
				
				
			if cima.collidepoint(event.pos):
				y=y-aceleracao
				aceleracao=20
				
			
			if baixo.collidepoint(event.pos):
				y=y+aceleracao
				aceleracao=20
				
	if ry>= 1360:
		ry = 0
		RX, RY = RX+randint(-20,20), RY+randint(-40,50)
	
	
	#para impedir que o bloco do jogador ultrapasse a tela do jogo
	if x < 0:
		x=x+20
	if x > largura+40:
		x=x-20
	if y < 0:
		y=y+20
	
		
	#para impedir que o bloco inimigo ultrapasse a tela do jogo
	if RECT_inimigo.colliderect(linha):
		RY=RY-80
	if RX >=largura:
		RX=RX-90
	if RX <=0:
		RX=RX+90
	if RY<=0:
		RY=RY+80
		
	#O inimigo começa a se movimentar assim que voce come a primeira maçã
	if comido == True:
		RX = RX+randint(-var,var)
		RY = RY+randint(-var,var)
		
		
#mostra os objetos na tela
	tela.blit(control_up, (580,1570))
	tela.blit(control_right, (735,1720))
	tela.blit(control_down, (580,1875))
	tela.blit(control_left, (435,1725))
	
	tela.blit(texto_form, (740,60))
	
	#atualiza a a tela a cada interação do while
	pygame.display.flip()
	
	
	#codigos fontes retirados de https://youtube.com/@joaotinti5293 curso de pygame com Joao Tini