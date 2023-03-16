class Navegador:
    def __init__(self, paginaInicial):
        self.paginaActual = paginaInicial
        self.listaDePaginas = []
    
    def navegar(self):
        url = input("Ingerese la pagina a la que quiera navegar: ")
        self.listaDePaginas.append(self.paginaActual)
        self.paginaActual = url
    def regresar(self):
        ultimaPagina = self.listaDePaginas.pop()
        self.paginaActual = ultimaPagina
navegador = Navegador("wwww.google.com")

while True:
    operaciones = """
        Ingrese N para navegar a una nueva pagina
        Ingrese H para conocer el historial completo
        Ingrese B para regresar a la pagina anterior
    """
    inputUsuario = input(operaciones)
    if inputUsuario == "N":
        navegador.navegar()
    elif inputUsuario == "H":
        print("Pagina actual: ", navegador.paginaActual)
        print("Historial anterior: ", navegador.listaDePaginas)
    elif inputUsuario == "B":
        navegador.regresar()
        print("Pagina actual: ", navegador.paginaActual)
    