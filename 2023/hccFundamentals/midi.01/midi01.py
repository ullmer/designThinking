#!/usr/bin/env python

import sys, os

import pygame as pg
import pygame.midi

from typing import Any, Dict, List, Optional, Set, Tuple, Union

def print_device_info():
    pygame.midi.init()
    _print_device_info()
    pygame.midi.quit()

def _print_device_info():
    for i in range(pygame.midi.get_count()):
        r = pygame.midi.get_device_info(i)
        (interf, name, input, output, opened) = r

        in_out = ""
        if input:
            in_out = "(input)"
        if output:
            in_out = "(output)"

        print(
            "%2i: interface :%s:, name :%s:, opened :%s:  %s"
            % (i, interf, name, opened, in_out)
        )


def input_main(device_id=None):
    pg.init()

    pygame.midi.init()

    _print_device_info()

    if device_id is None:
        input_id = pygame.midi.get_default_input_id()
    else:
        input_id = device_id

    print(f"using input_id :{input_id}:")
    i = pygame.midi.Input(input_id)

    pg.display.set_mode((1, 1))

    going = True
    while going:
        events = pygame.event.get()
        for e in events:
            if e.type in [pg.QUIT]:
                going = False
            if e.type in [pg.KEYDOWN]:
                going = False
            if e.type in [pygame.midi.MIDIIN]:
                print(e)

        if i.poll():
            midi_events = i.read(10)
            # convert them into pygame events.
            midi_evs = pygame.midi.midis2events(midi_events, i.device_id)

            for m_e in midi_evs:
                pygame.event.post(m_e)

    #del i
    #pygame.midi.quit()


    pg.init()
    pygame.midi.init()

    _print_device_info()

    if device_id is None:
        port = pygame.midi.get_default_output_id()
    else:
        port = device_id

    print(f"using output_id :{port}:")

    midi_out = pygame.midi.Output(port, 0)
    try:

        background = pg.Surface(screen.get_size())
        background.fill(BACKGROUNDCOLOR)
        dirty_rects = []
        keyboard.draw(screen, background, dirty_rects)
        pg.display.update(dirty_rects)

        regions = pg.Surface(screen.get_size())  # initial color (0,0,0)
        keyboard.map_regions(regions)

        pg.event.set_blocked(pg.MOUSEMOTION)
        mouse_note = 0
        on_notes = set()
        while True:
            e = pg.event.wait()
            if e.type == pg.MOUSEBUTTONDOWN:
                mouse_note, velocity, __, __ = regions.get_at(e.pos)
                if mouse_note and mouse_note not in on_notes:
                    keyboard.key_down(mouse_note)
                    midi_out.note_on(mouse_note, velocity)
                    on_notes.add(mouse_note)
                else:
                    mouse_note = 0
            elif e.type == pg.MOUSEBUTTONUP:
                if mouse_note:
                    midi_out.note_off(mouse_note)
                    keyboard.key_up(mouse_note)
                    on_notes.remove(mouse_note)
                    mouse_note = 0
            elif e.type == pg.QUIT:
                break
            elif e.type == pg.KEYDOWN:
                if e.key == pg.K_ESCAPE:
                    break
                try:
                    note, velocity = key_mapping[e.key]
                except KeyError:
                    pass
                else:
                    if note not in on_notes:
                        keyboard.key_down(note)
                        midi_out.note_on(note, velocity)
                        on_notes.add(note)
            elif e.type == pg.KEYUP:
                try:
                    note, __ = key_mapping[e.key]
                except KeyError:
                    pass
                else:
                    if note in on_notes and note != mouse_note:
                        keyboard.key_up(note)
                        midi_out.note_off(note, 0)
                        on_notes.remove(note)

            dirty_rects = []
            keyboard.draw(screen, background, dirty_rects)
            pg.display.update(dirty_rects)
    finally:
        del midi_out
        pygame.midi.quit()


def main(mode="output", device_id=None):
    """Run a Midi example

    Arguments:
    mode - if 'output' run a midi keyboard output example
              'input' run a midi event logger input example
              'list' list available midi devices
           (default 'output')
    device_id - midi device number; if None then use the default midi input or
                output device for the system

    """

    if mode == "input":
        input_main(device_id)
    elif mode == "output":
        output_main(device_id)
    elif mode == "list":
        print_device_info()
    else:
        raise ValueError(f"Unknown mode option '{mode}'")


if __name__ == "__main__":
    device_id: Optional[int] = None
    try:
        device_id = int(sys.argv[-1])
    except ValueError:
        device_id = None

    if "--input" in sys.argv or "-i" in sys.argv:
        input_main(device_id)

    elif "--output" in sys.argv or "-o" in sys.argv:
        output_main(device_id)
    elif "--list" in sys.argv or "-l" in sys.argv:
        print_device_info()
    else:
        usage()

    pg.quit()
