# /bin/python3
import random
import sys

from src.builder.builder_dictionary import BuilderDictionary
from src.controller.controller_dictionary_loader import ControllerDictionaryLoader
from src.controller.format.controller_word_with_positions import ControllerWordWithPositions
from src.entities.dictionary import Dictionary


def main():
    try:
        dictionary_loader = ControllerDictionaryLoader()
        builder_dictionary = BuilderDictionary(dictionary_loader)
        dictionary = builder_dictionary.build()

        word_list = ["фильм", "фикус", "книга", "столб", "монет", "крыша", "молот", "окроп", "шахта", "кошка"]
        dictionary = Dictionary(word_list)  # for testing
        attempts = 6
        free_letters = []
        fixed_letters = []
        positions = []
        excluded_words = []

        for attempt in range(attempts):
            if not dictionary.words:
                print("Программа не может больше предложить вариантов. Проверьте правильность вводимых данных")
                break

            if attempt == attempts - 1:
                print("Попытки закончились. Программа не смогла отгадать слово.")

            if len(excluded_words) == 0:
                # if there were no previous attempts, we output a random word
                guess = random.choice(dictionary.words)
            else:
                guess = dictionary.filter_words(free_letters, fixed_letters, positions, excluded_words)

            if guess is None:
                print("Программа не смогла подобрать слово по фильтру. Выход...")
                break

            formatted_guess = ControllerWordWithPositions.format(guess)
            print(f"Попытка {attempt + 1}/{attempts}: {guess}")

            # Enter the numbers of letters that are in the word, but not in their place
            incorrect_input = input(
                f"Введите номера букв, которые есть в слове, но не на своем месте: {formatted_guess}: ")
            indices = list(map(int, incorrect_input.split()))
            free_letters = [guess[i - 1] for i in indices]

            positions = input(f"Введите номера букв, которые стоят на своем месте: {formatted_guess}: ")
            indices = list(map(int, positions.split()))
            fixed_letters = [guess[i - 1] for i in indices]
            excluded_words.append(guess)
            positions = indices

    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем. Выход...")
        sys.exit(0)


if __name__ == '__main__':
    main()
