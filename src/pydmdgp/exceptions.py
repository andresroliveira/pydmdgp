"""
Este módulo define as exceções customizadas para o pacote pydmdgp.

Ter exceções específicas para a biblioteca permite que os usuários capturem
erros de forma granular, sem precisar capturar a `Exception` genérica.
"""


class DMDGPError(Exception):
    """
    Classe base para todas as exceções lançadas pela biblioteca pydmdgp.
    
    Capturar esta exceção permite tratar qualquer erro gerado pelo nosso pacote.
    ex:
    try:
        ...
    except DMDGPError as e:
        print(f"Ocorreu um erro na biblioteca pydmdgp: {e}")
    """
    pass


class NoSolutionError(DMDGPError):
    """
    Exceção lançada quando o algoritmo Branch-and-Prune não consegue encontrar
    uma solução que satisfaça todas as restrições de distância.

    Isso geralmente ocorre quando todo o espaço de busca é explorado sem que se
    encontre uma configuração com erro abaixo da tolerância (delta) especificada.
    """

    def __init__(
        self,
        message="O solver explorou a árvore de busca e não encontrou uma solução válida."
    ):
        self.message = message
        super().__init__(self.message)


class NoIntersectionError(DMDGPError):
    """
    Exceção lançada durante um cálculo geométrico quando três esferas não
    possuem um ponto de interseção em comum.

    É tipicamente usada para evitar o cálculo da raiz quadrada de um número negativo
    na função de interseção de esferas.
    """

    def __init__(
            self,
            message="Falha no cálculo geométrico: as esferas não se interceptam."
    ):
        self.message = message
        super().__init__(self.message)


class DiscretizationError(DMDGPError):
    """
    Exceção lançada quando não é possível encontrar uma ordem de discretização
    válida para o grafo fornecido.
    """

    def __init__(
        self,
        message="Não foi possível encontrar uma ordem de discretização para o grafo."
    ):
        self.message = message
        super().__init__(self.message)
