# Import des librairies necessaire au code
from PIL import Image
from textwrap import wrap

'''
Fonction : 
    analyser(selectedImage, size, channel, sampling, step)
        selectedImage : image que l'utilisateur souhaite analyser
                        (choisie dans le menu)
        size : tableau qui continent la largeur et la hauteur de l'image 
               (definie dans le menu avec la fonction sizeFinder())
        channel : canal qui sera utiliser pour la recherche 
                  R : 0
                  G : 1
                  B : 2
        sampling : nombre de lignes que l'on souhaite tester 
                   (si l'utilisateur ne souhaite pas de sampling alors la valeur sera la taille de l'image)
        step : le nombre de pixels à sauter entre chaques mesure 
               (par defaut 1, il fera tout les pixels)

Explication :
    analyser est la fonction qui permet de traiter uniquement un des canaux à la fois
    Liste des possibilitées tester : R, G, B
    La fonction va retourner une liste de d'octets qui seront elaborer depuis les LSB du canal choisi de chaque pixels
    dans le range qui sera donner
'''
def analyser(selectedImage, size, channel, sampling, step):
    # Ouverture de l'image pour pouvoir travailler dessus
    usedImg = Image.open(selectedImage)
    # Creation et initialisation d'une liste pour les valeurs lsb
    lsbList = ""
    for i in range(0, sampling): # permet de chercher dans une partie ou toute l'image
        for j in range(0,size[1],step): # ajoute le pas s'il est renseigner
            # Recuperation du pixel
            pixel = usedImg.getpixel((j,i)) # On utilise (j,i) car on avance dans la ligne
            # Recuperation de la valeur du canal choisi du pixel courant et passage de sa valeur decimal en binaire
            channelBinValue = bin(pixel[channel])
            # Recuperation du LSB
            theLSB = channelBinValue[-1:]
            # Ajout du lsb a la liste en cours
            lsbList = lsbList+theLSB
    # Regroupement en paquets de 8 pour former des octets
    lsbList = wrap(lsbList, 8)
    return lsbList

'''
Fonction : 
    analyser2(selectedImage, size, channelA, channelB, sampling, step)
        selectedImage : image que l'utilisateur souhaite analyser
                        (choisie dans le menu)
        size : tableau qui continent la largeur et la hauteur de l'image 
               (definie dans le menu avec la fonction sizeFinder())
        channelA : premier canal qui sera utiliser pour la recherche 
                  R : 0
                  G : 1
                  B : 2
        channelB : second canal qui sera utiliser pour la recherche 
                  R : 0
                  G : 1
                  B : 2
        sampling : nombre de lignes que l'on souhaite tester 
                   (si l'utilisateur ne souhaite pas de sampling alors la valeur sera la taille de l'image)
        step : le nombre de pixels à sauter entre chaques mesure 
               (par defaut 1, il fera tout les pixels)

Explication :
    analyser est la fonction qui permet de traiter deux des canaux à la fois
    Liste des possibilitées tester : RG, RB, GR, GB, BR, BG
    La fonction va retourner une liste de d'octets qui seront elaborer depuis les LSB des canaux choisi de chaque pixels
    dans le range qui sera donner
'''
def analyser2(selectedImage, size, channelA, channelB, sampling, step):
    # Ouverture de l'image pour pouvoir travailler dessus
    usedImg = Image.open(selectedImage)
    # Creation et initialisation d'une liste pour les valeurs lsb
    lsbList = ""
    for i in range(0, sampling): # permet de chercher dans une partie ou toute l'image
        for j in range(0,size[1],step):# ajoute le pas s'il est renseigner
            # Recuperation du pixel
            pixel = usedImg.getpixel((j,i)) # On utilise (j,i) car on avance dans la ligne
            # Recuperation de la valeur du canal A et B du pixel courant et passage de sa valeur decimal en binaire
            channelABinValue = bin(pixel[channelA])
            channelBBinValue = bin(pixel[channelB])
            # Recuperation du LSB des canaux A et B
            theLSBA = channelABinValue[-1:]
            theLSBB = channelBBinValue[-1:]
            # Ajout des lsb a la liste en cours
            lsbList = lsbList+theLSBA+theLSBB
    # Regroupement en paquets de 8 pour former des octets
    lsbList = wrap(lsbList, 8)
    return lsbList

'''
Fonction : 
    analyser3(selectedImage, size, channelA, channelB, channelC, sampling, step)
        selectedImage : image que l'utilisateur souhaite analyser
                        (choisie dans le menu)
        size : tableau qui continent la largeur et la hauteur de l'image 
               (definie dans le menu avec la fonction sizeFinder())
        channelA : premier canal qui sera utiliser pour la recherche 
                  R : 0
                  G : 1
                  B : 2
        channelB : second canal qui sera utiliser pour la recherche 
                  R : 0
                  G : 1
                  B : 2
        channelB : troisieme canal qui sera utiliser pour la recherche 
                  R : 0
                  G : 1
                  B : 2
        sampling : nombre de lignes que l'on souhaite tester 
                   (si l'utilisateur ne souhaite pas de sampling alors la valeur sera la taille de l'image)
        step : le nombre de pixels à sauter entre chaques mesure 
               (par defaut 1, il fera tout les pixels)

Explication :
    analyser est la fonction qui permet de traiter les trois canaux à la fois
    Liste des possibilitées tester : RGB, RBG, GRB, GBR, BRG, BGR
    La fonction va retourner une liste de d'octets qui seront elaborer depuis les LSB des canaux choisi de chaque pixels
    dans le range qui sera donner
'''
def analyser3(selectedImage, size, channelA, channelB, channelC, sampling, step):
    # Ouverture de l'image pour pouvoir travailler dessus
    usedImg = Image.open(selectedImage)
    # Creation et initialisation d'une liste pour les valeurs lsb
    lsbList = ""
    for i in range(0, sampling): # permet de chercher dans une partie ou toute l'image
        for j in range(0,size[1],step):# ajoute le pas s'il est renseigner
            # Recuperation du pixel
            pixel = usedImg.getpixel((j,i)) # On utilise (j,i) car on avance dans la ligne
            # Recuperation de la valeur des trois canaux du pixel courant et passage de leurs valeurs decimal en binaire
            channelABinValue = bin(pixel[channelA])
            channelBBinValue = bin(pixel[channelB])
            channelCBinValue = bin(pixel[channelC])
            # Recuperation du LSB des trois canaux
            theLSBA = channelABinValue[-1:]
            theLSBB = channelBBinValue[-1:]
            theLSBC = channelCBinValue[-1:]
            # Ajout des lsb a la liste en cours
            lsbList = lsbList+theLSBA+theLSBB+theLSBC
    # Regroupement en paquets de 8 pour former des octets
    lsbList = wrap(lsbList, 8)
    return lsbList

'''
Fonction : 
    reverse(lsbList)
        lsbList : liste qui contient les octets generer lors de l'analyse des canaux
Explication :
    reverse est la fonction qui permet de changer l'ordre des bits dans les octets de la liste generer via les analyse
    LSB des canaux
Exemple :
    liste = ['01000011']
    rev = reverse(liste)
    print(rev)
    >11000010
'''
def reverse(lsbList):
    # Creation d'une liste pour contenir lsbList une voir reverse
    reversedList = []
    for i in range(0, len(lsbList)):
        # Conversion en string pour pouvoir faire le reverse plus facilement
        byteUnit = str(lsbList[i])
        # Il pourrais y avoir moins de 8 bits dans le dernier byte, il est necessaire de connaitre la taille du byte
        # C'est pour ça que l'on cherche sa taille avec len(byteUnit) puis on le swap en lisant la chaine à l'envers sur
        # toute sa longueur
        reversedByteUnit = byteUnit[len(byteUnit)::-1]
        # Ajout du byte reversed a notre liste de sortie
        reversedList.append(reversedByteUnit)
    return reversedList

'''
Fonction : 
    opposite(lsbList)
        lsbList : liste qui contient les octets generer lors de l'analyse des canaux
Explication :
    opposite est la fonction qui permet de donner le contraire des bits dans les octets de la liste generer via les 
    analyse LSB des canaux
Exemple :
    liste = ['11001100','00110101','10011001']
    op = opposite(liste)
    print(op)
    >['00110011', '11001010', '01100110']
'''
def opposite(lsbList):
    # Creation d'une liste pour contenir lsbList une voir reverse
    oppositeList = []
    for i in range(0, len(lsbList)):
        byteUnit = lsbList[i]
        # Il pourrais y avoir moins de 8 bits dans le dernier byte, il est necessaire de connaitre la taille du byte
        # C'est pour ça que l'on cherche sa taille avec len(byteUnit) puis on le swap en lisant la chaine à l'envers sur
        # toute sa longueur
        retOpp = ""
        for i in range(0,len(byteUnit)):
            if byteUnit[i] == '1':
                opp = '0'
            else:
                opp = '1'
            retOpp = retOpp+opp
        # Ajout du byte inverse a notre liste de sortie
        oppositeList.append(str(retOpp))
    return oppositeList

'''
Fonction : 
    askChannel(nbChan)
        nbChan : nombre de canaux à observer
Explication :
    askChannel permet de proposer toutes les dispositions de canaux à l'utilisateur
    Par defaut :
        1 canal = R
        2 canaux = RG
        3 canaux = RGB
    retourne les valeurs des canaux 
'''
def askChannel(nbchan):
    chan1 = 5
    chan2 = 5
    chan3 = 5
    if nbchan == 1:
        print("Ordre possible : R, G, B ")
        while chan1 < 0 or chan1 > 2:
            chan1 = int(input("Analyser le canal rouge (0)(d) | Analyser le canal vert (1) | Analyser le canal bleu (2) : ") or '0')
        return chan1
    elif nbchan == 2:
        print("Ordre possible : RG, RB, GR, GB, BR, BG ")
        print("Canal 1 : ")
        while chan1 < 0 or chan1 > 2:
            chan1 = int(input("Analyser le canal rouge (0)(d) | Analyser le canal vert (1) | Analyser le canal bleu (2) : ") or '0')
        print("Canal 2 : ")
        while chan2 < 0 or chan2 > 2:
            chan2 = int(input("Analyser le canal rouge (0) | Analyser le canal vert (1)(d) | Analyser le canal bleu (2) : ") or '1')
        return chan1,chan2
    else:
        print("Ordre possible : RGB, RBG, GRB, GBR, BRG, BGR")
        print("Canal 1 : ")
        while chan1 < 0 or chan1 > 2:
            chan1 = int(input("Analyser le canal rouge (0)(d) | Analyser le canal vert (1) | Analyser le canal bleu (2) : ") or '0')
        print("Canal 2 : ")
        while chan2 < 0 or chan2 > 2:
            chan2 = int(input("Analyser le canal rouge (0) | Analyser le canal vert (1)(d) | Analyser le canal bleu (2) : ") or '1')
        print("Canal 3 : ")
        while chan3 < 0 or chan3 > 2:
            chan3 = int(input("Analyser le canal rouge (0) | Analyser le canal vert (1) | Analyser le canal bleu (2)(d) : ") or '2')
        return chan1,chan2,chan3

'''
Fonction : 
    askReverse()
Explication :
    askReverse permet de demander à l'utilisateur s'il souhaite reverse le resultat de chaque octets
    Par defaut non est selectionner
    retourne son choix 0 = non 1 = oui
'''
def askReverse():
    choix = 2
    while choix < 0 or choix > 1:
        choix = int(input("Voulez vous inverser les bits dans les octets ? (01000011 -> 11000010)\nNon (0)(d) | Oui (1) : ") or '0')
    return choix

'''
Fonction : 
    askOpposite()
Explication :
    askOpposite permet de demander à l'utilisateur s'il souhaite avoir l'oppose de chaque octets
    Par defaut non est selectionner
    retourne son choix 0 = non 1 = oui
'''
def askOpposite():
    choix = 2
    while choix < 0 or choix > 1:
        choix = int(input("Voulez vous avoir l'opposé des bits dans les octets ? (11001100 -> 00110011)\nNon (0)(d) | Oui (1) : ") or '0')
    return choix