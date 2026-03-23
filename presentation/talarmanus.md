# Talarmanus – "Hur påverkas omloppsbanor av startvillkor?"

**Presentatör:** Axel Jönsson
**Längd:** ca 18 minuter + frågor
**Format:** 18 slides i Reveal.js med fragment-animationer

---

## Tidsbudget

| Slide | Innehåll | Tid |
|-------|----------|-----|
| 1 | Titel | 0:30 |
| 2 | Vardagskrok | 1:00 |
| 3 | Kärnfrågan | 1:00 |
| 4 | Boll-på-kulle-analogi | 1:15 |
| 5 | Gravitation | 1:00 |
| 6 | Energi avgör allt | 1:15 |
| 7 | Varför numeriska metoder | 1:00 |
| 8 | Euler vs RK4 | 1:30 |
| 9 | OrbitLab-programmet | 0:45 |
| 9b | Utvecklingsprocessen | 0:45 |
| 10 | Demo | 1:30 |
| 11 | Resultat: Elliptisk bana | 1:15 |
| 12 | Resultat: Flyktbana | 1:00 |
| 13 | Resultat: Energibevarande | 1:15 |
| 14 | Resultat: Parametersvep | 1:15 |
| 15 | Diskussion | 1:00 |
| 16 | Utmaningar | 1:00 |
| 17 | Tips | 1:00 |
| 18 | Frågor | öppen |
| **Totalt** | | **~18 min + frågor** |

---

## SLIDE 1 – Titel
**[~30 sekunder]**

Hej allihopa! Jag heter Axel Jönsson och det här är mitt gymnasiearbete.

Frågan jag ställde mig var ganska enkel: vad händer med en satellit beroende på hur snabbt och i vilken riktning man skjuter upp den? Stannar den i bana, eller flyger den iväg? För att ta reda på det byggde jag en egen simulator — och den ska ni få se idag. Min handledare har varit Fredrik Persson.

---

## SLIDE 2 – Du använde omloppsbanemekanik idag
**[~1 minut]**

Innan vi dyker ner i fysiken vill jag börja med någonting ni alla har gjort idag, eller åtminstone den här veckan. Varje gång ni öppnar Google Maps, streamar en video eller kollar vädret på telefonen så använder ni teknik som är helt beroende av omloppsbanemekanik.

**[KLICKA]** Just nu kretsar 31 GPS-satelliter runt jorden med exakt rätt hastighet. Inte ungefär rätt — exakt rätt. Det är därför er position på kartan stämmer.

**[KLICKA]** Om de går för långsamt kraschar de tillbaka mot jorden. För snabbt och de flyger iväg ut i rymden. Så hur tar man reda på vilken hastighet som är den rätta? Det är precis den frågan som fick mig att välja det här ämnet — jag ville förstå fysiken bakom det och se om jag kunde simulera det själv.

---

## SLIDE 3 – Kärnfrågan
**[~1 minut]**

Det här är den centrala frågan i hela arbetet. Vad avgör om en satellit stannar i omloppsbana, flyr ut i rymden, eller kraschar tillbaka ner?

**[KLICKA]** För att besvara den frågan byggde jag en fullständig simulator från grunden och testade 6 000 olika uppskjutningar systematiskt, med olika hastigheter och riktningar.

**[KLICKA]** Och spoiler: det visar sig att det handlar om bara två tal — hastigheten och riktningen. Men varför just de? Låt mig förklara det med en enkel bild.

---

## SLIDE 4 – Tänk dig det som en boll på en kulle
**[~1 minut 15 sekunder]**

Föreställ er att ni rullar en boll uppför en kulle.

**[KLICKA]** Ger ni bollen en svag knuff så rullar den en bit uppåt, saktar ner och kommer tillbaka. I rymdtermer är det här en elliptisk omloppsbana — satelliten går runt och kommer tillbaka till samma punkt.

**[KLICKA]** Ger ni precis rätt knuff så når bollen precis toppen av kullen och stannar där. Det här är flyktgränsen — den exakta gränshastigheten.

**[KLICKA]** Och ger ni en hård knuff så flyger bollen över toppen och fortsätter ner på andra sidan. Det är en flyktbana — satelliten lämnar jorden och kommer aldrig tillbaka.

**[KLICKA]** Gravitationen är kullen. Hastigheten är knuffen. Och det är energin som avgör vilket utfall man får. Den här analogin är faktiskt inte bara en metafor — det är matematiskt samma ekvation. Och den ekvationen ska vi titta på nu.

---

## SLIDE 5 – Gravitation: Den enda kraften
**[~1 minut]**

Så vad händer egentligen i rymden? Jo, i rymden finns inget luftmotstånd och ingen friktion. Det enda som påverkar en satellit är gravitationen som drar den mot planeten.

**[KLICKA]** Och det viktiga att förstå är att ju närmare man är, desto starkare är dragningen. Dubbelt så nära innebär fyra gånger så stark kraft. Det kallas det omvända kvadratförhållandet.

**[KLICKA]** Det uttrycks i Newtons gravitationslag: F är lika med G gånger M gånger m delat på r i kvadrat. Kraften mellan två massor, som avtar med kvadraten på avståndet. Det här är den enda ekvationen som styr hela min simulering — allt annat följer från den här enda lagen.

---

## SLIDE 6 – Energin avgör allt
**[~1 minut 15 sekunder]**

Minns bollen på kullen? Vi kan uttrycka det mer exakt med en energiformel.

**[KLICKA]** Epsilon — den specifika energin — är lika med v i kvadrat delat på två, minus my delat på r. Det första är rörelseenergin: hur snabbt man rör sig. Det andra är den potentiella energin: hur långt från planeten man är. Och my är G gånger planetens massa.

**[KLICKA]** Det fina är att tecknet på epsilon avgör utfallet helt och hållet. Om epsilon är negativt har man inte tillräckligt med energi för att fly — då får man en elliptisk omloppsbana. Om epsilon är exakt noll är man precis vid flyktgränsen. Och om epsilon är positivt så flyger man iväg för alltid.

**[KLICKA]** Och i konkreta siffror, vid 600 kilometers höjd: en cirkulär bana kräver 7 561 meter per sekund. Flykt kräver 10 693. Bara 3 000 meter per sekund skiljer en stabil bana från att försvinna ut i rymden för alltid.

---

## SLIDE 7 – Ett problem datorer måste lösa
**[~1 minut]**

Så vi känner formeln för gravitationen. Varför kan vi inte bara lösa det med papper och penna?

**[KLICKA]** För en perfekt cirkulär bana kan vi faktiskt det. Men för alla realistiska banor är det inte så enkelt. Kraften ändrar både riktning och styrka i varje punkt längs banan. Positionen beror på hastigheten, som beror på accelerationen, som i sin tur beror på positionen. Det är ett hönan-och-ägget-problem.

**[KLICKA]** Lösningen är att ta små steg framåt i tiden och beräkna om vid varje steg. Det kallas numerisk integration — datorn spårar banan steg för steg. Tänk på det som GPS-navigering: telefonen beräknar inte hela rutten på en gång, utan uppdaterar var ni är varje sekund. Numerisk integration fungerar på precis samma sätt.

---

## SLIDE 8 – Två sätt att ta dessa steg
**[~1 minut 30 sekunder]**

I mitt arbete jämför jag två numeriska metoder för att ta dessa steg framåt i tiden.

*[Peka på vänster kolumn]* Först har vi Eulers metod. Den tittar en gång på var man är, beräknar riktningen, och tar ett steg framåt. Det är som att bara kolla vädret vid midnatt och anta att det förblir likadant hela dagen.

**[KLICKA]** Problemet är att felen ackumuleras. Satelliten spiralerar sakta bort från sin rätta bana.

*[Peka på höger kolumn]* Sedan har vi Runge-Kutta 4, eller RK4. Den tittar framåt fyra gånger innan den bestämmer var nästa steg ska landa. Det är som att kolla vädret vid midnatt, klockan sex på morgonen, mitt på dagen och klockan sex på kvällen, och sedan planera sin dag utifrån det.

**[KLICKA]** Resultatet är dramatiskt noggrannare för samma stegstorlek.

**[KLICKA]** För den som är intresserad: RK4 använder fyra lutningsuppskattningar — k1 till k4 — som viktas 1:2:2:1. Det matchar en Taylorutveckling till fjärde ordningen. Men det viktiga att ta med sig? RK4 tittar framåt flera gånger, Euler bara en gång. Den enkla skillnaden gör RK4 miljarder gånger noggrannare.

---

## SLIDE 9 – Programmet OrbitLab
**[~45 sekunder]**

Så då har vi teorin på plats. Låt mig berätta om programmet jag byggde för att testa allt det här. OrbitLab är byggt i Python med Pygame för realtidsvisualisering. Det stödjer 10 olika himmelskroppar — Jorden, Mars, Jupiter med flera — med 7 eller fler fördefinierade scenarier per planet. Man kan växla mellan RK4 och Euler i realtid för att se skillnaden direkt, och programmet loggar automatiskt all data för analys efteråt.

**[KLICKA]** Låt mig visa er hur det ser ut.

---

## SLIDE 9b – Utvecklingsprocessen
**[~45 sekunder]**

Men först vill jag visa hur programmet utvecklades. Här ser ni processen steg för steg. Det började som en enkel ChatGPT-genererad matplotlib-plot — det var version 1. Sedan byggde jag om det till Pygame för realtidsvisualisering. Version 3 fick en huvudmeny och knappar. I version 4 lade jag till muskontroller och en jordsprite. Och till slut ser ni version 1.5 av OrbitLab som det ser ut idag, med procedurell planetgenerering och fullständig meny.

---

## SLIDE 10 – Demo
**[~1 minut 30 sekunder]**

*[Här spelas en inspelad video av en cirkulär omloppsbana runt jorden.]*

Här ser ni OrbitLab i aktion. Det ni ser är en cirkulär omloppsbana runt jorden. Satelliten startar på 600 kilometers höjd med exakt 7 561 meter per sekund — den cirkulära hastigheten.

*[Peka på banan]* Titta på hur banan ritas ut bakom satelliten. Den sluter sig till en perfekt cirkel. Hastigheten är konstant hela vägen runt, precis som teorin förutsäger.

*[Peka på planeten]* Jordens yta renderas procedurellt — varje planet i programmet ser annorlunda ut. Man kan zooma in och ut, följa satelliten med kameran, och byta scenario med ett knapptryck.

*[Om live-demo:] Under frågesessionen kan jag köra det här live och visa andra scenarion — till exempel flyktbanor eller jämföra Euler och RK4 i realtid.*

---

## SLIDE 11 – Resultat: Elliptisk omloppsbana
**[~1 minut 15 sekunder]**

Nu till resultaten. Det här är det första nyckelresultatet. Jag startade en satellit på 600 kilometers höjd med hastigheten 8 696 meter per sekund — det är 1,15 gånger den cirkulära hastigheten, alltså lite snabbare än vad som behövs för en cirkel.

Och titta vad som händer: satelliten spårar en sluten ellips. Jorden befinner sig i en av ellipsens brännpunkter, precis som Kepler förutspådde för 400 år sedan.

**[KLICKA]** Omloppsperioden är ungefär 10 400 sekunder — det är cirka 2 timmar och 53 minuter.

**[KLICKA]** Och det viktiga: den här elliptiska formen var inte inprogrammerad. Jag matade bara in Newtons gravitationsekvation. Att banan blir en ellips med planeten i brännpunkten — det är Keplers första lag — framträdde helt naturligt från simuleringen. Simuleringen återupptäckte Keplers lag på egen hand.

---

## SLIDE 12 – Resultat: Flyktbana
**[~1 minut]**

Jämför nu med det här. Samma höjd — 600 kilometer — men hastigheten är 11 763 meter per sekund istället, alltså 1,10 gånger flykthastigheten. Och se vad som händer: satelliten kommer aldrig tillbaka. Den följer en kurva bort från jorden och försvinner ut i rymden.

Tänk på det: bara ungefär 33 procent högre hastighet — och utfallet är totalt annorlunda. I förra bilden kretsade satelliten runt och runt. Här försvinner den för alltid.

**[KLICKA]** Det är förresten precis så interplanetära uppdrag fungerar. Voyager 1 använde samma princip för att lämna solsystemet.

---

## SLIDE 13 – Resultat: Energibevarande
**[~1 minut 15 sekunder]**

Det här är kanske det resultat som bäst visar skillnaden mellan de två numeriska metoderna. Ni ser två grafer som visar hur väl varje metod bevarar den totala energin över tid.

Till vänster: RK4. Ni ser en helt platt linje. Energin håller sig nästan perfekt konstant över hela simuleringen.

Till höger: Euler. Här ser ni en tydlig drift — energin ökar sakta över tid, vilket innebär att satelliten gradvis spiralerar bort från sin rätta bana.

**[KLICKA]** Och skillnaden i siffror är häpnadsväckande. RK4 bevarar energin 100 miljarder gånger bättre än Euler.

**[KLICKA]** För att sätta det i perspektiv: om Euler missar målet med en kilometer, så missar RK4 med bredden av en atom. Det visar verkligen varför valet av numerisk metod spelar roll.

---

## SLIDE 14 – Resultat: 6 000 uppskjutningar i en bild
**[~1 minut 15 sekunder]**

Det här är kanske det mest imponerande resultatet och min personliga favorit. Jag körde 6 000 simuleringar, var och en med olika startvillkor — olika hastigheter längs y-axeln och olika riktningar längs x-axeln — och plottade resultaten som en värmekarta.

Varje pixel representerar en simulering. Grönt betyder att satelliten stannar i omloppsbana — en elliptisk bana. Gult är precis vid gränsen. Och rött betyder att den flyr ut i rymden — en hyperbolisk bana.

**[KLICKA]** Och titta på den skarpa gränsen. Den går vid ungefär 10 693 meter per sekund — och det matchar den teoretiska flykthastigheten exakt. Det är en stark bekräftelse på att simuleringen är korrekt.

**[KLICKA]** En annan intressant observation: notera att vinkeln knappt spelar någon roll. Färgövergången är nästan helt horisontell. Det är hastigheten som avgör nästan allt, precis som energiformeln förutsäger.

---

## SLIDE 15 – Diskussion
**[~1 minut]**

Så — vi har sett fyra nyckelresultat. Låt mig sammanfatta vad de betyder tillsammans. Flykthastigheten vid 600 kilometers höjd matchar teorin exakt: 10 693 meter per sekund. RK4 bevarar energin 100 miljarder gånger bättre än Euler. Och Keplers lagar framträdde naturligt från Newtons gravitation — de var inte inkodade i simuleringen.

**[KLICKA]** Den bredare slutsatsen är att numerisk simulering kan modellera fysik där exakta analytiska lösningar är opraktiska. Det är så rymdorganisationer faktiskt arbetar idag.

När det gäller begränsningar: det här är en 2D-simulering — verkliga banor är 3D. Det är bara två kroppar — ingen måne, ingen sol, ingen atmosfär. Och inga relativistiska effekter.

**[KLICKA]** Men dessa begränsningar är välkända och påverkar inte kärnresultaten för det omfång arbetet har.

---

## SLIDE 16 – Utmaningar längs vägen
**[~1 minut]**

Jag vill också vara ärlig om vilka utmaningar jag stötte på längs vägen.

Först och främst: matematiken var svår. Att förstå Taylorserier, härledningen av RK4, och alla formler för omloppsbanemekanik krävde stor ansträngning och många timmar.

**[KLICKA]** Sedan: var börjar man ens? Att gå från "jag vill simulera omloppsbanor" till fungerande kod krävde att jag bröt ner problemet i små, hanterbara delar.

**[KLICKA]** Att felsöka en fysiksimulering var också speciellt. När banan ser fel ut — är det ett kodfel eller ett matematikfel? Det är svårare att avgöra än man tror.

**[KLICKA]** Och slutligen: att balansera ambition med tid. Jag ville ständigt lägga till fler funktioner, men behövde faktiskt bli klar med både programmet och rapporten.

---

## SLIDE 17 – Tips för ditt gymnasiearbete
**[~1 minut]**

Jag vill avsluta med några tips för er som har ert gymnasiearbete framför er.

Nummer ett: börja tidigt och skjut inte upp. Projektet tar alltid längre tid än man tror. Ge er själva marginaltid.

**[KLICKA]** Nummer två: välj någonting ni verkligen tycker om. Ni kommer lägga många timmar på det här. Om ämnet intresserar er känns arbetet mindre som arbete.

**[KLICKA]** Nummer tre: bryt ner stora uppgifter i små steg. "Bygg en omloppssimulator" är överväldigande. "Beräkna gravitationen mellan två punkter" är görbart. Det var det viktigaste jag lärde mig.

**[KLICKA]** Nummer fyra: använd versionshantering, alltså Git. Spara era framsteg, spåra ändringar, och förlora aldrig arbete.

**[KLICKA]** Och nummer fem: var inte rädda att be om hjälp. Lärare, klasskamrater, onlineresurser — ingen gör det helt ensam.

---

## SLIDE 18 – Frågor?
**[Öppen]**

Tack så mycket för att ni lyssnade! Nu är det öppet för frågor. Jag kan också köra valfritt scenario live i OrbitLab om någon är nyfiken på att se en viss bantyp eller en specifik jämförelse. OrbitLabs källkod finns också på GitHub.

---

## Förberedda svar på troliga frågor

**"Varför just 600 km höjd?"**
600 km är en typisk LEO-bana — low Earth orbit. Det är ovanför det mesta av atmosfären men under Van Allen-bältena. ISS ligger på ungefär 400 km, så 600 km är en realistisk och vanlig höjd.

**"Varför tidssteg på 0,25 sekunder?"**
Det är en avvägning mellan noggrannhet och prestanda. Vid 7 500 m/s rör sig satelliten ungefär 2 km per steg, vilket ger tillräcklig upplösning för att RK4 ska följa kurvkrökningen. Samtidigt är det tillräckligt stort för att köra 6 000 simuleringar på rimlig tid.

**"Varför inte 3D?"**
Tvåkroppsproblemet i centralfält är planärt — banan ligger alltid i ett plan. 2D är därför fysikaliskt korrekt för detta fall, och det förenklar visualiseringen utan att offra noggrannhet.

**"Hur lång tid tog projektet?"**
Programmeringen tog flera månader och rapporten fick flera omskrivningar. Därför tipset att börja tidigt.

**"Använde du AI/ChatGPT?"**
Den allra första versionen — en enkel matplotlib-plot — genererades med ChatGPT. All vidare utveckling, fysikimplementering, analys och allt det som blev OrbitLab är eget arbete.

**"Kan man använda programmet för andra planeter?"**
Ja, OrbitLab stödjer 10 himmelskroppar — Jorden, Mars, Jupiter, Saturnus, Neptunus, Venus, Merkurius, Uranus, Månen och Io. Varje planet har realistiska fysikaliska egenskaper och egna förberäknade scenarier.

**"Vad skulle du göra annorlunda?"**
Jag skulle börja skriva rapporten tidigare, parallellt med programmeringen. Och jag hade velat testa symplektiska integratorer som alternativ till RK4 — de bevarar energi exakt per definition.

---

## Generella presenteringstips

- **Taltempo:** Prata lugnt och tydligt. Bättre att säga för lite än att hasta igenom allt.
- **Ögonkontakt:** Titta på publiken, inte på skärmen. Använd sliden som stöd, inte som manus.
- **Pauser:** Låt varje klick sjunka in en sekund innan du fortsätter förklara.
- **Demo:** Ha en backup-plan (inspelad video) ifall live-demon inte fungerar.
- **Frågor:** Det är helt okej att säga "Det är en bra fråga, det har jag inte undersökt." Ärliga svar är alltid bättre än gissningar.
