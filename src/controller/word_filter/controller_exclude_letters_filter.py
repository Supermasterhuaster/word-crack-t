from typing import Set
from src.controller.word_filter.interface_word_filter_visitor import InterfaceWordFilterVisitor


class ControllerExcludeLettersFilter(InterfaceWordFilterVisitor):
    def __init__(self, excluded_letters: Set[str]):
        self.excluded_letters = excluded_letters

    def visit(self, word: str) -> bool:
        return not any(letter in word for letter in self.excluded_letters)