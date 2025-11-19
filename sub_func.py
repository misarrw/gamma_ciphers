from constants import ALPHABET, SYMBOLS
from gamma import RepeatKeyGamma, OpenTextGamma, CipherTextGamma


def check_keyboard(text):
    for i in text.lower():
        if i not in ALPHABET and i not in SYMBOLS:
            print('\nPerhaps, you are using the wrong keyboard. Change the language and try again')
            return None
    return text
        

def text_into_numbers(text):
    numbers = []
    for symbol in text.lower():
        numbers.append(ALPHABET.index(symbol))
    return numbers


