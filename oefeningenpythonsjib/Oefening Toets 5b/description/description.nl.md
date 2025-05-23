## Oefening Toets 5b
Jeroen heeft heel wat gewerkt tijdens de vakanties en weekends en besluit de 2000 euro die hij verdiende op zijn spaarboekje te plaatsen. Hij wil berekenen hoelang het duurt vooraleer hij 2500 euro op zijn rekening heeft aan een samengestelde interestvoet van 2%.

#### Gevraagd

Schrijf een programma dat berekent hoeveel jaar het duurt vooraleer hij 2500 euro heeft. Het programma geeft het jaar weer en het gespaarde bedrag dat jaar. 
* Het programma vraagt achter het basisbedrag.(gespaarde bedrag) 
* Het programma vraagt ook achter de samengestelde interestvoet.

#### Voorbeeld
Stel dat Jeroen € 2000 op zijn spaarboekje stort. Hij spaart aan een samengestelde interestvoet van 2 % op jaarbasis. Dan heeft hij elk jaar meer geld op zijn rekening:

```
1 2040
2 2081
3 2122
4 2165
5 2208
6 2252
7 2297
8 2343
9 2390
10 2438
11 2487
12 2536
```
Na het 1e jaar heeft hij dus 2040 euro op zijn rekening.
Na het 2e jaar 2081 ...

{: .callout.callout-info}
> #### Tip
> De formule om het totale bedrag jaarlijks te berekenen: 
* basisbedrag = basisbedrag x (100 + interest)/100 

* 2000 x (100 + 2)/100 = 2000 x 1.02 = 2040

{: .callout.callout-info}
> #### Tip
> Als je kommagetallen wil omzetten in gehele getallen gebruik je de functie **round()**. 

Bv round(5.3) = 5
