# Vraag de gebruiker om het startbedrag en de jaarlijkse interest
basis = int(input("Voer het startbedrag in: "))
interest = int(input("Voer de jaarlijkse interest in: "))

# Bereken het bedrag op de rekening na elk jaar
jaar = 0
while bedrag < 2500:
    basis = basis(100 + interest) / 100
    jaar = jaar + 1
    print(jaar, round(basis))
