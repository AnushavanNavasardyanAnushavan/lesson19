import json
from typing import SupportsInt

# player1 = {
#     'name': 'Aram',
#     'age': 18,
#     'height':180,
#     'awards':['master',3,2,1]
# }
# aboutME = {
#     "name": "Anushvan",
#     "age": 23,
#     'height':175,
#     'awards':['master',3,2,1]
# } 
# player2 = {
#     'name': 'Ani',
#     'age': 14,
#     'height':178,
#     'awards':[3,2,1]
# }
# myplayers = [player1, player2, aboutME]
# with open("players.json", 'w') as file:
#     json.dump(myplayers, file)

# file = open("players.json")
# json_data = json.load(file)

# for data in json_data:
#     print(data)


# for data in json_data:
#     print('\nPlayer name is', data['name'])
#     print('Player age is', data['age'])
#     print('Player height is', data['height'])
#     print('Player awards is', data['awards'])

# aboutME = {
#     "name": "Anushvan",
#     "age": 23,
#     'height':175,
#     'awards':['master',3,2,1]
# } 


# with open("forME.json", "w") as file:
#     json.dump(aboutME, file)
# file = open("forME.json")
# res = json.load(file)
# resList = [res]
# print(resList)
# for i in resList:
#     print("name is --- ", i["name"])
#     print("Age is --- ", i["age"])
#     print(i)



# N1
# first = ['Ani', 'Jessy', 'Ben']
# second = [1,2,3]
# myDict = {}
# for i, j in zip(second, first):
#     myDict.setdefault(i, j)
# print(myDict)

# with open("players.json", 'a') as file:
#     json.dump(myDict, file)


# N3
# num = int(input("enter number ---- "))
# sum = 0
# for i in range(1, num):
#     if i % 3 == 0 or i % 5 == 0:
#         sum += i
# print(sum) 
# with open("players.json", 'a') as file:
#     json.dump(sum, file)




# N4
# strIntput = input("enter str ---")
# vowels = ['a', 'e', 'i', 'o']
# res = 0
# for i in strIntput:
#     if i in vowels:
#         res += 1
# print(res)
# with open("players.json", 'a') as file:
#     json.dump(res, file)





# N6.  NEw LisT
# def repeating(elements):
#     s = elements
#     s.sort()
#     for i in s:
#         if s.count(i) >= 2:
#             s.remove(i)
#     # print(s)
#     return s
# print(repeating([1, 2, 3, 2, 2,  5]))



# N7  HOw mucH  uppercase letters and lowercase letters.
# s  = """ Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
# Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
# when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
# It has survived not only five centuries, but also the leap into electronic typesetting, 
# remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset 
# sheets containing Lorem Ipsum passages, and more recently with desktop publishing software 
# like Aldus PageMaker including versions of Lorem Ipsum."""
# s = s.split(' ')
# print(s)

# uppercaseLetters = 0
# lowercaseLetters = 0
# for i in s:
#     if i == :
#         uppercaseLetters = s.count(s)





