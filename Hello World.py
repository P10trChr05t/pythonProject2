# # # # # # # # # # # # # # # # print('Hello World!')
# # # # # # # # # # # # # # # # i = 2
# # # # # # # # # # # # # # # # print(type(i))
# # # # # # # # # # # # # # # # f = 2.71828
# # # # # # # # # # # # # # # # print(type(f))
# # # # # # # # # # # # # # # # c = 0.5 + 1j
# # # # # # # # # # # # # # # # print(type(c))
# # # # # # # # # # # # # # # # print(float(i), int(f), c)
# # # # # # # # # # # # # # # # a = 2 > 1
# # # # # # # # # # # # # # # # print(a)
# # # # # # # # # # # # # # # # print(type(a))
# # # # # # # # # # # # # # # # b = 2.71828 > 3
# # # # # # # # # # # # # # # # print(b)
# # # # # # # # # # # # # # # # print(type(b))
# # # # # # # # # # # # # # # # znak = "A"
# # # # # # # # # # # # # # # # print(znak)
# # # # # # # # # # # # # # # # print(type(znak))
# # # # # # # # # # # # # # # # napis = "Ala ma kota"
# # # # # # # # # # # # # # # # print(napis[0])
# # # # # # # # # # # # # # # # print(type(napis[0]))
# # # # # # # # # # # # # # # # print(napis[-1])
# # # # # # # # # # # # # # # # print(napis[-3:-1])
# # # # # # # # # # # # # # # # print(napis[::1])
# # # # # # # # # # # # # # # # print(napis[::2])
# # # # # # # # # # # # # # # # print(type(napis[::2]))
# # # # # # # # # # # # # # # # napis = "Ala ma koty"
# # # # # # # # # # # # # # # # print(napis)
# # # # # # # # # # # # # # # # napis = "Ala ma kota a kot ma psa"
# # # # # # # # # # # # # # # # liczba_całkowita = 2
# # # # # # # # # # # # # # # # print(napis + str(liczba_całkowita))
# # # # # # # # # # # # # # # # str1 = "DataTypes"
# # # # # # # # # # # # # # # # a = int(len(str1)/2)
# # # # # # # # # # # # # # # # print(a)
# # # # # # # # # # # # # # # # str1[a-1:a+2]
# # # # # # # # # # # # # # # # print(str1[a-1:a+2])
# # # # # # # # # # # # # # # # str2="Fullstack"
# # # # # # # # # # # # # # # # b=int(len(str2)/2)
# # # # # # # # # # # # # # # # print(b)
# # # # # # # # # # # # # # # # print(str2[b-1:b+2])
# # # # # # # # # # # # # # # s1 = "FullStack"
# # # # # # # # # # # # # # # s2 = "Python"
# # # # # # # # # # # # # # # a = int(len(s1)/2)
# # # # # # # # # # # # # # # print(a)
# # # # # # # # # # # # # # # b = int(len(s2)/2)
# # # # # # # # # # # # # # # print(s1[a-4:a] + s2 + s1[a:])
# # # # # # # # # # # # # # s1 = "America"
# # # # # # # # # # # # # # s2 = "Japan"
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # a1=s1[0]
# # # # # # # # # # # # # # a2=s2[0]
# # # # # # # # # # # # # # a3=s1[int(len(s1)/2)]
# # # # # # # # # # # # # # a4=s2[int(len(s2)/2)]
# # # # # # # # # # # # # # a5=s1[-1]
# # # # # # # # # # # # # # a6=s2[-1]
# # # # # # # # # # # # # #
# # # # # # # # # # # # # # print(a1+a2+a3+a4+a5+a6)
# # # # # # # # # # # # #
# # # # # # # # # # # # # a = "Python"
# # # # # # # # # # # # # print(a[::-2])
# # # # # # # # # # # # #
# # # # # # # # # # # # Jan = ("Jan", "Kowalski",33)
# # # # # # # # # # # # Janina = ("Janina", "Nowak", (21, 12, 1978), 'K')
# # # # # # # # # # # # #tuple
# # # # # # # # # # #
# # # # # # # # # # # lista = [1, 2, 3, 4, -5, 6, -10]
# # # # # # # # # # # print(lista)
# # # # # # # # # # # print(type(lista))
# # # # # # # # # # #
# # # # # # # # # # # liczby = [0.1, 0.2, 0.3, 4.5, 6.7]
# # # # # # # # # # #
# # # # # # # # # # # imiona = ['Ala', 'Zygmunt', 'Piotr']
# # # # # # # # # # #
# # # # # # # # # # lista = [1, "Berta", 3, 4, -5, "kot", -10.75, 3.14]
# # # # # # # # # # # print(lista[1:6])
# # # # # # # # # # # print(lista[2:6:2])
# # # # # # # # # # #
# # # # # # # # # # # print(lista[:4])
# # # # # # # # # # #
# # # # # # # # # # # print(lista[-4:-1])
# # # # # # # # # #
# # # # # # # # # # print(lista[::-1])
# # # # # # # # # lista = [1, "Berta", 3, 4, -5, "kot", -10.75, 3.14]
# # # # # # # # # print(lista)
# # # # # # # # #
# # # # # # # # # lista = [2, 3, 5, 7, 9]
# # # # # # # # # print(lista)
# # # # # # # # #
# # # # # # # # # lista[2:4] = ["pies", "a", "2", "xd"]
# # # # # # # # #
# # # # # # # # # print(lista)
# # # # # # # # #
# # # # # # # # lista = [1, "Berta", 3, 4, -5, "kot", -10.75, 3.14]
# # # # # # # #
# # # # # # # # lista.append("zebra")
# # # # # # # # print(lista)
# # # # # # # #
# # # # # # # lista = [1, "Berta", 3, 4, -5, "kot", -10.75, 3.14]
# # # # # # # lista.insert(2, "zebra")
# # # # # # # print(lista)
# # # # # # list = ["Kamil", "Paweł", "Kasia", "Janek", "Izabela", "Jakub", "Janusz", "Julia", "Kacper", "Karolina", "Marta", "Piotr"]
# # # # # #
# # # # # # a = sorted(list)
# # # # # # print(a)
# # # # # #
# # # # # # list.sort()
# # # # # # print(list)
# # # # # # #
# # # # # # # print(len(list))
# # # # # #
# # # # # # slownik = {"ala": "kot", "ola": 1, "pyton": True} ????
# # # # # #
# # # # # # print(slownik)
# # # # #
# # # # # tel = {} # pusty słownik
# # # # # print(tel)
# # # # #
# # # # # tel = {'Maja': 500456, 'Jasio': 343455}
# # # # # print(tel)
# # # # #
# # # # # tel['Ola'] = 3024127
# # # # # print(tel)
# # # # #
# # # # # del tel['Maja']
# # # # # print(tel)
# # # # #
# # # # tel = dict([('Jan', 4139277), ('Kazimierz', 4126327)])
# # # #
# # # # print(tel)
# # # # c = {x: x**2 for x in (2, 4, 6)}
# # # # print(c)
# # # #
# # # zbior = {"ala", "kot", 1, 2.89}
# # # print(zbior)
# # #
# # # a = int(input("podaj 1. liczbę: "))
# # # b = int(input("podaj 2. liczbę: "))
# # # print(a/b)
# # # print(a%b)
# # # print(a//b)
# # #
# # #
# # x = 5
# # y = 5
# #
# # if x>3 or y%2==0:
# #     print("co najmniej jeden warunek jest spełniony")
# # if x<=3 and y%2!=0:
# #     print("żaden warunek nie jest spełniony")
# #
# #
# #
# x = False
# if not x:
#     print("warunek spełniony")
# x=5
# print(x>3 and x<10)
# x=10
# print(x>4 or x<3)


# x=5
# print(not(x>3 and x<10))

# nice = True
# personality = ("wredny", "miły")[nice]
# print(personality)
#

# string = 'Python'
# for kupa in string:
#     print('litera:', kupa)
#

# warzywa = ['kalafior', 'marchew', 'kapusta']
# for warzywo in warzywa:
#     print("warzywo:", warzywo)

# lista = ['Janek', 'Code Brainersa', 'Jakuba', 'Izabela', 'Janusz', 'Kacper', 'Karolina', 'Piotr', 'Julia', 'Szymon', 'Janusz',  'Kamil','Pawel', 'Marta', 'Kasia']
#
# lista.sort()
#
# print(lista)
#
# kobiety = 0
#
# for imie in lista:
#     if imie[-1] == 'a':
#         kobiety += 1
#
# print(kobiety)


# for i in range(2, 11, 2):
#     print(i, end=',    ')


# print(range(2, 11, 2)) #to nie działa
#
# lista = list(range(2, 11, 2))
# print(lista)

# for i in range(10):
#     print(i)
# else:
#     print("Gotowe!")



# lines = list()
# print('Wprowadź tekst po linijce.')
# print('Żenu zakończyć wprowadź pustą linię.')
# line = input('Następna linijka: ')
# while line != '':
#     lines.append(line)
#     line = input('Następna linijka: ')

# for num in range(1, 20):
#     if not num % 2:  # num % 2 == 0
#         print('Kolejna liczba parzysta:', num)
#         continue
#     print('Kolejna liczba:', num)
#
# x = int(input("podaj liczbę: "))
# y = int(input("podaj liczbę: "))
#
# if x < y:
#     z = x
# else:
#     z = y
# for i in range(1,z+1):
#     if x % i == 0 and y % i == 0:
#         print("Wspólny dzielnik: ", i)
#

# NWD

# x = int(input("podaj liczbę: "))
# y = int(input("podaj liczbę: "))
#
# if x < y:
#     z = x
# else:
#     z = y
# for i in range(z, 0, -1):
#     if x % i == 0 and y % i == 0:
#         print("Wspólny dzielnik: ", i)
#         break


