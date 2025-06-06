#!/usr/bin/python3

# Testing Motors Again
# Dictionary from https://www.cl.cam.ac.uk/ and ideas

import gpiod
from time import sleep

CODE = {' ': ' ',
        "'": '.----.',
        '(': '-.--.-',
        ')': '-.--.-',
        ',': '--..--',
        '-': '-....-',
        '.': '.-.-.-',
        '/': '-..-.',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ':': '---...',
        ';': '-.-.-.',
        '?': '..--..',
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '_': '..--.-'}

def dot():
        gpio8.set_value(1)
        sleep(0.5)
        gpio8.set_value(0)
        sleep(0.5)

def dash():
        gpio8.set_value(1)
        sleep(1.5)
        gpio8.set_value(0)
        sleep(0.5)

gpio8 = gpiod.find_line("GPIO14")
gpio8.request(consumer="BeagleY-AI", type=gpiod.LINE_REQ_DIR_OUT, default_val=0)

try:
    while True:
        put = input('What shall we send...?')
        for letter in put:
            for symbol in CODE[letter.upper()]:
                if symbol == '-':
                    dash()
                elif symbol == '.':
                    dot()
                else:
                    sleep(0.5)
        sleep(0.5)
except KeyboardInterrupt:
    gpio8.set_value(0)
    pass
    print("\nHey...done for now?\n")
