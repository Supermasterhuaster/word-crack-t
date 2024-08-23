

class ControllerWordWithPositions:
    """
    Contains a counter for the positions of letters in a word
    """

    @staticmethod
    def format(word: str) -> str:
        """
        Returns a string with numbered letters
        :param word:
        :return:
        """
        return ' '.join([f"{letter}[{i + 1}]" for i, letter in enumerate(word)])