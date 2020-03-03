def sum(num1, num2):
  sum = num1+num2
  print(f"{num1}+{num2}={sum}\n")

def subtraction(num1, num2):
  subtraction=num1-num2
  print(f"{num1}-{num2}={subtraction}\n")

def multiply(num1, num2):
  multiply=num1*num2
  print(f"{num1}*{num2}={multiply}\n")

def devide(num1, num2):
  devide=num1/num2
  print(f"{num1}/{num2}={devide}\n")




inputkeuze1=0

while inputkeuze1 !=3 :
  print("menu")
  print("1) Wet van Ohm")
  print("2) Simpele berekeningen")
  print("3) Afsluiten\n")
  inputkeuze1 = int(input("wat is je keuze: "))

 

  if inputkeuze1 == 1:
      inputkeuze2 = 0
      while inputkeuze2 != 4:
        print("\nmenu wet van ohm")
        print("1) Weerstand")
        print("2) Stroom")
        print("3) Spanning")
        print("4) Afsluiten\n")
        inputkeuze2=int(input("Wat is je keuze: "))

        if inputkeuze2 == 1:
          Spanning= int(input("\nWat is je Spanning? "))
          Stroom= int(input("Wat is je Stroom? \n"))
          devide(Spanning, Stroom)

        elif inputkeuze2 == 2:
          Weerstand= int(input("\nWat is je weerstand? "))
          Spanning= int(input("Wat is je Spanning? \n"))
          devide(Spanning, Weerstand)

        elif inputkeuze2 == 3:
          Weerstand= int(input("\nWat is je weerstand? "))
          Stroom= int(input("Wat is je Stroom? \n"))
          multiply(Weerstand, Stroom)

        elif inputkeuze2 == 4:
          print("Terug naar het beginscherm gegaan \n")
          break
          

  elif inputkeuze1 == 2:
      inputkeuze3 = 0
      while inputkeuze3 != 5:
        print("Simpele berekeningen\n")
        print("1) Optellen")
        print("2) Aftrekken")
        print("3) Vermenigvuldigen")
        print("4) Delen")
        print("5) Afsluiten\n")
        inputkeuze3=int(input("Wat is je keuze: "))

        if inputkeuze3 == 1:
          Guess1=int(input("\nGeef een getal: "))
          Guess2=int(input("Geef een getal: "))
          sum(Guess1, Guess2)

        elif inputkeuze3 == 2:
          Guess1=int(input("\nGeef een getal: "))
          Guess2=int(input("Geef een getal: "))
          subtraction(Guess1, Guess2)

        elif inputkeuze3 == 3:
          Guess1=int(input("\nGeef een getal: "))
          Guess2=int(input("Geef een getal: "))
          multiply(Guess1, Guess2)

        elif inputkeuze3 == 4:
          Guess1=int(input("\nGeef een getal: "))
          Guess2=int(input("Geef een getal: "))
          devide(Guess1, Guess2)

        elif inputkeuze3 == 5:
          print("Terug naar het beginscherm gegaan\n")
          break


 

  elif inputkeuze1 == 3:
    break
    print("end of program")

else:
  print("end of program")
