# Import des librairies necessaire au code
from datetime import datetime

'''
Fonction :
    logging(image, size, sampling, step, nbChannel, chan1, chan2, chan3, lsbList, lsbReverse, lsbOpposite, res, resRev, resOpp)
        image : chemin vers l'image utilisée
        size : tuple contenant la hauteur et largeur de l'image
        sampling : nombre de lignes qui ont été analyser
        step : pas dans la lecture des pixels
        nbChannel: nombre de canaux utiliser
        chan1 : canal 1
        chan2 : canal 2
        chan3 : canal3
        lsbList : liste des LSB obtenue avec analyser/analyser2/analyser3
        lsbReverse : Liste des octets inversé
        lsbOpposite : Liste des opposé des octets
        res : resultat de tout les char imprimables dans lsbList
        resRev : resultat de tout les char imprimables dans lsbReverse
        resOpp : resultat de tout les char imprimables dans lsbOpposite
Explication :
    askNbChannel est une fonction qui permet de savoir si on cherche dans tout les canaux des pixels ou si on veux uniquement en
    regarder 1 ou deux
    retourne un int contenant le nombre de canaux
'''

def logging(image, size, sampling, step, nbChannel, chan1, chan2, chan3, lsbList, lsbReverse, lsbOpposite, res, resRev, resOpp):
    Log = open("log.txt", 'a')
    Log.write("----- LOGS de la recherche ----- \n")
    Log.write("----- Informations Techniques ----- \n")
    Log.write("Image : "+str(image)+"\n")
    Log.write("Taille de l'image : "+ str(size)+"\n")
    Log.write("Nombre de ligne analyse : "+str(sampling)+" / "+str(size[0])+"\n")
    Log.write("Pas utilise pour la recherche : "+str(step)+"\n")
    Log.write("Nombre de canaux analyses sur chaque pixels : "+str(nbChannel)+"\n")
    Log.write("Canaux analyses : "+str(chan1)+" - "+str(chan2)+" - "+str(chan3)+"\n")
    Log.write("---- Resultats du scan ---- \n")
    Log.write("Resultat du scan a la recherche des LSB :\n")
    Log.write(str(lsbList)+"\n")
    Log.write("Resultat de l'inverse du LSB :\n")
    Log.write(str(lsbReverse)+"\n")
    Log.write("Resultat de l'oppose du LSB :\n")
    Log.write(str(lsbOpposite)+"\n")
    Log.write("---- Resultats de l'analyse ---- \n")
    Log.write("Resultat de la recherche dans le LSB :\n")
    Log.write(str(res)+"\n")
    Log.write("Resultat de la recherche dans l'inverse du LSB :\n")
    Log.write(str(resRev)+"\n")
    Log.write("Resultat de la recherche dans l'oppose du LSB :\n")
    Log.write(str(resOpp)+"\n")
    Log.close()
    print("Log sauvegrader dans log.txt")