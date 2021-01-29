import tools.channelAnalyse as CA
import tools.charSearch as CS
def bruteforce(image,size):
    print("Bruteforce ON :")
    print("Analyse en cours du canal R")
    lsbList = CA.analyser(image, size, 0, size[0], 1)
    res = CS.charSearcher(lsbList)
    print("Elements trouvé : \n" + res)
    print("Analyse en cours du canal G")
    print("Calcul du reverse en cours")
    lsbReverse = CA.reverse(lsbList)
    print("Elements trouvé : \n" + CS.charSearcher(lsbReverse))
    print("Calcule de l'opposé en cours")
    lsbOpposite = CA.opposite(lsbList)
    resOpp = CS.charSearcher(lsbOpposite)
    print("Elements trouvé : \n" + resOpp)
    lsbList = CA.analyser(image, size, 1, size[0], 1)
    res = CS.charSearcher(lsbList)
    print("Elements trouvé : \n" + res)
    print("Calcul du reverse en cours")
    lsbReverse = CA.reverse(lsbList)
    print("Elements trouvé : \n" + CS.charSearcher(lsbReverse))
    print("Calcule de l'opposé en cours")
    lsbOpposite = CA.opposite(lsbList)
    resOpp = CS.charSearcher(lsbOpposite)
    print("Elements trouvé : \n" + resOpp)
    print("Analyse en cours du canal B")
    lsbList = CA.analyser(image, size, 2, size[0], 1)
    res = CS.charSearcher(lsbList)
    print("Elements trouvé : \n" + res)
    print("Calcul du reverse en cours")
    lsbReverse = CA.reverse(lsbList)
    print("Elements trouvé : \n" + CS.charSearcher(lsbReverse))
    print("Calcule de l'opposé en cours")
    lsbOpposite = CA.opposite(lsbList)
    resOpp = CS.charSearcher(lsbOpposite)
    print("Elements trouvé : \n" + resOpp)
    print("Analyse en cours du canal RG")
    print("Analyse en cours des canaux RG")
    lsbList = CA.analyser2(image, size, 0, 1, size[0], 1)
    res = CS.charSearcher(lsbList)
    print("Elements trouvé : \n" + res)
    print("Calcul du reverse en cours")
    lsbReverse = CA.reverse(lsbList)
    print("Elements trouvé : \n" + CS.charSearcher(lsbReverse))
    print("Calcule de l'opposé en cours")
    lsbOpposite = CA.opposite(lsbList)
    resOpp = CS.charSearcher(lsbOpposite)
    print("Elements trouvé : \n" + resOpp)
    print("Analyse en cours du canal RB")
    lsbList = CA.analyser2(image, size, 0, 2, size[0], 1)
    res = CS.charSearcher(lsbList)
    print("Elements trouvé : \n" + res)
    print("Calcul du reverse en cours")
    lsbReverse = CA.reverse(lsbList)
    print("Elements trouvé : \n" + CS.charSearcher(lsbReverse))
    print("Calcule de l'opposé en cours")
    lsbOpposite = CA.opposite(lsbList)
    resOpp = CS.charSearcher(lsbOpposite)
    print("Elements trouvé : \n" + resOpp)
    print("Analyse en cours du canal GR")
    lsbList = CA.analyser2(image, size, 1, 0, size[0], 1)
    res = CS.charSearcher(lsbList)
    print("Elements trouvé : \n" + res)
    print("Calcul du reverse en cours")
    lsbReverse = CA.reverse(lsbList)
    print("Elements trouvé : \n" + CS.charSearcher(lsbReverse))
    print("Calcule de l'opposé en cours")
    lsbOpposite = CA.opposite(lsbList)
    resOpp = CS.charSearcher(lsbOpposite)
    print("Elements trouvé : \n" + resOpp)
    print("Analyse en cours du canal GB")
    lsbList = CA.analyser2(image, size, 0, 1, size[0], 1)
    res = CS.charSearcher(lsbList)
    print("Elements trouvé : \n" + res)
    print("Calcul du reverse en cours")
    lsbReverse = CA.reverse(lsbList)
    print("Elements trouvé : \n" + CS.charSearcher(lsbReverse))
    print("Calcule de l'opposé en cours")
    lsbOpposite = CA.opposite(lsbList)
    resOpp = CS.charSearcher(lsbOpposite)
    print("Elements trouvé : \n" + resOpp)
    print("Analyse en cours du canal BR")
    lsbList = CA.analyser2(image, size, 2, 0, size[0], 1)
    res = CS.charSearcher(lsbList)
    print("Elements trouvé : \n" + res)
    print("Calcul du reverse en cours")
    lsbReverse = CA.reverse(lsbList)
    print("Elements trouvé : \n" + CS.charSearcher(lsbReverse))
    print("Calcule de l'opposé en cours")
    lsbOpposite = CA.opposite(lsbList)
    resOpp = CS.charSearcher(lsbOpposite)
    print("Elements trouvé : \n" + resOpp)
    print("Analyse en cours du canal BG")
    lsbList = CA.analyser2(image, size, 2, 1, size[0], 1)
    res = CS.charSearcher(lsbList)
    print("Elements trouvé : \n" + res)
    print("Calcul du reverse en cours")
    lsbReverse = CA.reverse(lsbList)
    print("Elements trouvé : \n" + CS.charSearcher(lsbReverse))
    print("Calcule de l'opposé en cours")
    lsbOpposite = CA.opposite(lsbList)
    resOpp = CS.charSearcher(lsbOpposite)
    print("Elements trouvé : \n" + resOpp)
    print("Analyse en cours du canal RGB")
    lsbList = CA.analyser3(image, size, 0, 1, 2, size[0], 1)
    res = CS.charSearcher(lsbList)
    print("Elements trouvé : \n" + res)
    print("Calcul du reverse en cours")
    lsbReverse = CA.reverse(lsbList)
    print("Elements trouvé : \n" + CS.charSearcher(lsbReverse))
    print("Calcule de l'opposé en cours")
    lsbOpposite = CA.opposite(lsbList)
    resOpp = CS.charSearcher(lsbOpposite)
    print("Elements trouvé : \n" + resOpp)
    print("Analyse en cours du canal RBG")
    lsbList = CA.analyser3(image, size, 0, 2, 1, size[0], 1)
    res = CS.charSearcher(lsbList)
    print("Elements trouvé : \n" + res)
    print("Calcul du reverse en cours")
    lsbReverse = CA.reverse(lsbList)
    print("Elements trouvé : \n" + CS.charSearcher(lsbReverse))
    print("Calcule de l'opposé en cours")
    lsbOpposite = CA.opposite(lsbList)
    resOpp = CS.charSearcher(lsbOpposite)
    print("Elements trouvé : \n" + resOpp)
    print("Analyse en cours du canal GRB")
    lsbList = CA.analyser3(image, size, 1, 0, 2, size[0], 1)
    res = CS.charSearcher(lsbList)
    print("Elements trouvé : \n" + res)
    print("Calcul du reverse en cours")
    lsbReverse = CA.reverse(lsbList)
    print("Elements trouvé : \n" + CS.charSearcher(lsbReverse))
    print("Calcule de l'opposé en cours")
    lsbOpposite = CA.opposite(lsbList)
    resOpp = CS.charSearcher(lsbOpposite)
    print("Elements trouvé : \n" + resOpp)
    print("Analyse en cours du canal GBR")
    lsbList = CA.analyser3(image, size, 1, 2, 0, size[0], 1)
    res = CS.charSearcher(lsbList)
    print("Elements trouvé : \n" + res)
    print("Calcul du reverse en cours")
    lsbReverse = CA.reverse(lsbList)
    print("Elements trouvé : \n" + CS.charSearcher(lsbReverse))
    print("Calcule de l'opposé en cours")
    lsbOpposite = CA.opposite(lsbList)
    resOpp = CS.charSearcher(lsbOpposite)
    print("Elements trouvé : \n" + resOpp)
    print("Analyse en cours du canal BRG")
    lsbList = CA.analyser3(image, size, 2, 0, 1, size[0], 1)
    res = CS.charSearcher(lsbList)
    print("Elements trouvé : \n" + res)
    print("Calcul du reverse en cours")
    lsbReverse = CA.reverse(lsbList)
    print("Elements trouvé : \n" + CS.charSearcher(lsbReverse))
    print("Calcule de l'opposé en cours")
    lsbOpposite = CA.opposite(lsbList)
    resOpp = CS.charSearcher(lsbOpposite)
    print("Elements trouvé : \n" + resOpp)
    print("Analyse en cours du canal BGR")
    lsbList = CA.analyser3(image, size, 2, 1, 0, size[0], 1)
    res = CS.charSearcher(lsbList)
    print("Elements trouvé : \n" + res)
    print("Calcul du reverse en cours")
    lsbReverse = CA.reverse(lsbList)
    print("Elements trouvé : \n" + CS.charSearcher(lsbReverse))
    print("Calcule de l'opposé en cours")
    lsbOpposite = CA.opposite(lsbList)
    resOpp = CS.charSearcher(lsbOpposite)
    print("Elements trouvé : \n" + resOpp)