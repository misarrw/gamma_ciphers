from gamma import RepeatKeyGamma, OpenTextGamma, CipherTextGamma
from sub_func import check_keyboard, text_into_numbers
from vigenere import vigenere


def main():
    while True:
        print('\nEnter the text which you want to encrypt/decrypt:')
        pre_text = input().lower()
        text = check_keyboard(pre_text)

        while True:
            if text == None:
                pre_text = input().lower()
                text = check_keyboard(pre_text)
                continue
            else:
                break

        text_numbers = text_into_numbers(text)

        if text == 'stop':
            break
        
        print('\nEnter the key (It must consist of letters, neither numbers nor other symbols)')
        pre_key = input().lower()
        key = check_keyboard(pre_key)
        while True:
            if key == None:
                pre_key = input().lower()
                key = check_keyboard(pre_key)
                continue
            else:
                break

        check_keyboard(key)
        if len(key) >= len(text):
            print('\nYour key is too long, you are not allowed to choose any type of gamma generation :(')
            if len(key) > len(text):
                key = key[:len(text)]
            type = '0'
        else:
            print('\nChoose the type of the gamma:\n1. "Repeat key" gamma\n2. "Open text" gamma\n3. "Ciphertext" gamma\n(Enter a number between 1, 2 and 3)')
            type = input()

        print('\nChoose an operation:\n1. Encryption\n2. Decryption\n(Enter only 1 or 2)')
        operation = input()
        if operation == '1':
            if type == '1':
                key_numbers = text_into_numbers(key)
                pre_gamma = RepeatKeyGamma()
                gamma = pre_gamma.repeat_key(key_numbers, text)
            elif type == '2':
                pre_gamma = OpenTextGamma()
                gamma = pre_gamma.open_text(key, text_numbers, 1)

            elif type == '3':
                pre_gamma = CipherTextGamma()
                gamma = pre_gamma.cipher_text(key, text_numbers, 1)

            elif type == '0':
                key_numbers = text_into_numbers(key)

            else:
                print('\nThis operation is not available')

            if type != '0':
                ciphertext = vigenere(gamma, text_numbers, 1)
            else:
                ciphertext = vigenere(key_numbers, text_numbers, 1)
            print(f'\nCiphertext: {ciphertext}')

        elif operation == '2':
            if type == '1':
                key_numbers = text_into_numbers(key)
                pre_gamma = RepeatKeyGamma()
                gamma = pre_gamma.repeat_key(key_numbers, text)
            
            elif type == '2':
                pre_gamma = OpenTextGamma()
                gamma = pre_gamma.open_text(key, text_numbers, 2)

            elif type == '3':
                pre_gamma = CipherTextGamma()
                gamma = pre_gamma.cipher_text(key, text_numbers, 2)

            elif type == '0':
                key_numbers = text_into_numbers(key)

            else:
                print('\nThis operation is not available')

            if type != '0':
                text = vigenere(gamma, text_numbers, 2)
            else:
                text = vigenere(key_numbers, text_numbers, 2)
            print(f'\nText: {text}')

        else:
            print('\nThis operation is not available')


if __name__ == '__main__':
    main()