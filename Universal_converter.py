#Convertitore universale
#copyright Simone sabatti 2022
print("\n")
print("Copyright: September 2022 | Simons787 \n")
print("Choose your language: \n")
opzione_1 = int(input(" 1 - For English \n 2 - For Italian \n"))

if opzione_1 == 1:
    print("Hello ! \n")
    print("Welcome to the Python Universal Converter \n")
    print("Choose your conversion\n")
    print (" Select 1 if you want to convert kilometers in miles \n Select 2 if you want to convert kilos in libras \n Select 3 if you want to convert Dollars in Euros \n")

    opzione_2 = int(input("Choose your instruction \n"))

    if opzione_2 == 1:
        print("\n")
        print("Let's convert kilometers in Miles \n")
        kilometri = float(input("Insert the numbers of kilometers \n"))
        miglia = kilometri * 0.621371
        print(kilometri, "Kilometers are respectively ",miglia, "Miles")
    elif opzione_2 == 2:
        print("\n")
        print("Let's convert kilos in libres \n")
        kili = float(input("Insert number of kilos \n"))
        libbre = kili * 2.20462
        print(kili, "Kilos are respectively ",libbre, "Libras")
    elif opzione_2 == 3:
        print("\n")
        print(" Let's convert Dollars in Euros")
        dollari = float(input("Insert the amount of Dollars \n"))
        euro = dollari * 1.03
        print(dollari, "Dollars are respectively ",euro, "Euros")
    else:
        print("Choose one of the three options")

elif opzione_1 == 2:
    print("Ciao ! \n")
    print("Benvenuto nel convertitore universale in Python \n")
    print("Premi il numero corrispondente alla conversione che vuoi fare\n")
    print (" Premi 1 se vuoi Convertire i kilometri in miglia \n Premi 2 se vuoi Convertire i kili in libbre \n premi 3 se vuoi Convertire gli euro in dollari \n")

    opzione_2 = int(input("Scrivi il numero dell'istruzione da eseguire \n"))

    if opzione_2 == 1:
        print("\n")
        print("Convertiamo i kilometri in miglia \n")
        kilometri = float(input("Inserisci il numero di kilometri \n"))
        miglia = kilometri * 0.621371
        print(kilometri, "Kilometri Sono rispettivamente ",miglia, "Miglia")
    elif opzione_2 == 2:
        print("\n")
        print(" Convertiamo i kili in libbre")
        kili = float(input("Inserisci il numero di kili \n"))
        libbre = kili * 2.20462
        print(kili, "kili Sono rispettivamente ",libbre, "Libbre")
    elif opzione_2 == 3:
        print("\n")
        print(" Convertiamo i Dollari in Euero ")
        dollari = float(input("Inserisci l' ammontare di Dollari \n"))
        euro = dollari * 1.03
        print(dollari, "Dollari Sono rispettivamente ",euro, "Euro")
    else:
        print("Scegli una delle tre opzioni disponibili")

else:
    print(" Choose Option 1 or Option 2 \n Scegli l' Opzione 1 o l' Opzione 2 \n")