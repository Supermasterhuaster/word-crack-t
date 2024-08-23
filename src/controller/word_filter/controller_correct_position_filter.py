from typing import List

from src.controller.word_filter.interface_word_filter_visitor import InterfaceWordFilterVisitor


class ControllerCorrectPositionFilter(InterfaceWordFilterVisitor):
    def __init__(self, correct_positions: List[int], correct_letters: List[str]):
        self.correct_positions = correct_positions
        self.correct_letters = correct_letters

    def visit(self, word: str) -> bool:
        for i in self.correct_positions:
            if word[i] != self.correct_letters[i]:
                return False
        return True