## Corrigez ce code écrit par le stagiaire de votre équipe qui n’est pas encore familier avec le métier

Modifications apportées au code :

- Initialisation de orderList : On initialise une orderList au moment de la déclaration pour évité les NullPointerException.
- Validation des index dans modifyOrder : Ajout de vérification dans la fonction modifyOrder pour être sur que les id des articles sont valide avant de modifier les articles, on affiche un message d'erreur si l'index est non-valide.
- Validation des indexs dans removeOrder : Même chose que pour modifyOrder, on ajoute une vérification dans la fonction removeOrder pour être sur que les id des articles sont valide avant de modifier les articles, on affiche un message d'erreur si l'index est non-valide.
