# DEEPER — Recursion practice

Dépôt d'entraînement basé sur le sujet **DEEPER: The Recursion Protocol 1.2.0** fourni en PDF. Le dépôt est volontairement incomplet : tu dois écrire toi-même les fonctions avant le TP.

## Démarrage dans VS Code

1. Décompresse l'archive et ouvre le dossier `deeper-recursion-practice` dans VS Code.
2. Sélectionne Python 3.10 ou plus récent.
3. Complète les `pass` dans `deeper/` sans modifier les signatures des fonctions.
4. Dans le terminal intégré, exécute :

   ```powershell
   python -m unittest discover -s tests -v
   ```

Les tests de `test_public.py` vont **échouer au départ** puisque les fonctions sont des squelettes. Au fur et à mesure que tu avances, ils doivent passer. Les tests de `test_rules.py` contrôlent déjà certaines interdictions structurelles.

## Règles principales du sujet

- Recursion réelle obligatoire, avec cas de base clair.
- Interdiction des boucles `for`/`while`, compréhensions, `break` et `continue` dans les fonctions du TP.
- L'opérateur `**` est interdit partout dans les exercices.
- Respecter les restrictions propres à chaque fonction : elles sont notées dans les docstrings et dans [`docs/EXERCISES.md`](docs/EXERCISES.md).
- Lever `ValueError` quand le sujet le demande.
- Pas de `print()` de débogage dans les fonctions; `hanoi` fait exception car elle doit afficher les déplacements.
- Le test d'Ackermann doit rester petit : les nombres peuvent croître très rapidement.

## Fonctions à réaliser

```text
deeper/
  descent/
    depth_gauge.py   # depth_sum
    oxygen.py        # oxygen
    signal.py        # signal_power
    echoes.py        # echo (Fibonacci)
    beacon.py        # countdown_beacon
  core/
    layers.py        # layer_sum
    deepest.py       # deepest_digit
    gates.py         # gate_gcd
    binary.py        # to_binary
    abyss.py         # ackermann
    tower.py         # hanoi
tests/
  test_public.py     # exemples et cas invalides
  test_rules.py      # interdictions syntaxiques simples
  test_extra.py      # espace pour tes propres tests
docs/
  EXERCISES.md       # spécifications résumées
  EXAM_WORKFLOW.md   # planning d'entraînement sur 3 h
```

## Publier sur ton GitHub

Le connecteur GitHub actuellement associé à la conversation n'expose aucun dépôt accessible et ne permet pas de créer un nouveau dépôt distant. Tu peux donc utiliser cette archive comme base puis créer un dépôt **vide** sur GitHub. Dans le dossier du projet, ouvre le terminal et lance les commandes ci-dessous (remplace l'URL par celle affichée par GitHub) :

```powershell
git init -b main
git add .
git commit -m "Initialise le dépôt d'entraînement DEEPER"
git remote add origin https://github.com/TON-COMPTE/TON-DEPOT.git
git push -u origin main
```

Après tes exercices, pour envoyer les modifications :

```powershell
git add .
git commit -m "Complète les exercices de récursivité"
git push
```

## Attention : le vrai dépôt d'examen EPITA

Le PDF indique que, **dans le dépôt fourni pendant l'examen**, il faut utiliser la commande `submission` au lieu de faire manuellement les commits et tags. Le sujet précise que la notation se fait sur le dernier tag créé par cette commande. Cette commande officielle n'est pas incluse dans ce dépôt personnel : le jour de l'épreuve, suis les consignes présentes dans le dépôt fourni par EPITA.
