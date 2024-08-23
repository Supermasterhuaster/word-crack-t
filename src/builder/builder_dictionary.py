from src.entities.dictionary import Dictionary
from src.controller.controller_dictionary_loader import ControllerDictionaryLoader


class BuilderDictionary:

    def __init__(self, dictionary_loader: ControllerDictionaryLoader):
        self.dictionary_loader = dictionary_loader

    def build(self) -> Dictionary:
        word_list = self.dictionary_loader.load()
        return Dictionary(word_list)
