class Clients:
    def __init__(self, nom, adreça, telefon, email):
        self.nom = nom
        self.adreça = adreça
        self.telefon = telefon
        self.email = email
    
    def getNom(self):
        return self.nom
    
    def setNom(self, nom):
        self.nom = nom
    
    def getAdreça(self):
        return self.adreça
    
    def setAdreça(self, adreça):
        self.adreça = adreça
    
    def getTelefon(self):
        return self.telefon
    
    def setTelefon(self, telefon):
        self.telefon = telefon
    
    def getEmail(self):
        return self.email
    
    def setEmail(self, email):
        self.email = email

class Usuaris:
    def __init__(self, login, contrasenya, estat):
        self.login = login
        self.contrasenya = contrasenya
        self.estat = estat
    
    def getLogin(self):
        return self.login
    
    def setLogin(self, login):
        self.login = login
    
    def getContrasenya(self):
        return self.contrasenya
    
    def setContrasenya(self, contrasenya):
        self.contrasenya = contrasenya
    
    def getEstat(self):
        return self.estat
    
    def setEstat(self, estat):
        self.estat = estat

class Estat(Enum):
    NOU = 'nou'
    ACTIU = 'actiu'
    BLOQUEJAT = 'bloquejat'
    BANNEJAT = 'bannejat'

class Carros:
    def __init__(self, id_carro):
        self.id_carro = id_carro

class Linies_de_comanda:
    def __init__(self, id_comanda, quantitat, preu):
        self.id_comanda = id_comanda
        self.quantitat = quantitat
        self.preu = preu

class Productes:
    def __init__(self, id_producte, nom_producte, proveidor):
        self.id_producte = id_producte
        self.nom_producte = nom_producte
        self.proveidor = proveidor

class Factures:
    def __init__(self, id_factura, adreça_factura, data_emissio, data_tancament, pagament):
        self.id_factura = id_factura
        self.adreça_factura = adreça_factura
        self.data_emissio = data_emissio
        self.data_tancament = data_tancament
        self.pagament = pagament

class Ordre_enviaments:
    def __init__(self, id_ordre, dataComanda, dataEnviament, destinacio, import_, estat):
        self.id_ordre = id_ordre
        self.dataComanda = dataComanda
        self.dataEnviament = dataEnviament
        self.destinacio = destinacio
        self.import_ = import_
        self.estat = estat

# Relacions entre les classes
clients = Clients("John Doe", "Carrer Major 123", 123456789, "john@example.com")
usuaris = Usuaris("john_doe", "password123", Estat.ACTIU)
carros = Carros(1)
linia_comanda = Linies_de_comanda(1, 2, 10.99)
producte = Productes(1, "Producte A", "Proveïdor X")
factura = Factures(1, "Carrer Principal 456", "2024-03-04", "2024-03-05", "Targeta de crèdit")
ordre_enviament = Ordre_enviaments(1, "2024-03-04", "2024-03-05", "Destinació Y", 50.0, Estat.NOVA)

# Relacions entre els objectes
clients_usuaris = [usuaris]
usuaris_carros = [carros]
carros_linies_comanda = [linia_comanda]
linia_comanda_producte = [producte]
carros_factures = [factura]
factures_ordres_enviament = [ordre_enviament]
