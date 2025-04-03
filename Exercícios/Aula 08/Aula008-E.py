'''from playsound import playsound
audio = input('Deseja escutar uma música ? (Sim ou Não): ')
if audio.lower() == 'sim':
    playsound("D:\\Windows\\Músicas\\Cover\\Franklin.mp3")
else:
    print("OK, não tocarei a música.")'''

import pygame
pygame.init()
pygame.mixer.music.load("D:\\Windows\\Músicas\\Cover\\Franklin.mp3")
pygame.mixer.music.play()
pygame.event.wait()
