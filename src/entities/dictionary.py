from typing import List

from src.controller.word_filter.interface_word_filter_visitor import InterfaceWordFilterVisitor


class Dictionary:

    def __init__(self, word_list: List[str]):
        self.words = word_list

    def filter_words(self, correct_positions, incorrect_positions, correct_letters, excluded_letters) -> List[str]:
        filtered_list = []
        for word in self.words:
            if any(letter in word for letter in excluded_letters):
                continue
            match = True
            for i, letter in enumerate(word):
                if i in correct_positions and word[i] != correct_letters[i]:
                    match = False
                    break
                if i in incorrect_positions and word[i] == correct_letters[i]:
                    match = False
                    break
            for pos in incorrect_positions:
                if correct_letters[pos] not in word:
                    match = False
                    break
            if match:
                filtered_list.append(word)
        return filtered_list
