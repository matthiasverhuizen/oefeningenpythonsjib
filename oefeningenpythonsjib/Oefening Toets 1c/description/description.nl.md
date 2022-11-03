**Programma Discriminant**

Schrijf een programma waarmee je de nulwaarden bepaalt van een tweedegraadsfunctie. 
Een vaak gebruikte methode in de wiskunde is deze van de discriminant.

Een tweedegraadsfunctie heeft de vorm: y = ax2+bx+c
Waarbij de letters a, b en c een bepaald cijfer krijgen toegekend.

Deze waarden voor a, b en c dien je zelf in te geven wanneer het programma hierom vraagt. 
Vervolgens berekent het programma de waarde van de discriminant (D = b² - 4ac).

Daarna berekent het programma de waarde van de variabelen:
 X1 = (-b-sqrt(D))/ (2a) 
 X2 = (-b+sqrt(D)) / (2a)

Als invoer werken we enkel met gehele getallen.
Voorbeelden voor het programma:
Voorbeeld 1
De invoer bedraagt:
•	a = 2
•	b = 3
•	c = 1
De uitvoer van je programma moeten onderstaande antwoordzinnen zijn:
De discriminant D bedraagt 1.
De eerste nulwaarde bevindt zich op -0.5.
De tweede nulwaarde bevindt zich op -1.0.
Voorbeeld 2
Dit zelfde programma zou ook moeten werken voor onderstaande invoer:
•	a = 1
•	b = 8
•	c = 7
En onderstaande uitvoerzinnen:
De discriminant D bedraagt 36.
De eerste nulwaarde bevindt zich op -1.0.
De tweede nulwaarde bevindt zich op -7.0.

TIP
Voor een wortel te nemen maak je gebruik van de functie : sqrt()
Voor het argument van deze functie geef je de variabele of getal in waarvan je de wortel wenst te nemen.
OPGELET
Voor deze functie te kunnen gebruiken moet deze geïmporteerd worden in Replit. Dit doe je door je programma te starten met de onderstaande programmaregel:
•	from math import sqrt
