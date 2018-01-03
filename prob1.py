# -*- coding: utf8 -*-
import sys
import math

phrase = "le chien marche vers sa niche et trouve une limace de chine nue pleine de malice qui lui fait du charme"

liste_mot = phrase.split(" ")
print(liste_mot)
liste_classee = [''.join(sorted(list(word))) for word in liste_mot] 
print(liste_classee)
dict_mot = {}
for word in liste_mot:
    key = ''.join(sorted(list(word)))
    if dict_mot.setdefault(key, False)== False:
        dict_mot[key] = [word]
    elif word not in dict_mot[key]:
        dict_mot[key].append(word)
print(dict_mot)

list_sol = [liste for liste in dict_mot.values() if len(liste) >1]
print(list_sol)
