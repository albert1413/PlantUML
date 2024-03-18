Aquest es el diagrama del codi UML.

![alt text](image.png)

Tasca 4: Els canvis que s'han fet en el segon codi de classes respecte al codi proporcionat inicialment són:

Al primer, s'han eliminat l'ús de mètodes específics per a l'accés i la modificació dels atributs de les classes. Mentre que en el codi original es defineixen mètodes set i get per a aquesta finalitat.

En el codi original, es feia servir mètodes d'inicialització separats per a cada atribut, mentre que ara tots els valors dels atributs s'assignen directament dins de l'inicialitzador __init__().

En el codi original, els atributs estaven encapsulats dins de mètodes d'accés i modificació, proporcionant un cert grau de protecció i ocultació de les dades. No obstant, en el nou codi els atributs són accessibles directament des de fora de les classes, reduint així el nivell de encapsulació i fent les dades més accessibles.

El nou codi és més concís i senzill, ja que no requereix la definició de mètodes addicionals per a l'accés i la modificació dels atributs, cosa que el fa més fàcil d'entendre i mantenir, especialment en projectes de menor escala o complexitat.