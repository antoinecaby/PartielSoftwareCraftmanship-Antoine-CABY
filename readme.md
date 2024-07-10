# Corrigez ce code écrit par le stagiaire de votre équipe qui n’est pas encore familier avec le métier

Modifications apportées au code :

- Initialisation de orderList : On initialise une orderList au moment de la déclaration pour évité les NullPointerException.
- Validation des index dans modifyOrder : Ajout de vérification dans la fonction modifyOrder pour être sur que les id des articles sont valide avant de modifier les articles, on affiche un message d'erreur si l'index est non-valide.
- Validation des indexs dans removeOrder : Même chose que pour modifyOrder, on ajoute une vérification dans la fonction removeOrder pour être sur que les id des articles sont valide avant de modifier les articles, on affiche un message d'erreur si l'index est non-valide.

# Qu’est ce que du code propre ?

Un code propre est un code qui valides plusieurs règles :

- Il faut qu'il passe tous les test, pour celà on peut utiliser la méthode T.D.D. (Test Driven Developpement) qui consiste à écrire dans un premier temps les test et développer notre solution pour que les test soient valides
- Il faut qu'il décrive une intention, il faut que l'on puisse savoir à quoi il sert rien qu'en le lisant
- Il ne faut pas qu'il contienne des duplications, pour celà on peut retenir D.R.Y. pour Dont Repeat Yoursefl ou encore W.E.T. pour Write Everything Twice qui consiste à ne pas dupliquer plus de 2 fois son code
- Il faut qu'il utilise un nombre minimum de classe, fonction, méthode, etc...
