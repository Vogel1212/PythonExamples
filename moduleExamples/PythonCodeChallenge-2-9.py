# course challenge 21
# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
# Music: Kevin MacLeod ~ There It Is

import pygame
pygame.init()
pygame.mixer.music.load('PythonCodeChallenge-2-9.mp3')
pygame.mixer.music.play()
pygame.event.wait()