from typing import List


class ControllerFilterByLetters:
    """
    Contains a filter for the dictionary
    """

    @staticmethod
    def filter(word_list: List[str], letters: List[str], excluded_words: List[str]) -> List[str]:
        """
        Filters words from the list that do not contain the specified letters
        :param word_list:
        :param letters:
        :param excluded_words:
        :return:
        """
        # Removing the excluded words from the initial list
        filtered_words = [word for word in word_list if word not in excluded_words]

        # Filter the remaining words by the presence of all the specified letters
        filtered_words = [word for word in filtered_words if all(letter in word for letter in letters)]

        return filtered_words
