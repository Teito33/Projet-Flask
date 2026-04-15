TP2
Question 1 (compte-rendu) : Décrivez la structure du fichier ci.yml : que signifient on, jobs, runs-on, steps et uses ?

    On : Trigger. Définit quand le workflow s'éxecute
    jobs : Les tâches à éxecuter
    runs-on : L'environnement d'éxecution (VM,OS,etc...)
    steps : Les étapes du job, qui s'éxecutent dans l'ordre défini
    uses : Actions prédéfinies

Question 2 (compte-rendu) : Expliquez le rôle de la fixture client dans les tests Flask.
Pourquoi utilise-t-on app.test_client() plutôt que de lancer le serveur ?

    La fixture client dans les tests Flask permet d'activer le mode test, de créer un client test, et de les fournir à chaque test.
    app.test_client() simule les requêtes HTTP sans lancer un vrai serveur, ce qui rend les tests rapides, fiables et faciles à paralleliser.

Question 3 (compte-rendu) : Pourquoi est-il important de tester localement avant de pousser
? Que se passe-t-il si un test échoue dans la CI ?

    - Détection précoce des erreurs
    - Economie de ressources (Test local = gratuit, test CI = peut coûter en temps serveur)
    - Plus fluide, peut-être corriger directement si test local, sans avoir à attendre le résultat de la CI

    Si le test échoue dans la CI : 
        Workflow s'arrête
        Build marqué comme échoué
        Notification d'échec (mail ou autre)


Question 4 (compte-rendu) : Qu'est-ce qu'un artefact GitHub Actions ? Donnez 3 exemples
d'artefacts utiles.

    Un artefact GitHub Actions est un ensemble de fichier générés lors de l'exécution du workflow. Ils permettent de conserver les résultats des tests, et de les télécharger.
        - Couverture de code
        - Rapports de test
        - Build ou binaires compilés


Question 5 (compte-rendu) : Qu'est-ce que la couverture de code ? Pourquoi 100% n'est pas
toujours souhaitable ?

    La couverture de code indique combien de lignes/branches du code sont éxecutés par les tests.
    Forcer 100% pousse à faire des tests médiocres
    Les derniers 10-20% demandent beaucoup d'efforts pour un rendu limité
    Certains chemins sont impossibles à atteindre dans les tests.

Question 6 (compte-rendu) : Quel est le rôle d'un linter ? Pourquoi l'exécuter avant les tests dans le pipeline ?

    Le linter est un outil qui analyse le code pour vérifier qu'il respecte les conventions.
    Il est exécuté avant les tests, pour l'économie de ressource, pour vérifier que les conventions sont bien respectés avant de lancer ces derniers.


Question 7 (compte-rendu) : Comment fonctionne le cache dans GitHub Actions ? Que se
passe-t-il quand requirements.txt change ?

    Le cache dans GitHub Actions permet de sauvegarder le dossier, ce qui permet de le restaurer au lieu de le réinstaller à chaque exécution.
    Lorsque requirements.txt change, GitHub installe les nouvelles dépendances, et crée un nouveau cache.


Question 8 (compte-rendu) : Comparez les runners GitHub-hosted et self-hosted : avantages,
inconvénients, et dans quel cas utiliser chacun.

    GitHub-Hosted : 
        Avantages : Prêt à l'emploi, aucune configuration. Toujours à jour
        Inconvénients : Coûteux pour les private repos, pas de contrôle sur l'infrastructure, démarrage plus lent
        Cas d'usage : Projets open-source, petites équipes, Workflows standards

    Self-hosted : 
        Avantages : Pas de coûts supplémentaires, accès aux ressources internes, démarrage instantané
        Inconvénients : Configuration et maintenance manuelle requise, sécurité à notre charge, mise à jour à gérer
        Cas d'usage : Entreprise avec repos private importants, accès aux ressources de l'entreprise nécessaire, Sécurité scricte.
        

Question 9 (compte-rendu) : Décrivez le workflow complet qu'un développeur doit suivre pour
intégrer du code quand la branche main est protégée.

    - Créer une branche depuis main
    - Développer et tester localement avant de pousser
    - Commit et push
    - Créer une PR
    - Attendre les test de la CI
    - Mettre à jour la branche local

TP3 
Question 1 (compte-rendu) : Quelle est la différence entre un linter et un formatter ? Donnez
un exemple de chaque en Python.

    Linter : Détecte les erreurs de style et de conventions, mais ne corrige pas les problèmes.

    Formatter : Corrige automatiquement le formatage du code

    Exemple Linter :
        Run flake8 src/ tests/ --max-line-length=120
        src/app.py:28:1: W293 blank line contains whitespace
        src/app.py:28:5: W292 no newline at end of file

    Exemple Formatter : 
        # Avant (désorganisé)
        def my_function(x,y):
        z=x+y
        return z

        # Après black --format (corrigé automatiquement)
        def my_function(x, y):
        z = x + y
        return z


Question 2 (compte-rendu) : Pourquoi utilise-t-on --check dans la CI plutôt que de laisser la
CI formater le code directement ?

    Permet de garder le contrôle des changements, et d'avoir une traçabilité, qu'il n'y aurait pas si le code était formaté directement.
    Permet d'être conscient de tous les changements, ce qui ne serait pas le cas si c'était automatique.

    