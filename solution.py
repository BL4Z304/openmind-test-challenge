def genere_combinaison (n, p-ouver=0, p-ferme=0, entre=None, sortie, resultat ):

    if entre is None:
        sortie = []

    elif p-ouver==n and p-ferme==n:
        sortie= ["()"]

    else:

        for n in range(1, 9):
            resultat = genere_combinaison(n)
            print(n, len(resultat))

        
