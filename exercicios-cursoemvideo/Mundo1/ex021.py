#  Desafio 021 - Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

print('Desafio 021 - Tocando um MP3')

pygame.init()

pygame.mixer.music.load('boom.wav')
pygame.mixer.music.play()
pygame.event.wait()
