#!/usr/bin/env python

import sys, os, yaml
import pygame as pg
import pygame.midi

f = open('yaml/numark-dj2go-midi.yaml', 'rt')
y = yaml.safe_load(f)

pygame.midi.init()
i = pygame.midi.Input(1)
e = i.read(100); print(e)

