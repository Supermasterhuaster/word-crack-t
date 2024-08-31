from typing import List, Union

from src.controller.controller_matching_words import ControllerMatchingWords


class Dictionary:
    """
    Contains a dictionary of words for analysis
    """

    def __init__(self, word_list: List[str]):
        self.words = word_list

    def filter_words(self, fixed_letters: List[str], fixed_positions: List[int], floating_letters: List[str],
                     floating_positions: List[int], excluded_words: List[str]) -> Union[str, None]:
        """
        Returns the first filtered word from the dictionary or None if the desired word could not be found
        :param fixed_letters:
        :param fixed_positions:
        :param floating_letters:
        :param floating_positions:
        :param excluded_words:
        :return:
        """
        filtered_words = ControllerMatchingWords.match(self.words, fixed_letters, fixed_positions, floating_letters,
                                                       floating_positions, excluded_words)
        if len(filtered_words) == 0:
            return None

        return filtered_words[0]
