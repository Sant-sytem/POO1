from ebook import Ebook 
from audiobook import AudioBook
from revistadigital import RevistaDigital
from biblioteca import Biblioteca

ebook1 = Ebook(" My hero", "Jojo", "PDF", True)
audiobook1 = AudioBook("Menos e Mais", "Juselino", 120, True)
revista1 = RevistaDigital("Revelacao geografica", "Jesus", 10, 2023, True)

biblioteca = Biblioteca()

print("\n------- Emprestimos -------\n")
biblioteca.emprestar_midia(ebook1)
biblioteca.emprestar_midia(audiobook1)
biblioteca.emprestar_midia(revista1)

print("\n--------Emprestados------")
biblioteca.listar_itens_emprestados()

print("\n-----Devolucao de Midia------")
biblioteca.devolver_midia(ebook1)

print("\n------ Apos Devolucao--------")
biblioteca.listar_itens_emprestados()

print("\n-----------")
