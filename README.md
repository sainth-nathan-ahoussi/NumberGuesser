# Number Guesser

## Introduction

**Number Guesser** est un jeu simple en Python où le joueur tente de deviner un nombre généré aléatoirement. Le jeu fournit des indices pour indiquer si le nombre cible est supérieur ou inférieur à la proposition du joueur. Ce dernier doit trouver le bon nombre en un nombre limité de tentatives.

Ce projet est une façon ludique de pratiquer des concepts fondamentaux de Python tels que les boucles, les conditions, et la génération de nombres aléatoires.

## Table des Matières

- [Introduction](#introduction)
- [Fonctionnalités](#fonctionnalités)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Améliorations Futures](#améliorations-futures)
- [Exemples](#exemples)
- [Contributeurs](#contributeurs)
- [Licence](#licence)

## Fonctionnalités

- **Génération Aléatoire de Nombres** : Un nouveau nombre aléatoire est généré à chaque partie.
- **Indices** : Fournit des indices sur la longueur du nombre et si la proposition est supérieure ou inférieure au nombre cible.
- **Système de Vies** : Le joueur dispose de 4 tentatives pour deviner le bon nombre.
- **Bannière ASCII** : Affiche une bannière stylisée lors du démarrage du jeu.

## Installation

1. **Cloner le Dépôt** :
   ```bash
   git clone https://github.com/sainth-nathan-ahoussi/NumberGuesser.git
   cd NumberGuesser
   ```
2. **Installer Python** :
   Assurez-vous d'avoir Python 3.x installé sur votre système. Vous pouvez le télécharger depuis [python.org](https://www.python.org).

3. **Lancer le Jeu** :
   Exécutez directement le script :
   ```bash
   python NumberGuesser.py
   ```

## Utilisation

1. Lancez le jeu en exécutant le script.
2. Proposez vos nombres lorsque cela vous est demandé.
3. Utilisez les indices fournis pour affiner vos propositions.
4. Trouvez le bon nombre avant de perdre toutes vos vies !

## Améliorations Futures

Le script contient des idées pour des fonctionnalités à venir :
- **Animations de Jeu** : Ajouter des animations pour enrichir l'expérience.
- **Minuteur** : Implémenter un compte à rebours pour augmenter la difficulté.
- **Système d'Indices** : Permettre aux joueurs d'utiliser des indices en échange d’un coût, tels que :
  - Afficher le début ou la fin du nombre.
  - Vérifier si un chiffre spécifique est dans le nombre.
- **Système de Paiement en Jeu** : Introduire une mécanique de paiement pour les indices.

## Exemples

### Exemple de Partie
```plaintext
Petit indice, le nombre à trouver à une longueur de 5
Proposez un nombre : 12345
Raté ! C'est moins, il vous reste 3 vie.
Proposez un nombre : 54321
Raté ! C'est plus, il vous reste 2 vie.
Proposez un nombre : 43210
Bien joué, vous avez trouvé ! Il vous restait 2 vie.
```

## Contributeurs

- **AHOUSSI Sainth-Nathan** – *Développeur et Mainteneur*

## Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.
