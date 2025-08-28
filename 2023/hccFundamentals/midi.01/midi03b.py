#!/usr/bin/env python

import sys, os

import pygame as pg
import pygame.midi
from time import *

def print_device_info():
  pygame.midi.init()
  print_device_info()
  pygame.midi.quit()


def print_device_info():
  for i in range(pygame.midi.get_count()):
    r = pygame.midi.get_device_info(i)
    (interf, name, input, output, opened) = r

    in_out = ""

    if input:  in_out = "(input)"
    if output: in_out = "(output)"

    print(
      "%2i: interface :%s:, name :%s:, opened :%s:  %s"
      % (i, interf, name, opened, in_out)
    )


pg.init()
pygame.midi.init()
print_device_info()

input_id = pygame.midi.get_default_input_id()
print("input_id:", input_id)

while True:
  i = pygame.midi.Input(2)
  print(i)

  sleep(.3)

print("beyond end of time")

#pg.display.set_mode((1, 1))

