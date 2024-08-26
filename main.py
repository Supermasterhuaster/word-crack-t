# /bin/python3
import sys

from src.builder.builder_dictionary import BuilderDictionary
from src.controller.controller_dictionary_loader import ControllerDictionaryLoader
from src.controller.format.controller_word_with_positions import ControllerWordWithPositions
from src.entities.dictionary import Dictionary


def main():
    try:
        STARTING_WORD = 'парка'  # statistically, this is the most convenient word to start a search
        dictionary_loader = ControllerDictionaryLoader()
        builder_dictionary = BuilderDictionary(dictionary_loader)
        dictionary: Dictionary = builder_dictionary.build()
        attempts = 6
        free_letters = []
        fixed_letters = []
        fixed_positions = []
        free_positions = []
        excluded_words = []

        for attempt in range(attempts):
            print("")
            if not dictionary.words:
                print("Программа не может больше предложить вариантов. Проверьте правильность вводимых данных")
                break

            if attempt == attempts - 1:
                print("Попытки закончились. Программа не смогла отгадать слово.")

            if len(excluded_words) == 0:
                # if there were no previous attempts, we output a random word
                guess = STARTING_WORD
            else:
                guess = dictionary.filter_words(free_letters, fixed_letters, fixed_positions, free_positions,
                                                excluded_words)

            if guess is None:
                print("Программа не смогла подобрать слово по фильтру. Выход...")
                break

            formatted_guess = ControllerWordWithPositions.format(guess)
            print(f"Попытка {attempt + 1}/{attempts}: {guess}")

            # Enter the numbers of letters that are in the word, but not in their place
            incorrect_input = input(
                f"Введите номера букв через пробел, которые есть в слове, \nно не на своем месте: {formatted_guess}: ")

            indices = list(map(int, incorrect_input.split()))
            free_letters = [guess[i - 1] for i in indices]
            free_positions = indices

            positions = input(f"Введите номера букв через пробел, \nкоторые стоят на своем месте: {formatted_guess}: ")
            indices = list(map(int, positions.split()))
            fixed_letters = [guess[i - 1] for i in indices]
            fixed_positions = indices

            excluded_words.append(guess)

    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем. Выход...")
        sys.exit(0)


if __name__ == '__main__':
    main()
