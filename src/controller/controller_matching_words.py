from typing import List


class ControllerMatchingWords:

    @staticmethod
    def match(word_list: List[str], fixed_letters: List[str], fixed_positions: List[int], floating_letters: List[str],
              floating_positions: List[int], excluded_words: List[str]) -> List[str]:
        """
        Searches the dictionary for words according to the passed filter
        :param word_list:
        :param fixed_letters:
        :param fixed_positions:
        :param floating_letters:
        :param floating_positions:
        :param excluded_words:
        :return:
        """

        def word_matches_criteria(word: str) -> bool:
            # Checking excluded words
            if word in excluded_words:
                return False

            # Checking fixed_letters for fixed_positions
            for letter, position in zip(fixed_letters, fixed_positions):
                if word[position - 1] != letter:
                    return False

            # Checking floating_letters and floating_positions
            for letter in floating_letters:
                if letter not in word:
                    return False
            for letter, position in zip(floating_letters, floating_positions):
                if word[position - 1] == letter:
                    return False

            return True

        # Applying a filter
        filtered_words = [word for word in word_list if word_matches_criteria(word)]

        return filtered_words
