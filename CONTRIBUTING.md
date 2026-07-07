# Contribuer à Projet-Flask

Merci de vouloir contribuer ! Voici comment procéder.

## Signaler un bug
Ouvrez une issue en utilisant le template **Bug Report** : description, étapes pour reproduire, comportement attendu/obtenu, environnement (OS, Python, Docker).

## Proposer une fonctionnalité
Ouvrez une issue avec le template **Feature Request** : description, motivation, solution envisagée.

## Soumettre une Pull Request
1. Créez une branche depuis `main` (`feature/xxx` ou `fix/xxx`)
2. Développez et testez localement avant de pousser
3. Respectez les conventions ci-dessous
4. Ouvrez la PR en remplissant le template, la CI doit passer avant merge

## Conventions

### Commits
On suit [Conventional Commits](https://www.conventionalcommits.org/) :
- `feat:` nouvelle fonctionnalité
- `fix:` correction de bug
- `docs:` documentation
- `ci:` changement de pipeline
- `test:` ajout/modification de tests

### Style de code
- Formatage : [Black](https://black.readthedocs.io/), line-length 120
  ```bash
  black --check src/ tests/

### Linting : Ruff

ruff check src/ tests/

## Tests
Framework : pytest
Couverture minimale attendue : 70 %

pytest --cov=src --cov-report=term
Toute PR doit passer la CI (formatage, linting, sécurité, tests) avant d'être mergée.

Une fois collé, ajoute-le à git : `git add CONTRIBUTING.md` puis commit avec les autres fichiers de gouvernance.
