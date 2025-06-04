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
        sleep(0.2)
        gpio8.set_value(0)
        sleep(0.2)

def dash():
        gpio8.set_value(1)
        sleep(0.6)
        gpio8.set_value(0)
        sleep(0.2)

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        morse_code += CODE.get(char, '') + ' '
    return morse_code.strip()

def morse_to_text(morse):
    text = ''
    morse_words = morse.split('   ')  # Split by triple spaces for words
    for word in morse_words:
        morse_chars = word.split(' ')
        for char in morse_chars:
            for key, value in CODE.items():
                if value == char:
                    text += key
                    break
        text += ' '
    return text.strip()

gpio8 = gpiod.find_line("GPIO14")
gpio8.request(consumer="BeagleY-AI", type=gpiod.LINE_REQ_DIR_OUT, default_val=0)

try:
    while True:
        inp = input('What shall we send...?\n')
        for letter in inp:
            for symbol in CODE[letter.upper()]:
                if symbol == '-':
                    dash()
                elif symbol == '.':
                    dot()
                else:
                    sleep(1)
        sleep(1)

        text = inp
        morse = text_to_morse(text)
        print(f"Text: {text}")
        print(f"Morse: {morse}")
        translated_text = morse_to_text(morse)
        print(f"Translated: {translated_text}")
except KeyboardInterrupt:
    gpio8.set_value(0)
    pass
    print("Hey...done for now?\n")
