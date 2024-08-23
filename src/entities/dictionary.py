from typing import List, Union

from src.controller.word_filter.controller_filter_by_letters import ControllerFilterByLetters
from src.controller.word_filter.controller_filter_by_positions import ControllerFilterByPositions


class Dictionary:
    """
    Contains a dictionary of words for analysis
    """

    def __init__(self, word_list: List[str]):
        self.words = word_list

    def filter_words(self, free_letters: List[str], fixed_letters: List[str], positions: List[int],
                     excluded_words: List[str]) -> Union[str, None]:
        """
        Returns the first filtered word from the dictionary or None if the desired word could not be found
        :param free_letters:
        :param fixed_letters:
        :param positions:
        :param excluded_words:
        :return:
        """
        filtered_words = ControllerFilterByLetters.filter(self.words, free_letters, excluded_words)
        filtered_words = ControllerFilterByPositions.filter(filtered_words, fixed_letters, positions, excluded_words)
        if len(filtered_words) == 0:
            return None

        return filtered_words[0]
