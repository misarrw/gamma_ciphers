from constants import ALPHABET


class StandartGamma:
    def __init__(self):
        self.len_alphabet = len(ALPHABET)
    

class RepeatKeyGamma(StandartGamma):

    def repeat_key(self, key_numbers: list, text: str) -> list:
        gamma = []
        index = 0
        len_key = len(key_numbers) - 1
        while len(gamma) < len(text):
            if index == len_key:
                index = 0
            else: 
                gamma.append(key_numbers[index])
                index += 1
        return gamma
    

class OpenTextGamma(StandartGamma):

    def open_text(self, key: str, text_numbers: list, option: int) -> list:
        gamma = []
        for symbol in key.lower():
            gamma.append(ALPHABET.index(symbol))
        index = 0
        if option == 1:
            len_text = len(text_numbers)
            while len(gamma) < len_text:
                gamma.append(text_numbers[index])
                index += 1
        else:
            len_text_numbers = len(text_numbers)
            while len(gamma) < len_text_numbers:
                gamma.append((text_numbers[index] - gamma[index]) % self.len_alphabet)
                index += 1
        return gamma


class CipherTextGamma(StandartGamma):
    
    def cipher_text(self, key: str, text_numbers: list, option: int) -> list:
        gamma = []
        for symbol in key.lower():
            gamma.append(ALPHABET.index(symbol))
        index = 0
        if option == 1:
            len_text_numbers = len(text_numbers)
            while len(gamma) < len_text_numbers:
                gamma.append((text_numbers[index] + gamma[index]) % self.len_alphabet)
                index += 1
        else:
            len_text = len(text_numbers)
            while len(gamma) < len_text:
                gamma.append(text_numbers[index])
                index += 1
        return gamma
    