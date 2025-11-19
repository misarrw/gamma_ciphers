from constants import ALPHABET
from sub_func import text_into_numbers


def vigenere(gamma: list, text_numbers: list, operation: int) -> str:
    ciphertext_or_text_numbers = []
    len_text_numbers = len(text_numbers)
    len_alphabet = len(ALPHABET)
    for index in range(len_text_numbers):
        if operation == 1:
            ciphertext_or_text_numbers.append((gamma[index] + text_numbers[index]) % len_alphabet)
        else:
            ciphertext_or_text_numbers.append((text_numbers[index] - gamma[index]) % len_alphabet)
    ciphertext_or_text = ''
    for number in ciphertext_or_text_numbers:
        ciphertext_or_text += str(ALPHABET[number])
    return ciphertext_or_text.upper()