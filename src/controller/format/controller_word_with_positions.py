

class ControllerWordWithPositions:

    @staticmethod
    def format(word: str) -> str:
        return ' '.join([f"{letter}[{i + 1}]" for i, letter in enumerate(word)])