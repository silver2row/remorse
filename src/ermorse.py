#!/usr/bin/python3

# From Google and AI Search Labs

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ' ': ' '
}

def text_to_morse(text):
    morse_code = ''
    for char in text.upper():
        morse_code += morse_code_dict.get(char, '') + ' '
    return morse_code.strip()

def morse_to_text(morse):
    text = ''
    morse_words = morse.split('   ')  # Split by triple spaces for words
    for word in morse_words:
        morse_chars = word.split(' ')
        for char in morse_chars:
            for key, value in morse_code_dict.items():
                if value == char:
                    text += key
                    break
        text += ' '
    return text.strip()

# Example usage
text = "Hello World"
morse = text_to_morse(text)
print(f"Text: {text}")
print(f"Morse: {morse}")
translated_text = morse_to_text(morse)
print(f"Translated: {translated_text}")
