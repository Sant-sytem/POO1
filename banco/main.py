from pessoa import Pessoa
from fotografia import Fotografia

def main():
    fotografo = Pessoa("João Fotógrafo", "123.456.789-00", "Rua A, 123", "(86) 99999-9999")
    proprietario = Pessoa("Maria Proprietária", "987.654.321-00", "Rua B, 456", "(86) 98888-8888")
    
    caminho_imagem = "./imagem.jpg"
    
    try:
        foto1 = Fotografia(caminho_imagem, fotografo, "2024-11-21", proprietario)
    except FileNotFoundError:
        print(f"Erro: O arquivo de imagem '{caminho_imagem}' não foi encontrado.")
        return
    except Exception as e:
        print(f"Erro ao criar a fotografia: {e}")
        return

    foto1.mostrar_fotografia()
    propriedades = foto1.propriedades_fotografia()
    print("\nPropriedades da Fotografia:")
    for chave, valor in propriedades.items():
        print(f"{chave}: {valor}")

if __name__ == "__main__":
    main()
