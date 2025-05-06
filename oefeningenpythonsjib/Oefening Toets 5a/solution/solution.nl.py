# Inlezen van de benodigde waarde:
# --------------------------------

N = int(input("Voer een natuurlijk getal in: "))

# While lus (inclusief printen):
# ------------------------------
x = 1

while x**3 <= N:
    print(x**3)
    x = x + 1
