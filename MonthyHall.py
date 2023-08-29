#Laziness**2
#Laziness < 0
#Positive Laziness is no longer called laziness
from matplotlib import pyplot as plot
from numpy.random import randint
Times = 10000
print("Without Changing")
Wins = 0
Lose = 0
Wl = []
for i in range(Times):
    numb = randint(1, 4)
    guess = randint(1, 4)
    if numb == guess:
        Wins += 1
    else:
        Lose += 1
    Wl.append(Wins)
print(Wins, "Wins")
print(Lose, "Losses")
print("Times: ", Times)
print("%",100 * (Wins / Times))
print("_________________________________________________")
print("With Changing")
Victory = 0
Defeat = 0
Vl = []
for i in range(Times):
    numb = randint(1, 4)
    guess = randint(1, 4)
    none = [1, 2, 3]
    for j in range(2, -1, -1):
        if none[j] - numb == 0 or none[j] - guess == 0:
            none.pop(j)
    none = int(none[0])
    FinallAnswer = 1
    while FinallAnswer - none == 0 or FinallAnswer - guess == 0:
        FinallAnswer += 1
    if FinallAnswer == numb:
        Victory += 1
    else:
        Defeat += 1
    Vl.append(Victory)        
print(Victory, "Wins")
print(Defeat, "Losses")
print("Times", Times)
print(100 * (Victory / Times), "%")
Tl = []
WL = []
for i in range(1, Times):
    Tl.append((Vl[i] / i)*100)
    WL.append((Wl[i] / i)*100)
V = []
C = []
for i in range(1, Times):
    V.append(i*100)
    C.append((2/3)*100)
plot.plot(V, Tl, V, WL)
plot.show()
print("Made by Arvin Mallahi")
