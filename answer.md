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

Question 3 (compte-rendu) : Quels avantages a Ruff par rapport à flake8 ? Pourquoi le fichier
pyproject.toml est-il préférable à des arguments en ligne de commande ?

    Ruff est plus rapide que Flake8, possède plus de règles, donc plus précis.
    Flake8 ne possède pas de correction automatique par rapport à Ruff qui l'a.
    Le fichier pyprojet.toml permet de centraliser les configurations en un seul fichier, plutôt que d'utiliser des arguments en ligne de commande.
    Facile à maintenir et à versionner


Question 4 (compte-rendu) : Quelle est la différence entre Bandit et Semgrep ? Dans quel cas
utiliseriez-vous l'un ou l'autre ?

    Bandit s'occupe uniquement de la sécurité, alors que Semgrep s'occupe de la sécurité ainsi que la qualité du code.
    Il vaut mieux prioriser Semgrep pour des projets multi-langage, Bandit étant 100% Python.


Question 5 (compte-rendu) : Qu'est-ce que l'analyse statique ? En quoi diffère-t-elle des tests unitaires ?

    L'analyse statique permet d'examiner le code sans l'éxecuter, alors que les tests unitaires exécutent le code, et vérifient que le comportement est correct.

Question 6 (compte-rendu) : Quel est l'intérêt des pre-commit hooks par rapport à la CI ?
Pourquoi utiliser les deux ?

    Les pre-commit hooks permettent de tester localement avant chaque commit.
    Ils empêchent les erreurs d'être commit et améliore la qualité du code.
    Le pre-commit détecte les erreurs évidentes, alors que la CI fais une vérification complète et standardisée.


Question 7 (compte-rendu) : Un collègue fait un git commit --no-verify pour contourner les
pre-commit hooks. Est-ce un problème ? Pourquoi ?

    Oui, sauf urgence, il n'est pas conseillé de contourner les pre-commit.
    Le contournement peut faire échoué le commit, et perdre plus de temps que celui gagné en contournant.


Question 8 (compte-rendu) : Qu'est-ce qu'un Quality Gate ? Donnez 3 exemples de conditions
qu'on pourrait y mettre.

    Un Quality gate est un ensemble de critères qui doivent être satisfaits pour pouvoir merge le code.
    3 exemples : Tous les tests doivent passer / Couverture de code > 70% / Pas de vulnérabilité de sécurité critique.


Question 9 (compte-rendu) : Décrivez l'ordre des vérifications dans votre pipeline final et
expliquez pourquoi cet ordre est important.

    Checkout code
    Setup Python + Cache Pip
    Dépendances
    Vérification du formatage
    Linting
    Bandit
    Semgrep
    Tests unitaires + couverture
    Sauvegarder rapport


Question 10 (compte-rendu) : Décrivez ce que vous voyez sur le tableau de bord SonarCloud
de votre projet. Quel est le résultat du Quality Gate ? Quels problèmes ont été détectés ?

    Quaity gate status : Failed
    0.0% Security Hotspots Reviewed
    ≥ 100% required

Question 11 (compte-rendu) : Comparez SonarCloud avec les outils locaux (Bandit, Semgrep,
Ruff). Quels sont les avantages d'un outil centralisé comme SonarCloud en entreprise ?

    Avantages :
     Centralisation des projets de l'entreprise
     Traçabilité long terme
     Quality Gates standardisés


TP4

Question 1 (compte-rendu) : Qu'est-ce qu'une CVE ? Expliquez le score CVSS et donnez un
exemple de CVE avec son impact.

    CVE (Common Vulnerabilities and Exposures) : Un identifiant standard pour les vulnérabilités de sécurité découvertes dans des logiciels publiquement connus.

    Le CVSS prend en compte :
        Vecteur d'attaque : réseau, local, physique
        Complexité : facilité à exploiter
        Privilèges requis : non, bas, élevés
        Impact : confidentialité, intégrité, disponibilité

        CVE-2021-44228 - "Log4Shell"

        Vulnérabilité dans Apache Log4j 2
            Score CVSS : 10.0 (Critique)
            Impact : Exécution de code à distance, compromission totale du système
            Les attaquants pouvaient injecter du code malveillant via les logs
            Affecté : millions de serveurs Java mondialement
            Correction : mise à jour urgente de Log4j vers la version 2.17.0+


Question 2 (compte-rendu) : Pourquoi est-il important de scanner les dépendances et pas
seulement votre propre code ?

    Les vulnérabilités critiques viennent souvent des dépendances, pas du code.
    On ne contrôle pas la sécurité du packagage tier.


Question 3 (compte-rendu) : Quel est l'avantage de Dependabot par rapport à un scan manuel
avec pip-audit ? Pourquoi configure-t-on aussi l'écosystème github-actions ?

    Dépendabot : Automatisé, continu, crée des PRs de patch automatiquement. pip-audit : Manual, one-shot, tu dois l'exécuter régulièrement.

    Écosystème github-actions : Les actions du workflow (checkout, setup-python, etc.) sont aussi des dépendances vulnerables. Dependabot les scan et les update automatiquement pour éviter les compromissions supply-chain.

Question 4 (compte-rendu) : Pourquoi ne doit-on jamais mettre un secret directement dans le
code source ? Citez 3 endroits où stocker des secrets de manière sécurisée.

    Si le code est versionné en git, les secrets sont exposés à tous, y compris les anciens commits.
    3 endroits où les stockers :
        Variables d'environnements
        GitHub Secrets
        Gestionnaires de secrets


Question 5 (compte-rendu) : Un développeur a accidentellement commité une clé API GCP
dans le code, puis l'a supprimée dans un commit suivant. Le secret est-il en sécurité ? Que faut-il faire ?

    Révoquer immédiatement la clé GCP
    Nettoyer l'historique git (git filter-branch ou BFG Repo-Cleaner)
    Regénérer une nouvelle clé
    Ajouter le fichier à .gitignore
    Force push après nettoyage


Question 6 (compte-rendu) : Pourquoi GitLeaks est-il placé au tout début du pipeline, avant
même le linting ?

    La sécurité est prioritaire. Il faut arrêter immédiatement si un secret est détecté. Inutile de linter/tester si la sécurité est compromise. Ça évite aussi de gaspiller des ressources et d'exposer les données sensibles dans les logs.

Question 7 (compte-rendu) : Citez 3 risques de l'OWASP Top 10 et expliquez comment votre
pipeline CI les adresse (ou pas).

    3 risques de l'OWASP Top 10 :
        1. A02 : Cryptographic Failures ✅
        Adressé : Bandit (secrets) + GitLeaks (clés exposées)
        Manque : Pas de vérification HTTPS/TLS

    La pipeline couvre bien les injections et secrets, mais ignore complètement les contrôles d'accès.

Question 8 (compte-rendu) : Décrivez l'ordre complet de votre pipeline final. Pour chaque
étape, indiquez quel type de problème elle détecte.

    1. GitLeaks → Détecte les secrets exposés (clés API, tokens, mots de passe)
    2. Installer Python → Prépare l'environnement d'exécution
    3. Cache pip → Optimise les performances (réutilise les cache)
    4. Installer dépendances → Installe les requêtes Python
    5. Black (--check) → Détecte les erreurs de formatage du code
    6. Ruff (linter) → Détecte les violations de style, imports non utilisés, bugs courants
    7. pip-audit → Détecte les vulnérabilités connues dans les dépendances
    8. Bandit → Détecte les problèmes de sécurité Python (injection, cryptographie faible)
    9. Semgrep → Détecte les patterns de sécurité et qualité du code (multi-langage)
    10. Tests pytest + couverture → Vérifie que le code fonctionne correctement et calcule le taux de couverture
    11. SonarCloud Scan → Analyse complète centralisée (qualité, duplications, hotspots sécurité)
    12. Sauvegarder rapport → Archive les résultats de couverture

Question 9 (compte-rendu) : Comparez les approches Shift Left et audit de sécurité traditionnel. Quels sont les avantages du Shift Left ?

    Approche traditionnel : Test en fin de cycle, problèmes coûteux à corriger.

    Shift Left : Test dès le développement.

    Avantages : Coûts réduits, feedback continu, meilleure sécurité, automatisé (GitLeaks, Bandit, pre-commit dès le commit).

Question 10 (compte-rendu) : Votre pipeline contient maintenant de nombreuses étapes. Si le
temps d'exécution devenait trop long, comment pourriez-vous l'optimiser ?

    Paralléliser les jobs
    Cache aggressif
    Aborter tôt
    Réduire outils redondants
    Conditions (SonarCloud sur main/PR seulement)
    Runners optimisés
    Matrix jobs

Question 11 (compte-rendu) : Décrivez la CVE que vous avez trouvée : son identifiant, le
package affecté, le score CVSS, l'impact, et la version corrigée. Expliquez comment pip-audit
ou Dependabot aurait pu prévenir ce problème. Indiquez le lien vers la page de la CVE.

    changedetection.io Authentication Bypass
        Identifiant : CVE-2026-35490
        Package affecté : changedetection.io (pip)
        Sévérité : Critical
        Type : Authentication Bypass via Decorator Ordering
        Publié : 2 weeks ago
        Impact : Accès non authentifié aux endpoints protégés via improper decorator ordering
        Lien : https://github.com/advisories/CVE-2026-35490

    pip-audit -r requirements.txt → détecterait changedetection.io vulnérable
    Dependabot → bloquerait le merge jusqu'à mise à jour vers version corrigée



TP5

Question 1 (compte-rendu) : Expliquez chaque instruction du Dockerfile. Pourquoi copie-t-on
requirements.txt avant le code source ?

    Explication du Dockerfile :

    FROM python:3.12-slim
        Image de base Python

    WORKDIR /app
        Définit le répertoire de travail

    COPY requirements.txt .
        Copie les dépendances

    RUN pip install --no-cache-dir -r requirements.txt
        Installe les dépendances

    COPY src/ ./src/
        Copie le code source

    HEALTHCHECK --interval=30s --timeout=5s --retries=3 \ CMD curl -f http://localhost:5000/health || exit 1
        Vérifie la santé du conteneur

    EXPOSE 5000
        Expose le port 5000

    CMD ["gunicorn", "--bind", "0.0.0.0:5000", "src.app:app"]
    Lance gunicorn au démarrage

    Pourquoi copier requirements.txt en premier ?

       La réponse est dans le dockerfile : # Dependances d'abord (cache Docker)


Question 2 (compte-rendu) : Quelle est la différence entre une VM et un container Docker ?
Quel est l'avantage principal des containers ?

    VM : Émule un OS complet, lourd, démarrage lent
    Container : Utilise le kernel du host, léger, démarrage rapide

    Avantage principal :
    Beaucoup plus léger et rapide qu'une VM. Ça rend le déploiement rapide et moins gourmand en ressources


Question 3 (compte-rendu) : Quel est l'intérêt de Docker Compose par rapport à un simple
docker run ? Dans quel cas Docker Compose devient-il indispensable ?

    docker run demande une longue commande. Docker Compose centralise tout dans un fichier. Indispensable quand il y a plusieurs services qui doivent communiquer.


Question 4 (compte-rendu) : Pourquoi tagger une image avec plusieurs tags (SHA, version,
latest) ? Pourquoi ne doit-on pas utiliser :latest en production ?
    SHA (commit hash) permet de tracer exactement quel code tourne en prod. Version (v1.0) est lisible pour un humain.

    Certains services en prod dépendent d'une version spécifique. Si on déploie une nouvelle version avec latest et que ça casse la compatibilité, toute la production s'arrête.


Question 5 (compte-rendu) : Qu'est-ce qu'un registre de conteneurs ? Comparez ghcr.io,
Docker Hub et Google Artifact Registry.

    Qu'est-ce qu'un registre de conteneurs :

        Un registre est un serveur centralisé où sont stockées et distribuées les images Docker. Il permet aux équipes de partager et de déployer des images.

    Comparaison :

        Docker Hub : Registre public par défaut de Docker. Gratuit avec des images publiques, mais les images privées ont des limitations.

        ghcr.io (GitHub Container Registry) : Registre intégré à GitHub. Gratuit et lié aux dépôts GitHub, idéal pour les projets hébergés sur la plateforme.

        Google Artifact Registry : Registre managé par Google Cloud. Plus robuste et sécurisé, généralement utilisé en entreprise. Nécessite un compte GCP payant.

Question 6 (compte-rendu) : Pourquoi teste-t-on le conteneur dans la CI avant de le pousser
sur le registre ?

    Pour s'assurer que le conteneur fonctionne avant de le rendre public sur ghcr.io. Si l'image a un problème (le code ne démarre pas, le health check échoue, etc.), on le détecte avant le push.

    Ça évite de polluer le registre avec des images cassées et ça économise du temps/ressources.

Question 7 (compte-rendu) : Expliquez la condition if: github.ref == 'refs/heads/main'.
Pourquoi le build Docker ne se déclenche-t-il pas sur les Pull Requests ?

    La condition if: github.ref == 'refs/heads/main' vérifie qu'on est sur la branche main. Sur une PR, github.ref pointe vers la branche de feature, donc la condition est fausse.

    Pourquoi ? Parce qu'on ne veut builder et pusher une image que si le code est déjà validé et mergé sur main. Sur une PR, le code n'est pas encore accepté. Si on buildait à chaque PR, on polluerait le registre avec plein d'images instables.

    L'idée : tester sur la PR, puis une fois mergée sur main, on build l'image pour la production.

Question 8 (compte-rendu) : Pourquoi utilise-t-on ${{ github.sha }} comme tag d'image ?
Quel avantage par rapport à un numéro de version manuel ?

    github.sha c'est le hash unique du commit. Chaque commit a un SHA différent, donc chaque image a un tag unique automatiquement.

    Avantages :
    - C'est automatique, pas d'erreur humaine (pas besoin de se souvenir d'incrémenter la version)
    - Traçabilité parfaite : on sait exactement quel commit/code est en production
    - Pas de doublon : deux commits différents = deux images différentes

    Avec un numéro manuel (v1.0, v1.1, etc.), faut se souvenir d'incrémenter, et c'est facile d'oublier ou de faire une erreur.

Question 9 (compte-rendu) : Qu'est-ce qu'un rollback ? Pourquoi est-il essentiel de versionner les images Docker avec des tags précis ?

    Un rollback c'est revenir à une version précédente d'une application. Par exemple, si la dernière version en prod a un bug, on relance la version d'avant.

    Exemple : docker run ... ghcr.io/app:sha-abc1234 (au lieu de :latest)

    Pourquoi les tags précis sont essentiels :

    Sans tags précis (latest), on sait pas quelle version tourne en prod. Si y a un bug, on peut pas revenir à la version d'avant.

    Avec des tags SHA ou des numéros de version, on a une traçabilité totale. On sait exactement quel code tourne, et on peut revenir à n'importe quelle version précédente en cas de problème.

Question 10 (compte-rendu) : Expliquez la différence entre Continuous Delivery et Continuous Deployment. Lequel avez-vous mis en place dans ce TP ?

    Continuous Delivery : Code automatiquement testé, validé, et prêt pour la prod. Mais le déploiement en prod est manuel.

    Continuous Deployment : Code va automatiquement jusqu'en production sans intervention manuelle.

    Dans ce TP : Continuous Deployment

    Preuve : dès qu'on push sur main, tout est automatique. Tests → build → push sur ghcr.io. L'image est directement disponible en prod sans étape manuelle.

Question 11 (compte-rendu) : Quels risques pose le déploiement automatique ? Comment les atténuer ?

    Risques du déploiement automatique :

     Un bug passe en prod directement et affecte les utilisateurs
     Pas de validation humaine, donc plus d'erreurs
     Données corrompues/perdues si quelque chose tourne mal
     Perte de contrôle, déploiement trop rapide

    Comment les atténuer :

     Tests complets (unitaires, intégration) : ils sont dans la CI
     Review en PR : quelqu'un doit valider avant merge
     Health checks : le conteneur s'arrête si quelque chose tourne mal
     Monitoring en prod : alertes si ça crash
     Rollback rapide avec les tags SHA : revenir à la version précédente en cas de bug
     Staged rollout : déployer progressivement (10% des utilisateurs d'abord, puis 50%, etc.)
     Feature flags : activer/désactiver les features sans redéployer

Question 12 (compte-rendu) : Expliquez le principe du multi-stage build. Quel est l'avantage en termes de taille et de sécurité ? Montrez votre Dockerfile modifié et la différence de taille. Indiquez le lien vers la documentation que vous avez consultée.

    Principe du multi-stage build :

    Un multi-stage build utilise plusieurs FROM dans un Dockerfile. Chaque FROM est une étape. On peut copier des artefacts d'une étape à l'autre avec COPY --from=. Les étapes précédentes disparaissent de l'image finale.

    Idée : séparer la compilation/installation des dépendances de l'exécution de l'app.

    Avantages en taille :

    Stage 1 (builder) : python:3.12 installe les dépendances
    Stage 2 (runtime) : python:3.12-slim reçoit seulement les packages
    L'image finale contient juste ce qu'il faut pour exécuter l'app, pas les outils de build.


    Avantages en sécurité :

    L'image finale n'a pas gcc, make, build tools, etc. Moins d'outils = moins de risques qu'un attaquant les exploite. Surface d'attaque réduite.

    Dockerfile modifié :

        # Stage 1 : Builder
        FROM python:3.12-slim as builder

        WORKDIR /build

        COPY requirements.txt .

        RUN pip install --user --no-cache-dir -r requirements.txt

        # Stage 2 : Runtime (image finale)
        FROM python:3.12-slim

        WORKDIR /app

        # Copie seulement les dépendances installées depuis le builder
        COPY --from=builder /root/.local /root/.local

        ENV PATH=/root/.local/bin:$PATH

        COPY src/ ./src/

        HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
            CMD curl -f http://localhost:5000/health || exit 1

        EXPOSE 5000

        CMD ["gunicorn", "--bind", "0.0.0.0:5000", "src.app:app"]

    Différence de taille :

    flask-app:new                                                                            3e32cc77c32b        777MB      164MB
    flask-app:old                                                                            36db7c26b4b2       2.21GB      535MB

    Documentation :

    https://docs.docker.com/build/building/multi-stage/
    https://docs.docker.com/language/python/build-images/

** TP 7**
Question 1 (compte-rendu) : Qu'est-ce que le concept « Documentation as Code » ? Quels
avantages ?

    Documentation as Code : traiter la doc comme du code. Écrite en Markdown, versionnée dans Git, relue en PR, buildée et déployée automatiquement par la CI.

    Avantages :

    Versionnée (historique, diff, rollback)
    Relue en PR comme le code
    Reste synchro avec le code (même commit/PR)
    Déploiement auto du site via CI
    Pas besoin d'outil proprio, juste du texte

Question 3 (compte-rendu) : Pourquoi un projet open source doit-il avoir une licence ? Que se passe-t-il sans licence ?

    Sans licence, le code reste sous copyright par défaut. Personne (même pas pour un usage perso) n'a le droit légal de l'utiliser, le copier, le modifier ou le redistribuer, même si le repo est public sur GitHub.

    Une licence (MIT, Apache, GPL...) définit explicitement ce que les autres ont le droit de faire avec le code.
