import random

# Reste à implémenter :
# -- Animation au début du lancement du jeu 
# -- Timer 
# -- Utiliser des items pour avoir des indices (début de nombres, fin nombre, demander si un chiffre est dans le nombre )
# -- Mode de paiement pour les indices 



def tirage_number():
    numTofind = random.randrange(100000) 
    return numTofind

def Intro():
     print(
                """
        ░░░█▀█░█░█░█▄█░█▀▄░█▀▀░█▀▄░░░█▀▀░█░█░█▀▀░█▀▀░█▀▀░█▀▀░█▀▄
        ░░░█░█░█░█░█░█░█▀▄░█▀▀░█▀▄░░░█░█░█░█░█▀▀░▀▀█░▀▀█░█▀▀░█▀▄
        ░░░▀░▀░▀▀▀░▀░▀░▀▀░░▀▀▀░▀░▀░░░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀▀▀░▀░▀
        """
    )

def jouer():
    life = 4 
    Playernumber = 0
    TrueNumber = tirage_number()
    print("Petit indice, le nombre a trouvé à une longueur de",len(str(TrueNumber)))
    while life > 0 :
        Playernumber = int(input("Proposez un nombre : "))

        if Playernumber == TrueNumber:
            print("Bien joué, vous avez trouvé ! Il vous restait", life, "vie")
            break

        if  Playernumber > TrueNumber :
            life -= 1
            print(f"Raté ! C'est moins, il vous reste {life} vie.")
           
        else:
            life -= 1
            print(f"Raté ! C'est plus, il vous reste {life} vie.")
    else:
        print("Désolé, vous avez perdu ! Le nombre était :", TrueNumber)
        
        

jouer()