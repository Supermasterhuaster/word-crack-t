import os
import bz2
import pickle
from typing import List


class ControllerDictionaryLoader:
    """
    Downloads the contents of the dictionary from disk
    """

    STORAGE_NAME = 'storage'
    FILE_NAME = 'dictionary.pkl.bz2'

    def load(self) -> List[str]:
        """
        Reads a PSD file from a disk that contains words for analysis
        :return:
        """

        file_path = os.path.join('.', self.STORAGE_NAME, self.FILE_NAME)

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл словаря не найден: {file_path}")
        with bz2.BZ2File(file_path, 'rb') as f:
            data = pickle.load(f)

        return data
