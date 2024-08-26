from typing import List


class ControllerFilterByLetters:
    """
    Contains a filter for the dictionary
    """

    @staticmethod
    def filter(word_list: List[str], letters: List[str], positions: List[int], excluded_words: List[str]) -> List[str]:
        """
        Filters words from the list that do not contain the specified letters in the specified positions.
        :param word_list: List of words to filter
        :param letters: List of letters to look for in words
        :param positions: List of positions where these letters should NOT appear (1-based index)
        :param excluded_words: List of words to exclude from the results
        :return: List of filtered words
        """
        filtered_words = word_list

        if excluded_words:
            # Removing the excluded words from the initial list
            filtered_words = [word for word in word_list if word not in excluded_words]

        if letters and positions:
            # Ensure that the letters and positions lists have the same length
            if len(letters) != len(positions):
                raise ValueError("The length of letters and positions must be the same.")

            # Filter the remaining words by the presence of the specified letters not in the specified positions
            def is_valid_word(word):
                for letter, position in zip(letters, positions):
                    if letter in word and word[position - 1] == letter:
                        return False
                return True

            filtered_words = [word for word in filtered_words if is_valid_word(word)]

        return filtered_words