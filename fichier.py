#Exo Guillaume PONTANIER - Hugo FERNANDEZ

import pandas as pd

df = pd.read_csv('test.csv')

#Consigne n°2 : Garder uniquement les colonnes : Period, Data_value et Series_title_2
#On supprime tout d'abord les colonnes inutiles (et donc celles vides qui nous feraient supprimer tout le tableau à cause de leurs lignes vides pour la consigne n°1)
df = df[['Period', 'Data_value', 'Series_title_2']]

#Consigne n°3 : Filtrer les résultats en ne gardant que les résultats avec Credit, Debit et Services dans la colonne Series_title_2
df = df.query("Series_title_2 in ('Credit','Debit','Services')")

#Consigne n°1 : Supprimer toutes les lignes ayant au moins une cellule vide
#On peut enfin supprimer toutes les lignes avec une cellule vide
df = df.dropna()

#Consigne n°4 : Ajouter une colonne id, auto-incrémenté
df.insert(0, 'id', range(1, 1 + len(df)))

#Consigne n°5 : Écrire le nouveau jeu de données dans un fichier result.csv
df.to_csv('result.csv', index=False)