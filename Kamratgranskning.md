## Klasser och struktur:
Central klass i form av postkontoret samt mindre klass som definierar varje kunds egenskaper. Väl strukturerat. Hade kunnat separera de grafiska funktionerna i egna klasser så att de är lätta att hålla isär från själva programmet. Men det är långt ifrån nödvändigt för att koden ska vara lätt att förstå.

Följer anvisningarna, all kod ligger i klasser, metoder och funktioner.
Storlek på komponenter:
Ingen onödigt stor klass eller metod/funktion.
Menu-funktionen hade kanske kunnat separera ut olika delar av menyn i egna funktioner för att hålla bättre reda och enklare kunna ta bort olika element.

## Kommentarer:
Väldigt välformulerade docstrings på nästan alla funktioner, metoder och klasser.
Det saknas dock på “update_gui” samt str-metoden hos “customer”. De är dock enkla och självförklarande. 

För is_positive-funktionerna tycker jag att kommentarerna är lite överflödiga. Men eftersom vi har krav på att alla funktioner ska dokumenteras så ser jag inget bättre sätt att göra det på.

Multiline docstrings ska enligt pep8 ha sina 3 sista citattecken på en egen rad.

För enradskommentaren på rad 170 exempelvis följs inte heller pep8 helt korrekt. Det ska egentligen vara minst två mellanslag före samt ett efter hashtaggen.

## Globalitet:
Inga globala variabler.

## Kodupprepning:
Hittar ingen strikt onödig kodupprepning.
Funktionen som skapar inmatningsrutor och labels är dock ett bra exempel som minskar kodupprepning och gör programmet mer flexibelt.

## Hårdkodning:
Programmet accepterar förändring av alla kritiska variabler för simulationen och även det grafiska gränssnittet kan ganska enkelt förändras som nämnt i föregående punkt.

## Utskrifter/Gränssnitt:
Lätt att förstå, all information som krävs för att hantera simulationen finns med.

## Namngivning (litteraler):
I allmänhet väldigt bra. Man hade kunnat byta namn på “insert_text” till ex. “append text” eftersom det är enbart det den gör. Den vanliga metoden på widgeten heter ju redan insert så det skapar mindre oklarheter. 
