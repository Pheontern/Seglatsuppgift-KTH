# #135 Segling, p-uppgift

## Initieringsfil
Matrisen med information om havet läses in från en initieringsfil med varje rutas värde i ordning. \
Format: (vindfart (m/s)/riktning (grader)).\
Värdena ska separeras antingen med nya rader eller mellanslag. \
Rader som börjar med ett # ignoreras (kommentarer).

## GUI-design
Start- och slutkoordinaterna väljs genom att klicka på rutorna. (startruta grön och slutruta röd?)\
Vindhastighet indikeras med en pil och ett värde i varje ruta. \
\
Startknapp samt resultatruta som skriver tiden för den optimala seglatsen.\
Start kan enbart klickas om start- och slutrutor markerats.

## Programstruktur

Ska börja med att initiera en 2D-array med alla rutobjekt med korrekta egenskaper.

### Klass som representerar en rutas egenskaper:

- Ska ta in värden för vindfart och -riktning genom konstruktorn.

#### Generell vindberäkningsfunktion

- Beräknar och returnerar tiden det tar för båten att röra sig i en viss riktning (parameter) i rutan.

#### Individuella vindfunktioner
- Alla individuella vindfunktioner beroende på båtens rörelseriktning ska vara definierade här.

### Klass som representerar båten: 

Innehåller ett attribut för nuvarande minsta ackumulerade tid, modifieras av move-funktionen.

#### Innehåller en rekursiv Move-funktion

Den ska jobba inåt och testa alla möjliga riktningar för båtens rörelse ända tills den inte kommer längre.\
Kanske måste innehålla en for loop för att gå igenom alla individuella riktningar att åka åt.\
\
Ska returnera ett objekt av nästa ruta båten hamnar i samt ackumulerad tid och en lista med tidigare besökta rutobjekt.\
\
Alternativt felmeddelande/basfall om riktningen inte fungerar.\
Om båten nått sitt mål annat basfall och modifierar båtattributet minimal ackumulerad tid om den är mindre en den nya.\
Denna ska alltså vara rekursiv.



## Allmänna anteckningar
En rutsida är 1 meter. 
En förflyttning diagonalt är roten ur 2 meter lång.