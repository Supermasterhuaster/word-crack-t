import random
import sys

from src.builder.builder_dictionary import BuilderDictionary
from src.controller.controller_dictionary_loader import ControllerDictionaryLoader
from src.controller.format.controller_word_with_positions import ControllerWordWithPositions
from src.controller.word_filter.controller_correct_position_filter import ControllerCorrectPositionFilter
from src.controller.word_filter.controller_exclude_letters_filter import ControllerExcludeLettersFilter
from src.controller.word_filter.controller_incorrect_position_filter import ControllerIncorrectPositionFilter
from src.entities.dictionary import Dictionary


def main():
    try:
        dictionary_loader = ControllerDictionaryLoader()
        builder_dictionary = BuilderDictionary(dictionary_loader)
        dictionary = builder_dictionary.build()

        word_list = ["фильм", "фикус", "книга", "столб", "монет", "крыша", "молот", "окроп", "шахта", "кошка"]
        dictionary = Dictionary(word_list)  # for testing
        attempts = 6
        correct_positions = []
        incorrect_positions = []
        correct_letters = [''] * 5
        excluded_letters = set()

        for attempt in range(attempts):
            if not dictionary.words:
                print("Программа не может больше предложить вариантов. Проверьте правильность вводимых данных.")
                break

            guess = random.choice(dictionary.words)
            formatted_guess = ControllerWordWithPositions.format(guess)
            print(f"Попытка {attempt + 1}: {guess}")

            # Ввод номеров букв, которые есть в слове, но не на своем месте
            incorrect_input = input(
                f"Введите номера букв, которые есть в слове, но не на своем месте: {formatted_guess}: ")
            incorrect_positions = [int(i) - 1 for i in incorrect_input.split() if i.isdigit()]

            # Ввод номеров букв, которые стоят на своем месте
            correct_input = input(f"Введите номера букв, которые стоят на своем месте: {formatted_guess}: ")
            correct_positions = [int(i) - 1 for i in correct_input.split() if i.isdigit()]

            if not incorrect_input and not correct_input:
                excluded_letters.update(set(guess))
            else:
                for pos in correct_positions:
                    correct_letters[pos] = guess[pos]

            # Фильтрация списка возможных слов
            possible_words = dictionary.filter_words(correct_positions, incorrect_positions,
                                                     correct_letters, excluded_letters)

            if len(possible_words) == 1:
                print(f"Слово отгадано: {possible_words[0]}")
                break
            elif attempt == attempts - 1:
                print("Попытки закончились. Программа не смогла отгадать слово.")

        # for attempt in range(attempts):
        #     if not dictionary.words:
        #         print("Программа не может больше предложить вариантов. Проверьте правильность вводимых данных.")
        #         break
        #
        #     guess = random.choice(dictionary.words)
        #     formatted_guess = ControllerWordWithPositions.format(guess)
        #     print(f"Попытка {attempt + 1}: {guess}")
        #
        #     # Input the numbers of the letters that are in the word but not in their place
        #     incorrect_input = input(
        #         f"Введите номера букв, которые есть в слове, но не на своем месте: {formatted_guess}: ")
        #     incorrect_positions = [int(i) - 1 for i in incorrect_input.split() if i.isdigit()]
        #
        #     # Input the numbers of the letters that are in the correct position
        #     correct_input = input(f"Введите номера букв, которые стоят на своем месте: {formatted_guess}: ")
        #     correct_positions = [int(i) - 1 for i in correct_input.split() if i.isdigit()]
        #
        #     if not incorrect_input and not correct_input:
        #         excluded_letters.update(set(guess))
        #     else:
        #         for pos in correct_positions:
        #             correct_letters[pos] = guess[pos]
        #
        #     # Create filters based on the input data
        #     visitors = [
        #         ControllerCorrectPositionFilter(correct_positions, correct_letters),
        #         ControllerIncorrectPositionFilter(incorrect_positions, correct_letters),
        #         ControllerExcludeLettersFilter(excluded_letters)
        #     ]
        #
        #     # Filter the list of possible words
        #     dictionary.words = dictionary.filter_words(visitors)
        #
        #     if len(dictionary.words) == 1:
        #         print(f"Слово отгадано: {dictionary.words[0]}")
        #         break
        #     elif attempt == attempts - 1:
        #         print("Попытки закончились. Программа не смогла отгадать слово.")

    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем. Выход...")
        sys.exit(0)


if __name__ == '__main__':
    main()
