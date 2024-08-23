from typing import List


class ControllerFilterByPositions:
    """
    Contains a filter for the dictionary
    """

    @staticmethod
    def filter(word_list: List[str], letters: List[str], positions: List[int], excluded_words: List[str]) -> List[str]:
        """
        Filters words based on the positions of letters in the word and taking into account previously processed words
        :param word_list:
        :param letters:
        :param positions:
        :param excluded_words:
        :return:
        """

        filtered_list = word_list
        if len(excluded_words) != 0:
            # Removing the words that are in excluded_words
            filtered_list = [word for word in word_list if word not in excluded_words]
        if len(positions) == 0 or len(letters) == 0:
            return filtered_list

        # Filtering words by letter positions
        result = []
        for word in filtered_list:
            if len(word) < max(positions):
                continue
            match = True
            for letter, pos in zip(letters, positions):
                if word[pos - 1] != letter:
                    match = False
                    break
            if match:
                result.append(word)

        return result
