from src.entities.dictionary import Dictionary
from src.controller.controller_dictionary_loader import ControllerDictionaryLoader


class BuilderDictionary:
    """
    Builds a dictionary model
    """

    def __init__(self, dictionary_loader: ControllerDictionaryLoader):
        self.dictionary_loader = dictionary_loader

    def build(self) -> Dictionary:
        """
        Creates a dictionary model using a loader
        :return:
        """
        word_list = self.dictionary_loader.load()
        return Dictionary(word_list)
