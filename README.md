Aquest es el diagrama del codi UML.

![alt text](image.png)

Tasca 4: En primer lloc, a la classe Clients, s'ha afegit un constructor __init__ que accepta paràmetres per inicialitzar els atributs nom, adreça, telefon i email. Això permet crear instàncies de la classe Clients amb valors específics des del principi.

A la classe Usuaris, s'ha seguit el mateix enfocament afegint un constructor que accepta paràmetres per inicialitzar login, contrasenya i estat. Els mètodes getter i setter també s'han conservat per mantenir la encapsulació de les dades.

L'Enum Estat ha experimentat una modificació en la forma com es defineixen les seves enumeracions. S'han canviat els valors a cadenes de text perquè siguin més descriptius i llegibles.

A la classe Ordre_enviaments, s'ha canviat el nom de l'atribut import a import_ a causa que import és una paraula reservada a Python. A més, s'ha ajustat el constructor per acceptar el paràmetre import_ i s'han reanomenat els paràmetres dataComanda i dataEnviament a data_comanda i data_enviament, respectivament, seguint la convenció de noms de Python (snake_case).

Finalment, s'han creat instàncies de les classes amb valors específics proporcionats. Aquestes instàncies s'han utilitzat per establir relacions entre els objectes, seguint la mateixa lògica que a la versió original del codi. 