from typing import List

from src.controller.word_filter.interface_word_filter_visitor import InterfaceWordFilterVisitor


class Dictionary:

    def __init__(self, word_list: List[str]):
        self.words = word_list

    def filter_words(self, visitors: List[InterfaceWordFilterVisitor]) -> List[str]:
        filtered_words = []
        for word in self.words:
            if all(visitor.visit(word) for visitor in visitors):
                filtered_words.append(word)
        return filtered_words
