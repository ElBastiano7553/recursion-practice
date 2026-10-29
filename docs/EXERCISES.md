# Spécifications des exercices

Les signatures doivent rester exactement identiques. Tous les exercices doivent être résolus par récursion, sans `for`, `while`, compréhension, `break`, `continue` ou opérateur `**`. Les interdictions spécifiques ci-dessous s’ajoutent à ces règles. Une entrée hors domaine doit lever `ValueError`.

## Fundamentals — `deeper/descent/`

| Fichier | Fonction | Comportement | Cas particuliers / interdictions |
|---|---|---|---|
| `depth_gauge.py` | `depth_sum(n: int) -> int` | Somme des entiers de 0 à n inclus. | `n < 0` : `ValueError`. |
| `oxygen.py` | `oxygen(n: int) -> int` | Factorielle `n!`. | `0! = 1`; `n < 0` : `ValueError`; pas de `math.factorial`. |
| `signal.py` | `signal_power(x: int, n: int) -> float` | Calcul récursif de `x` élevé à `n`. | `x == 0 and n == 0` : `ValueError`; exposant négatif = réciproque de la puissance positive; pas de `**`. |
| `echoes.py` | `echo(n: int) -> int` | Terme n de Fibonacci : 0, 1, 1, 2, 3, 5… | `n < 0` : `ValueError`; le cas récursif doit faire deux appels récursifs. |
| `beacon.py` | `countdown_beacon(n: int) -> str` | Chaîne `n,n-1,...,1,0`. | `n < 0` : `ValueError`; `str()` autorisé; pas de `range` ni `reversed`. |

## Proficiencies — `deeper/core/`

| Fichier | Fonction | Comportement | Cas particuliers / interdictions |
|---|---|---|---|
| `layers.py` | `layer_sum(n: int) -> int` | Somme des chiffres décimaux. | Les négatifs sont traités comme leur valeur positive; pas de `abs()`. |
| `deepest.py` | `deepest_digit(n: int) -> int` | Plus grand chiffre décimal. | Les négatifs sont traités comme leur valeur positive; pas de `abs()` ni `max()`. |
| `gates.py` | `gate_gcd(a: int, b: int) -> int` | PGCD positif par l’algorithme d’Euclide. | Signes quelconques; pas de `abs()` ni `math.gcd`. |
| `binary.py` | `to_binary(n: int) -> str` | Écriture binaire sous forme de chaîne. | `0` donne `"0"`; `n < 0` : `ValueError`; pas de `bin()` ni `format()`. |
| `abyss.py` | `ackermann(m: int, n: int) -> int` | Fonction d’Ackermann : `A(0,n)=n+1`; `A(m,0)=A(m-1,1)`; sinon `A(m,n)=A(m-1,A(m,n-1))`. | `m < 0` ou `n < 0` : `ValueError`; tester avec de petites entrées. |
| `tower.py` | `hanoi(n: int, start: str, end: str, intermediate: str) -> None` | Affiche les déplacements minimaux des tours de Hanoï. | `n < 0` : `ValueError`; `n == 0` n’affiche rien. Chaque déplacement : `disk {n}: {from} -> {to}`. |

## Méthode de récursion à vérifier

Pour chaque fonction, écris avant de coder :

1. **Cas de base** : quelle condition donne la réponse sans rappeler la fonction ?
2. **Cas récursif** : quel appel plus petit résout le sous-problème ?
3. **Progression** : pourquoi chaque appel se rapproche-t-il du cas de base ?
4. **Domaine** : quelles entrées doivent déclencher `ValueError` ?
5. **Contraintes** : quelles fonctions, opérateurs ou constructions sont interdits ?

Ces consignes résument le PDF d’entraînement fourni. Le sujet officiel et ses consignes restent prioritaires en examen.
