# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 20:21:56 2023

@author: User
"""

friends=[]
friends.append("Azat")
friends.append("Abat")
friends.append("Nurlibek")
friends.append("Ajiniyaz")
#print(friends)
friends.remove("Azat")
#print(friends)
friends.append("Rinat")
friends.append("Nurdawlet")
friends.append("Shuxrat")
friends.append("Miyras")
friends.append("Ruslan")
friends.insert(2,"Kuat")
print(friends)

#Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida 
#mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
mehmonlar = []
mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(-1))
mehmonlar.append(friends.pop(0))
print("\nKelgan mehmonlar: ", mehmonlar)