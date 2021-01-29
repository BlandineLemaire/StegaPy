# Import des librairies necessaire au code
from PIL import Image
import os

''' 
Fonction : 
    sizeFinder(image)
        image : image dont on souhaite trouver la hauteur et la largeur 

Explication : 
    sizeFinder est une fonction qui permet de trouver et retourner la taille de l'image qui est donnee en parametre sous
    la forme d'un tuple (hauteur - largeur)

Exemple : 
    sizeFinder("./IMG.jpg") = (400, 650) 
'''
def sizeFinder(imageSRC):
    source = Image.open(imageSRC)
    size = ( source.height,source.width )
    return size

'''
Fonction : 
    imgListing()

Explication : 
    imgListing est une fonction que j'ai ajouter au cours du developpement pour faciliter les input de l'utilisateur la 
    fonction permet de lister toutes les images au format .png et .jpg qui sont dans le repertoire courant

Info : 
    il n'est pas compliquer d'ajouter des extensions à la recherche ou de changer le repertoire de recherche 
    cf - explications dans le code

Exemple :
    imgListing(): # Dans un repertoire contenant [test.txt,image1.png,image2.jpg]
    retour : 
        >  image1.png
        >  image2.jpg
'''
def imgListing():
    # Dans un premier temps il faut lister tout les fichiers dans le repertoire
    # (j'ai decider de prendre "." (repertoire courant), on peux changer ce repertorie dans la variable path.)
    path = "./"
    allTheFiles = os.listdir(path)
    # Affichage du chemin vers ce repertoire
    print("Le chemin vers le repertoire est : ",path)
    # On va maintenant regarder les extensions de chacun des fichiers que l'on a trouver
    for file in allTheFiles:
        # la ligne suivante permet de recuperer l'extension du fichier
        fileExtense = os.path.splitext(file)
        # On va maintenant regarder si l'extension est une de celles que l'on souhaite afficher
        # Il est possible d'en ajouter autant qu'on le souhaite sous le format suivant :
        #   or fileExtense[1] == ".extension"
        if fileExtense[1] == ".png" or fileExtense[1] == ".jpg":
            print("> ",file)
    return (path)

'''
Fonction : 
    askSampling(image)
        image : path vers l'image qui est à analyser
    
Explication : 
    askSampling est une fonction qui permet de savoir si on cherche dans toute l'image ou uniquement dans une partie
    retourne un int contenant le nombre de lignes qui seront à analyser
    Par defaut toute l'image est analysée
'''
def askSampling(image):
    taille = sizeFinder(image)
    sample = 0 # Variable qui va contenir la taille de la zone de recherche
    choix = 0 # Variable qui continent le choix de l'utilisateur
    while choix < 1 or choix > 2:
        choix = int(input("Analyser toute l'image (1)(d) | Analyser une partie seulement (2) : ") or '1')
    if choix == 1 :
        sample = taille[0]
    else:
        while sample < 1 or sample > (taille[0]):
            sample = int(input("Veuillez choisir une valeur d'analyse entre 1 et "+str(taille[0])+" : "))
    return sample


'''
Fonction : 
    askStep()

Explication : 
    askStep est une fonction qui permet de savoir si on cherche dans tout les pixels ou si on veux uniquement en 
    regarder 1 tout les n 
    Par defaut le pas est de 1
    retourne un int contenant le pas 
'''
def askStep(sample,size):
    step = 1 # Variable qui va contenir le pas
    choix = 0 # Variable qui continent le choix de l'utilisateur
    while choix < 1 or choix > 2:
        choix = int(input("Analyser tout les pixels (1)(d) | Analyser une partie seulement (2) : ")or '1')
    if choix == 2 :
        while step < 2 or step > (sample*size[1]):
            step = int(input("Veuillez choisir une valeur de pas entre 1 et "+str(int((sample*size[1])/8))+" : "))
    return step

'''
Fonction : 
    askChannel()

Explication : 
    askNbChannel est une fonction qui permet de savoir si on cherche dans tout les canaux des pixels ou si on veux uniquement en 
    regarder 1 ou deux
    Par defaut tout les canaux sont analyser
    retourne un int contenant le nombre de canaux 
'''
def askChannel():
    choix = 0 # Variable qui continent le choix de l'utilisateur
    while choix < 1 or choix > 3:
        choix = int(input("Analyser un canal (1) | Analyser deux canaux (2) | Analyser trois canaux (3)(d) : " ) or '3')
    return choix

'''
Fonction : 
    askBruteForce()

Explication : 
    askBruteForce est une fonction qui permet de savoir si on effectu une recherche par bruteforce ou une recherche plus specifique 
    Par defaut on effectu une recherche detaillée 
    retourne un int contenant le choix  
'''
def askBruteForce():
    choix = -1
    while choix < 0 or choix > 1:
        choix = int(input("Voulez vous utiliser le BruteForce(0) ou choisir vous mêmes les options de recherche(1)(d) ?") or '1')
    return choix