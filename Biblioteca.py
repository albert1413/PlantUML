class Llibre:
    def __init__(self, titol, any, categoria, autor, editorial):
        self.titol = titol
        self.any = any
        self.categoria = categoria
        self.autor = autor
        self.editorial = editorial

class Editorial:
    def __init__(self, nom, nacionalitat):
        self.nom = nom
        self.nacionalitat = nacionalitat

class Categoria:
    def __init__(self, tipus, definicio):
        self.tipus = tipus
        self.definicio = definicio

class Autor:
    def __init__(self, nom, data_naixement):
        self.nom = nom
        self.data_naixement = data_naixement

class Copia:
    def __init__(self, codi_copia, ubicacio):
        self.codi_copia = codi_copia
        self.ubicacio = ubicacio

class Prestec:
    def __init__(self, data_inici, data_fi, nom_llibre, nom_lector):
        self.data_inici = data_inici
        self.data_fi = data_fi
        self.nom_llibre = nom_llibre
        self.nom_lector = nom_lector

class Lector:
    def __init__(self, nom, cognoms, dni, adreca):
        self.nom = nom
        self.cognoms = cognoms
        self.dni = dni
        self.adreca = adreca

class Multa:
    def __init__(self, data_inici, data_finalitzacio):
        self.data_inici = data_inici
        self.data_finalitzacio = data_finalitzacio

