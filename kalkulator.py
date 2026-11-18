dzialanie = input("Podaj jakie dzialanie chcesz wykonac (+,-,*,/,%):")

liczba1 = float(input("Podaj pierwsza liczbe: "))
liczba2 = float(input("Podaj druga liczbe: "))

if dzialanie == "+":
    wynik = liczba1 + liczba2
    print(round(wynik, 3))
elif dzialanie == "-":
    wynik = liczba1 - liczba2
    print(round(wynik, 3))
elif dzialanie == "*":
     wynik = liczba1 * liczba2
     print(round(wynik, 3))
elif dzialanie == "/":
    wynik = liczba1 / liczba2
    print(round(wynik, 3))
elif dzialanie == "%":
    wynik = (liczba1 / liczba2) * 100
    print(round(wynik, 3), "%")
else:
    print(f"Nie powinienes tutaj pisac : .{dzialanie} tylko */+- ")