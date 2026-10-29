# Entraînement en conditions de TP — 3 heures

## Chronomètre conseillé

- **00–10 min** : lire toutes les signatures, les domaines et les interdictions.
- **10–65 min** : `depth_sum`, `oxygen`, `signal_power`, `countdown_beacon`. 
- **65–95 min** : `echo` (penser aux deux appels récursifs).
- **95–135 min** : `layer_sum`, `deepest_digit`, `gate_gcd`, `to_binary`.
- **135–155 min** : `ackermann`, en gardant des tests petits; puis `hanoi`.
- **155–175 min** : lancer toute la suite de tests, corriger les cas limites.
- **175–180 min** : inspecter le diff et pousser le travail.

Adapte cet ordre aux consignes du sujet du jour. Ce planning est une proposition d’entraînement, pas une prédiction du futur sujet.

## Commandes depuis le terminal intégré de VS Code

```powershell
python --version
python -m unittest discover -s tests -v
git status
git diff
```

Après avoir créé un dépôt vide sur GitHub, connecter et envoyer le dépôt local (remplacer l’URL par celle fournie par GitHub) :

```powershell
git init -b main
git add .
git commit -m "Initialise le dépôt d'entraînement DEEPER"
git remote add origin https://github.com/TON-COMPTE/TON-DEPOT.git
git push -u origin main
```

Pour les poussées suivantes :

```powershell
git add .
git commit -m "Complète les exercices de récursivité"
git push
```

Si le dossier est déjà un dépôt Git, ne relance pas `git init` : configure seulement le remote si nécessaire.

## Astuces de débogage

- Trace à la main un petit appel (par exemple `depth_sum(3)` ou `oxygen(4)`).
- Teste les bornes : `0`, `1`, une petite valeur positive et une valeur négative si elle doit être rejetée.
- Pour les chiffres, utilise `n % 10` pour extraire le dernier chiffre et `n // 10` pour l’enlever; pour les négatifs, normalise le signe sans `abs()`.
- Pour Hanoi, compare exactement les lignes imprimées, y compris les tirets et les espaces.
- Ackermann croît très vite : reste sur les petits exemples du sujet.

## Particularité du vrai examen EPITA

Le PDF indique que, dans le dépôt fourni pendant l’examen, il faut utiliser la commande `submission` pour enregistrer une version notée. Il interdit alors les commits et tags manuels et indique une limite de deux tags par minute. Cette commande n’est pas incluse dans ce dépôt d’exercice personnel : suis les instructions du dépôt officiel le jour de l’épreuve.
