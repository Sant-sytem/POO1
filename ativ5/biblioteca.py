class Biblioteca:
    def __init__(self):
        self.itens_emprestados = []

    def emprestar_midia(self, midia):
        if midia.verificar_disponibilidade():
            self.itens_emprestados.append(midia)
            midia.disponivel = False 
            print(f"Midia '{midia.titulo}' emprestado.")
        else:
            print(f"Midia '{midia.titulo}' nao esta disponivel para empréstimo.")

    def devolver_midia(self, midia):
        if midia in self.itens_emprestados:
            self.itens_emprestados.remove(midia)
            midia.disponivel = True  
            print(f"Midia '{midia.titulo}' devolvida.")
        else:
            print(f"Midia '{midia.titulo}' nao foi emprestado.")

    def listar_itens_emprestados(self):
        if not self.itens_emprestados:
            print("Nao ha midias emprestadas.")
        else:
            print("Itens emprestados:")
            for midia in self.itens_emprestados:
                print(midia.obter_info())
