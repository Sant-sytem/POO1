import os
from skimage.io import imread
from matplotlib.pyplot import imshow, show

class Fotografia:
    _quantidade_fotos = 0

    __slots__ = ("_foto", "_fotografo", "_data", "_proprietario")

    def __init__(self, caminho_foto, fotografo, data, proprietario):
        if not os.path.exists(caminho_foto):
            raise FileNotFoundError(f"O arquivo de imagem '{caminho_foto}' não foi encontrado.")
        try:
            self._foto = imread(caminho_foto)
        except Exception as e:
            raise ValueError(f"Erro ao carregar a imagem: {e}")
        
        self._fotografo = fotografo
        self._data = data
        self._proprietario = proprietario

        Fotografia._quantidade_fotos += 1

    @property
    def fotografo(self):
        return self._fotografo

    @property
    def data(self):
        return self._data

    @property
    def proprietario(self):
        return self._proprietario

    def mostrar_fotografia(self):
        imshow(self._foto)
        show()

    def propriedades_fotografia(self):
        return {
            "Dimensões (pixels)": self._foto.shape,
            "Fotógrafo": self._fotografo.nome,
            "Data": self._data,
            "Proprietário": self._proprietario.nome
        }

    @classmethod
    def quantidade_fotos(cls):
        return cls._quantidade_fotos
