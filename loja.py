# Programação Orientada a Objetos
# AC03 ADS-EaD - Implementação de classes, herança, polimorfismo e lançamento de exceções.
#
# Email Impacta: william.pereira@aluno.faculdadeimpacta.com.br


class Produto:
    """
    Classe Produto: deve representar os elementos básicos de um produto.
    """

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @property
    def nome(self):
        return self.__nome

    @property
    def preco(self):
        return self.__preco

    @nome.setter
    def nome(self, novo_nome):
        if len(novo_nome) == 0:
            raise ValueError("Nome vazio. Preencha um nome!")
        self.__nome = novo_nome

    @preco.setter
    def preco(self, novo_preco):
        if isinstance(novo_preco, int) or isinstance(novo_preco, float):
            if novo_preco >= 0:
                self.__preco = novo_preco
            else:
                raise ValueError("Preço negativo. Insira um preço positivo!")
        else:
            raise TypeError("Digite um preço de tipo int ou float!")

    def calcular_preco_com_frete(self):
        self.preco + 15
        return self.__preco


class ProdutoFisico(Produto):
    """
    Classe ProdutoFisico: deve representar os elementos básicos de um produto físico.
    Esta classe herda da classe Produto.
    """

    def __init__(self, nome, preco, peso):
        super().__init__(nome, preco)
        self.peso = peso

    @property
    def peso(self):
        return self.__peso

    @peso.setter
    def peso(self, novo_peso):
        if not isinstance(novo_peso, int):
            raise TypeError("Peso deve ser um núnero inteiro!")
        if novo_peso <= 0:
            raise ValueError("Digite um peso maior que zero!")
        self.__peso = novo_peso

    def peso_em_kg(self):
        return self.__peso / 1000

    def calcular_preco_com_frete(self):
        return self.preco + (self.peso_em_kg() * 5)


class ProdutoEletronico(ProdutoFisico):
    """
    Classe ProdutoEletronico: deve representar os elementos básicos de um produto eletrônico.
    Esta classe herda da classe ProdutoFisico.
    """

    def __init__(self, nome, preco, peso, tensao, tempo_garantia):
        super().__init__(nome, preco, peso)
        self.tensao = tensao
        self.__tempo_garantia = tempo_garantia

    @property
    def tensao(self):
        return self.__tensao

    @property
    def tempo_garantia(self):
        return self.__tempo_garantia

    @tensao.setter
    def tensao(self, nova_tensao):
        if not isinstance(nova_tensao, int):
            raise TypeError("Tensão Precisa ser inteira")
        if nova_tensao != 0 and nova_tensao != 127 and nova_tensao != 220:
            raise ValueError("Escolha entre 0, 127 ou 220 volts!")
        self.__tensao = nova_tensao

    def calcular_preco_com_frete(self):
        return(super().calcular_preco_com_frete()*0.01) + super().calcular_preco_com_frete()


class Ebook(Produto):

    """
    Classe Ebook: deve representar os elementos básicos de um ebook (livro digital).
    Esta classe herda da classe Produto.
    """

    def __init__(self, nome, preco, autor, numero_paginas):
        super().__init__(nome, preco)
        self.__autor = autor
        self.numero_paginas = numero_paginas

    @property
    def nome_exibicao(self):
        return f'{self.nome} ({self.__autor})'

    @property
    def numero_paginas(self):
        return self.__numero_paginas

    @numero_paginas.setter
    def numero_paginas(self, valor):
        if valor <= 0:
            raise ValueError("O valor precisa ser maior que 0!")
        self.__numero_paginas = valor
