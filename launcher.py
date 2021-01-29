# Import des librairies necessaire au code
import os
import tools.channelAnalyse as CA
import tools.charSearch as CS
import tools.other as O
import tools.save as S
import tools.bruteforce as BF

# Affichage des images qui sont dans le repertoire ou est lancer le code
path = O.imgListing()

# Demande de l'image a utiliser
valid = 0 # Variable de la boucle de verification de l'existance du fichier
while valid == 0:
    image = path+input("Entrer le nom de l'image que vous souhaitez analyser (ne pas oublier l'extension) : ")
    if os.path.exists(image):
        valid = 1

# Demande si on veux faire un bruteforce ou une recherche plus specifique
bf = O.askBruteForce()
# Recuperation de la taille de l'image
size = O.sizeFinder(image)
if bf == 0:
    BF.bruteforce(image, size)
else:
    # Demande du sampling
    sampling = O.askSampling(image)

    # Demande du step
    step = O.askStep(sampling, size)

    # Demande du nombre de canaux à analyser
    nbChannel = O.askChannel()

    # Demande de la disposition des canaux
    if nbChannel == 1:
        chan1 = CA.askChannel(nbChannel)
    elif nbChannel == 2:
        chan1, chan2 = CA.askChannel(nbChannel)
    else:
        chan1, chan2, chan3 = CA.askChannel(nbChannel)
    # Demande si on veux reverse
    reverse = CA.askReverse()

    # Demande si on veux l'opposer des octets
    opposite = CA.askOpposite()

    # Partie analyse
    # Analyse d'un canal
    if nbChannel == 1:
        print("Analyse en cours du canal "+str(chan1))
        lsbList = CA.analyser(image, size, chan1, sampling, step)
        res = CS.charSearcher(lsbList)
        print("Elements trouvé : \n"+res)
        if reverse == 1:
            print("Calcul du reverse en cours")
            lsbReverse = CA.reverse(lsbList)
            resRev = CS.charSearcher(lsbReverse)
            print("Elements trouvé : \n" + CS.charSearcher(lsbReverse))
        else:
            lsbReverse = "N/A"
            resRev = "N/A"
        if opposite == 1:
            print("Calcule de l'opposé en cours")
            lsbOpposite = CA.opposite(lsbList)
            resOpp = CS.charSearcher(lsbOpposite)
            print("Elements trouvé : \n" + resOpp)
        else:
            lsbOpposite = "N/A"
            resOpp = "N/A"
        S.logging(image, size, sampling, step, nbChannel, chan1, "N/A", "N/A", lsbList, lsbReverse, lsbOpposite, res, resRev, resOpp)
    # Analyse de deux canaux
    elif nbChannel == 2:
        print("Analyse en cours des canaux "+str(chan1)+" et "+str(chan2))
        lsbList = CA.analyser2(image, size, chan1, chan2, sampling, step)
        res = CS.charSearcher(lsbList)
        print("Elements trouvé : \n" + res)
        if reverse == 1:
            print("Calcul du reverse en cours")
            lsbReverse = CA.reverse(lsbList)
            resRev = CS.charSearcher(lsbReverse)
            print("Elements trouvé : \n" + CS.charSearcher(lsbReverse))
        else:
            lsbReverse = "N/A"
            resRev = "N/A"
        if opposite == 1:
            print("Calcule de l'opposé en cours")
            lsbOpposite = CA.opposite(lsbList)
            resOpp = CS.charSearcher(lsbOpposite)
            print("Elements trouvé : \n" + resOpp)
        else:
            lsbOpposite = "N/A"
            resOpp = "N/A"
        S.logging(image, size, sampling, step, nbChannel, chan1, chan2, "N/A", lsbList, lsbReverse, lsbOpposite, res, resRev, resOpp)
    # Analyse de trois canaux
    else:
        print("Analyse en cours des canaux "+str(chan1)+" , "+str(chan2)+" et "+str(chan3))
        lsbList = CA.analyser3(image, size, chan1, chan2, chan3, sampling, step)
        res = CS.charSearcher(lsbList)
        print("Elements trouvé : \n" + res)
        if reverse == 1:
            print("Calcul du reverse en cours")
            lsbReverse = CA.reverse(lsbList)
            resRev = CS.charSearcher(lsbReverse)
            print("Elements trouvé : \n" + CS.charSearcher(lsbReverse))
        else:
            lsbReverse = "N/A"
            resRev = "N/A"
        if opposite == 1:
            print("Calcule de l'opposé en cours")
            lsbOpposite = CA.opposite(lsbList)
            resOpp = CS.charSearcher(lsbOpposite)
            print("Elements trouvé : \n" + resOpp)
        else:
            lsbOpposite = "N/A"
            resOpp = "N/A"
        S.logging(image, size, sampling, step, nbChannel, chan1, chan2, chan3, lsbList, lsbReverse, lsbOpposite, res, resRev, resOpp)
