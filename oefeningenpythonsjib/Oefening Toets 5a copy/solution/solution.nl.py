# Vraag de gebruiker om het startbedrag en de jaarlijkse interest
bedrag = int(input("Voer het startbedrag in: "))
interest = int(input("Voer de jaarlijkse interest in: "))

# Bereken het bedrag op de rekening na elk jaar
jaar = 0
while bedrag < 2500:
    bedrag *= (100 + interest) / 100
    print(1, round(bedrag))
    jaar = jaar + 1
