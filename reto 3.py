from random import randint
from re import I

dado1=randint(1,6)
dado2=randint(1,6)

print(dado1,dado2)
if dado1==1 and dado2==1:
    print("ganaste")
if dado1==1 and dado2==2 or dado1==2 and dado2==1:
    print("ganaste")
if dado1==5 and dado2==6 or dado1==6 and dado2==5:
    print("ganaste")
if dado1==6 and dado2==6 or dado1==1 and dado2==1:
    print("ganaste")
if dado1==2 and dado2==5 or dado1==5 and dado2==2 or dado1==4 and dado2==3 or dado1==3 and dado2==4 or dado1==6 and dado2==1 or dado1==1 and dado2==6:
    print("ganaste")
else:
    print("perdiste")