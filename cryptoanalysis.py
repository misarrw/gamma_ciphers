from constants import ALPHABET
from sub_func import text_into_numbers


def cryptoanalysis(text: str, ciphertext: str) -> str:
    text_numbers = text_into_numbers(text)
    ciphertext_numbers = text_into_numbers(ciphertext)
    gamma_numbers = []
    for index in range(len(text)):
        gamma_numbers.append((ciphertext_numbers[index] - text_numbers[index]) % len(ALPHABET))
    gamma = ''
    for el in gamma_numbers:
        gamma += str(ALPHABET[el])
    return gamma.upper()


text = input()
ciphertext = input()
print(cryptoanalysis(text, ciphertext))
