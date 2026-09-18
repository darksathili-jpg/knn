"""KNN sans bibliothèque de machine learning — Première NSI.

Compléter les TODO puis exécuter ce fichier.
Précondition : 1 <= k <= len(donnees)
"""

from math import sqrt

DONNEES = [
    {"x": 16, "y": 72, "classe": "cyan"},
    {"x": 25, "y": 81, "classe": "cyan"},
    {"x": 31, "y": 65, "classe": "cyan"},
    {"x": 38, "y": 77, "classe": "cyan"},
    {"x": 63, "y": 30, "classe": "ambre"},
    {"x": 72, "y": 42, "classe": "ambre"},
    {"x": 78, "y": 24, "classe": "ambre"},
    {"x": 66, "y": 54, "classe": "ambre"},
]

def distance(a, b):
    """Renvoie la distance euclidienne entre deux points."""
    return sqrt(
        (a["x"] - b["x"]) ** TODO_1
        + (a["y"] - b["y"]) ** TODO_2
    )

def knn(donnees, cible, k):
    """Prédit 'cyan', 'ambre' ou 'égalité' avec un vote uniforme."""
    assert 1 <= k <= len(donnees)
    distances = []

    for point in donnees:
        d = distance(point, cible)
        distances.append((d, point["classe"]))

    distances.TODO_3()

    votes = {"cyan": 0, "ambre": 0}

    for i in range(TODO_4):
        classe = distances[i][TODO_5]
        votes[classe] = votes[classe] + 1

    if votes["cyan"] > votes["ambre"]:
        return "cyan"
    elif votes["ambre"] > votes["cyan"]:
        return "ambre"
    return "égalité"


# Jeux de tests à utiliser après avoir remplacé les cinq TODO.
# assert distance({"x": 0, "y": 0}, {"x": 3, "y": 4}) == 5
# assert knn(DONNEES, {"x": 30, "y": 70}, 3) == "cyan"
# assert knn(DONNEES, {"x": 70, "y": 35}, 3) == "ambre"
