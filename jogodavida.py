import pygame
import numpy as np
import time

pygame.init()

width = 500
height = 500

screen = pygame.display.set_mode((height,width))

bg = 25,25,25
screen.fill(bg)

nxC=25
nyC=25

dimCW= width /nxC
dimCh= height /nyC

#celula viva == 1 morta === 0
gameState = np.zeros((nxC, nyC))

gameState[5,3] = 1
gameState[5,4] = 1
gameState[5,5] = 1

pauseexect=False

while True:

    newGameState =  np.copy(gameState)

    screen.fill(bg)
    time.sleep(0.2)

    ev =  pygame.event.get()
    for event in ev:
      if event.type == pygame.KEYDOWN:
        pauseexect = not pauseexect
      mouseClick = pygame.mouse.get_pressed()
      if sum(mouseClick) > 0:
        posX, posY = pygame.mouse.get_pos()
        celX, celY = int(np.floor(posX/ dimCW)), int(np.floor(posY / dimCh))
        newGameState[celX, celY] = mouseClick[0]


    for y in range(0, nxC):
        for x  in range(0,nyC):
            if not pauseexect:
              n_neigh = gameState[(x-1) % nxC, (y-1) % nyC] + \
                        gameState[(x) % nxC, (y-1) % nyC] + \
                        gameState[(x+1) % nxC, (y-1) % nyC] + \
                        gameState[(x-1) % nxC, (y) % nyC] + \
                        gameState[(x+1) % nxC, (y) % nyC] + \
                        gameState[(x-1) % nxC, (y+1) % nyC] + \
                        gameState[(x) % nxC, (y+1) % nyC] + \
                        gameState[(x+1) % nxC, (y+1) % nyC]

              if gameState[x,y] == 0 and n_neigh == 3:
                  newGameState[x,y] = 1

              elif gameState[x,y] == 1 and (n_neigh < 2 or n_neigh > 3):
                  newGameState[x,y] = 0

            poly = [((x) * dimCW, y *  dimCh),
                    ((x+1) * dimCW, y *dimCh),
                    ((x+1) * dimCW, (y+1) *dimCh),
                    ((x) * dimCW, (y+1)* dimCh)]
            if newGameState[x,y] == 0:
                pygame.draw.polygon(screen,(128,128,128),poly, 1)
            else:
                pygame.draw.polygon(screen,(255,255,255),poly,0)

    gameState = np.copy(newGameState)
    pygame.display.flip()

