# Objetivo: Criar uma aplicação que gerencia informações de uma biblioteca, incluindo livros, autores e usuários. O sistema
# deve permitir a adição de novos livros, consulta de livros por autor, e exportação/importação 
# de dados em diferentes formatos (texto, binário, JSON e CSV).

import json

class Livro:
    def __init__(self, titulo, autor, ano_publicacao, genero):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.genero = genero
    
    def __repr__(self):
        return f"Livro= '{self.titulo}, autor='{self.autor}', Ano de Publicação='{self.ano_publicacao}', Gênero='{self.genero}'"
class Biblioteca:

    def __init__(self):
        self.livros = []
    
    def adicionar_livro(self, livro):
        self.livros.append(livro)
    
    def listar_livro_por_autor(self, autor):
        return len([livro for livro in self.livros if livro.autor == autor])
    
    def contar_livro_por_genero(self, genero):
        return len([livro for livro in self.livros if livro.genero == genero])
    
    def exportar_para_json(self, caminho):
        with open(caminho, 'w') as arquivo:
            json.dump([livro.__dict__ for livro in self.livros], arquivo)
    
    def importar_do_json(self, caminho):
        with open(caminho, 'r') as arquivo:
            dados = json.load(arquivo)
            self.livros = [Livro(**livro) for livro in dados]
            

biblioteca = Biblioteca()

biblioteca.adicionar_livro(Livro('A Tempestade de Luz', 'Arkady Martine', 2024, 'Ficção Científica'))
biblioteca.adicionar_livro(Livro('As Filhas da Terra', 'Nnedi Okorafor', 2024, 'Ficção Científica'))
biblioteca.adicionar_livro(Livro('Ciborgue: O Último Refúgio', 'Marissa Meyer', 2024, 'Ação'))
biblioteca.adicionar_livro(Livro('A Sociedade de Preservação dos Kaiju', 'Bora ChungJohn Scalzi', 2024, 'Ação'))

print('Livros do autor Arkady Martine:', biblioteca.listar_livro_por_autor('Arkady Martine'))
print('Qtd de Livros de Ficção Científica', biblioteca.contar_livro_por_genero('Ficção Científica'))

biblioteca.exportar_para_json("biblioteca.json")
biblioteca.livros = []
biblioteca.importar_do_json("biblioteca.json")

print(f'Livros após importação:', biblioteca.livros)






