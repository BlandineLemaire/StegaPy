'''
Fonction :
    charSearcher(byteList)
        byteList : liste de byte dans lesquels on va chercher tout les caracteres qui sont imprimable

Explication :
    charSearcher est une fonction qui permet de trouver tout les caracteres imprimable qui sont dans
    une liste de bytes et de les retourner dans une variable qui les contient. On va regarde les
    valeurs decimale de chaque byte et si elle est entre 32(spc) et 126(~) alors on l'ajoutera à la
    variable de sortie

Exemple :
    liste = ['01110100','01100101','01110011','01110100']
    lesChar = charSearcher(liste)
    print(lesChar)
        >test
'''


def charSearcher(byteList):
    # Initialisation de la variable qui va contenir tout les char trouver dans la liste
    listOfChar = ""
    # Boucle sur tout les char de la liste passee en arguments
    for i in range(0, len(byteList)):
        # On regarde les valeurs decimale de chaque byte et si elle est entre 32 et 126 alors on l'ajout
        # a notre liste de char
        if int(byteList[i], 2) > 31 and int(byteList[i], 2) < 127:
            # Ajout du char dans la liste
            listOfChar = listOfChar + chr(int(byteList[i], 2))
    return listOfChar

