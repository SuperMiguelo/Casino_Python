#!/usr/bin/env python
# coding: utf-8

# In[78]:


from random import randrange
from math import ceil

Thune = 50
ThuneInt = int(Thune)
nbRandom = randrange(49)

liste =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]

def TestPair():
    for numéro in liste:
        if numéro % 2 == 0:
            print ("Noire %i" % numéro)
        else: 
            print ("Rouge %i" % numéro)

print('Choisir un nombre entre 0 et 49')
NombreChoisi = input()


print('Combien voulez-vous miser en dollars ?')
ThuneMisé = input("$")
ThuneMiséInt = int(ThuneMisé)

print("La boule magique s'est arrêtée sur le nombre :", nbRandom)


a = int(NombreChoisi)
b = randrange

if a == b:
    ThuneInt = ThuneInt - ThuneMiséInt + (ThuneInt * 3)
    print("GG c'est le bon nombre, vous avez gagné ", ThuneMiséInt * 3 ,"$" )
    
elif (a % 2 == 0 and nbRandom % 2 == 0) or (a % 2 != 0 and nbRandom % 2 != 0 ) :
    ThuneInt = ThuneInt - ThuneMiséInt + (ThuneMiséInt/2)
    ThuneMiséInt / 2
    ThuneMiséInt = ceil(ThuneMiséInt)
    print("Perdu haha noobi, il vous reste ",ThuneMiséInt, "$" )
    
else:
    ThuneInt = ThuneInt - ThuneMiséInt
    print("Vous avez perdu toute votre thune")

ThuneInt = ceil(ThuneInt)


# In[ ]:




