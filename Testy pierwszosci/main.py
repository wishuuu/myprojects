import time
from os import system
import functions

while (1):
    print('Jaka operacje chcesz wykonac?\n1 - obliczanie pierwszosci\n2 - rysowanie wykresu relacji podzielnosci')
    c = input()
    if c == '1':
        testy = [False, False, False, False]
        while c != '5':
            system('cls')
            print('Wybierz testy ktore chcesz wykonac:')
            print('1 - test naiwny(n-1) ' + str(testy[0]))
            print('2 - test naiwny(sqrt(n)) '  + str(testy[1]))
            print('3 - test oparty o Twierdzenie Wilsona '  + str(testy[2]))
            print('4 - test oparty o Twierdzenie Fermata '  + str(testy[3]))
            print('5 - wykonaj testy')
            c = input()
            if c in ['1','2','3','4']:
                testy[int(c)-1] = not testy[int(c)-1]
        system('cls')
        print('Podaj liczbe ktora chcesz rozpatrzyc:')
        n = int(input())
        results = []
        times = []
        if testy[0]:
            start = time.time()
            results.append(functions.naive1(n))
            end = time.time()
            times.append([end-start])
        if testy[1]:
            start = time.time()
            results.append(functions.naive2(n))
            end = time.time()
            times.append([end-start])
        if testy[2]:
            start = time.time()
            try:
                results.append(functions.wilson(n))
            except OverflowError:
                print("Zbyt duża liczba aby przeprowadzić test oparty o Twierdzenie Wilsona")
            end = time.time()
            times.append([end-start])
        if testy[3]:
            start = time.time()
            results.append(functions.fermat(n))
            end = time.time()
            times.append([end-start])

        done = [i for i in range(4) if testy[i]]

        for num, i in enumerate(done):
            if i == 0:
                print("Test naiwny(n-1):\t" + str(results[num]) + '\t' + str(times[num]) + "s")
            if i == 1:
                print("Test naiwny(sqrt(n)):\t" + str(results[num]) + '\t' + str(times[num]) + "s")
            if i == 2:
                print("Test Wilsona:\t\t" + str(results[num]) + '\t' + str(times[num]) + "s")
            if i == 3:
                print("Test Fermata:\t\t" + str(results[num]) + '\t' + str(times[num]) + "s")
        system('pause')
    elif c == '2':
        system('cls')
        print('Podaj przedzial argumentow rysowanej relacji:')
        x = int(input())
        print('Podaj przedzial wartosci rysowanej relacji:')
        y = int(input())
        functions.show_chart(x,y)
    else:
        system('cls')
        break
