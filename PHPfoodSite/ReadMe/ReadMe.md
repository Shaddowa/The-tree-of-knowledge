Prosjekt nettside : Em's nettside                       


--------------------------------------------------------------------------------Konsept-----------------------------------------------------------------------------------------------------------
Ønsker å lage en fin og enkel nettside med mye funksjonalitet og avanserte php scripts. Ideen er at man skal få et godt inntrykk av maten som serveres, få en god kundeopplevelse samtidig som at
det skal være brukervennlig og minimalistisk desig. Jeg henter litt inspirasjona av flere nettsider, inkludert : PINK FISH, MCDONNALDS, CHIPOTLE, STOCK RESTURANG, MINT.COM    

UPDATE: For nå kan jeg lage en online dumplings og sommerrull buisniss bare for å selv bruke produktet og kanskje tjene litt penger og erfaring! Dette er mitt første "store" prosjekt så vi får se hvordan dette går.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


-------------------------------------------------------------------------------Spesifikkasjoner---------------------------------------------------------------------------------------------------
    Skal være dynamisk, slik at andre skjermer ikke får feil oppløsning på nettsiden

    Kunne betale på nettsiden, enten ved at man er kunde eller quick fix betaling

    Skal kunne legge igjen en tilbakemelding slik at andre på siden også får et inntrykk av kvaliteten på maten

    Bildekaruseller med de forskjellige rettene

    En Meny side hvor man kan se alt utvalget

    Lokasjon, vite hvor stedet befinner seg

    Åpningstider

    Kontakt oss

    Sosiale medier

    Forskjellige språk

    Delivery?

    Om resturanten og konseptet

-----------------------------------------------------------------------------------------------------------------------------------------------------------


-------------------------------------------------------------------------------------Logg------------------------------------------------------------------

10.05.2018 : LETT IMPLEMENTERING AV UTVALG PÅ HJEMMESIDEN : PROTOTYPE

Først vil jeg lage en funksjon i Js hvor det skal være lett å legge til det forskjellige utvalget på siden. Det skal være brukervennlig og lett og redigere.


 * Jeg har lagd et lett system hvor dataen av alle varer som legges til og de egenskapene den besitter blir lagret i et array med objekter, her er navnet på utvalget, prisen, beskrivelsen, type og kategori registrert. Senere skal jeg legge til slik at man kan laste opp et bilde og da vil bildet bli lastet opp i img foldere og man kan lett hente bildet til elementet med for løkker.*
 
 *Jeg hadde et lite problem med at når jeg la til textarea taggen så ble pristaggen tullet til slik at den enten viste NaN eller "europeisk", var litt usikker på hvordan jeg løste den, da det ikke så ut som noen klare feil i koden, så jeg ente opp med å endre litt hvor className skulle plasseres også hadde jeg textarea utenfor for løkken og registrert for seg selv. Etter at disse endringene ble gjort funket det igjen, så det var tydligvis noe som ble forstyrret mellom pris elementet og beskrivelses elementet.*

 *Nå er jeg ferdig med å kode for idag og det jeg har laget så langt er et system hvor man lett kan legge til nye elementer i ett array i form av objekter slik at det blir lett og assosiere de forskjellige elimentene med verdiene den besitter. Samtidig så vil varene vises i en tabell hver gang man legger til nye elementer. Da vil en ny rad bli lagd og informasjonen vil automatisk bli puttet i riktig kolonne. Jeg slet litt med hvordan jeg skulle få til tabellen, men jeg endte opp med å ha en preloaded <th> og at dette aldri skulle endre, dermed skulle nye rader bli lagt til hver gang man trykket på legg til knappen. Brukte text align center for å midstille teksten og har tenkt til å legge en fjern knapp på hver rad for å slette raden. Til nå lurer jeg på om det lureste er å lage elementene i JS eller om jeg bruker innerHTML for å få til det ønskede resultatet.*


11.05.2018 : LETT IMPLEMENTERING AV UTVALG PÅ HJEMMESIDEN : PROTOTYPE - FORTSETTELSE

    Idag vil jeg bli ferdig med å lage tabellen perfekt og få en fjerne knapp slik at man kan redigere de varene som er i listen av utvalg

    *Fikset systemet, nå kan man fjerne det som er lagret i utvalgs arrayen ved å trykke på knappen ved siden av som er linket til selve objektet i arrayen. Dermed vil tabellen oppdateres og den riktige oppdaterte tabellen vil bli vist.*


    *viste seg at det var en bug hvor systemet tullet med hva som skulle fjernes og ikke så det ble feil i rekkefølgen eller antall ting som ble fjernet. For å løse problemet, måtte jeg console logge hele prosessen og tenke logisk, isteden for å lage en og en linje hver gang man trykket på legg til knappen gjorde jeg slik at hele tabellen ble lagd hver gang man trykket på knappen. Dette er med på å eliminere mulige bugs senere i programmet når det kommer til rekkefølgen på tingene. Har en legg til vare funksjon og en oppdater funksjon som ser helt lik ut, har lyst til å gjøre programmet mer simpelt ved å knytte dem sammen.*

    *Fikset det, nå ser alt ut til å kjøre som det skal*


    EXSPANSIONS: Jeg tenker at jeg kan legge til mere informasjon i objektene slika at det blir lettere å finne informasjonen linket til de forskjellige rettene/annet. Dette kan være: RabattPris
    Bilde(r), Allergier.

    Kan også ha en "Er du sikker på at du vil slettet dette objektet knapp";


16.05.2018: HANDLEKURV FUNKSJON PROTOTYPE 1

    Idag har jeg lyst til å gjøre det mulig og legge varer i en handlekurv hvor prisen blir vist som samlet total pris og mulighet for å redigere innholdet, Tenker at dette ikke skal være en nettside som lagrer ønsker, fordi det skal være "hva har jeg lyst på her og nå". Handle kurven skal senere kunne betales for ved at man bare oppgir informasjon slik at vi kan godta bestillingen.

    *Idag gjorde jeg slik at når varer ble lagt til i systemet ble litt grunnleggende informasjon gitt om produktet. En legg til i handlekurven knapp ble generert for hver vare som ble laget og når man trykket på knappen ble summen av varen lagt til total summen og når man holder musen over den blå knappen så vil man se hva slags vare man har i vognen, hvilken pris hver av dem koster og hva totalprisen er. Når man fjerner musen fra knappen, forsvinner lista.

    ERROR: Hadde litt problemer med først og fremst og posisjonere divEl, men jeg endte opp med å Appende det til en container som var under knappen slik at den blå knappen aldri ble bortgjemt av andre elementer.

    Hadde også ett problem hvor når jeg fjernet musen fra knappen, så skulle divEl forsvinne ut ifra en loop i systemet, men det endte opp med at det ble feilkalibrering og det var alltid en eller flere objekter som ikke ble fjernet fra handlevogns display listen. Dette løste jeg ved å fjerne hele container elementet en gang, slik at systemet slapp og telle alle div elementene og få en error når den ikke fant det det lette eller eller at den "hoppet over" noen. 

    Har også litt problemer med når listen skal forsvinne for har lyst til å legge til en knapp på hver objekt hvor man eventuelt kan legge til eller fjerne et antall. Har enda ikke funnet ut av hvordan jeg vil ha det.
    *




    Prøver å legge til et system hvor alle varene som befinner seg i utvalgslisten blir vist som en egen boks på nettsiden. Her vil jeg at bilde og eventuelt info som handler om varen blir generert automatisk. Til nå har jeg fått til å få boksene opp på skjermen og de fjernes når noe på lista blir fjernet, men den fyller ikke helt ut den negative plassen som jeg ønsker. prøver å løse det med flexbokser.


    25.05.2018 LEGGE TIL BESTILLING PROTOTYPE

    Idag ønsker jeg å legge til et raskt system som lar deg kjøpe de varene man legger i handlekurven ved å fylle ut et skjema med informasjon om kjøperen. For nå ønsker jeg et simpelt system som jeg kan forbedre i fremtiden. 

    Begynnte å legge til en lytterfunksjon som sier at når handlekurven har varer kan man begynne med betalingsprosessen. For nå er ikke logikken 100% solid så jeg må endre på koden men jeg vet hva jeg ønsker å gjøre. 

    Fant ut en måte å lagre nøkkelnavnene på: Object.keys(variabel[posisjon])


    04.06.2018 FORTSETTELSE PÅ Å LEGGE TIL BESTILLING

    Idag skal jeg fortsette med der jeg slapp, men ønsker å forenkle tankene mine så det funker uten å tenke noe veldig på optimiseringsdelens

    Klarte det på en effektiv måte, lagde en lopp som gikk gjennom en liste med objekter
    neste gang må jeg kontrolere at alle feltene er fylt ut og at når man "betaler skal bestillingen stå som en svarsetning for kundene og resturanten".


    07.06.2018 FORBEDRE HANDLEKURVSYSTEMET OG LEGGE TIL BETALINGSMELDING

    Idag ønsker jeg og vise flere varer grupert i handlekurv systemet slik at X2 lakseburger (pris) vises isteden for lakseburger ... lakseburger. Jeg vil også få til en konfirmasjons melding som viser kundens bestilling.


    08.06.2018 UPDATE
    Idag fikset jeg med hjelp av lærerne mine handlekurv systemet. Jeg begynte med å legge til antall i handlekurvsystemet og sammenlignet ID til varen man trykket på med ID til varen i handlelkurven for å sjekke om man allerede hadde varene. 

    Var en bug om hvordan jeg skulle øke antallet med de varene som allerde lå i handlekurven uten å skrive mye kode. Antallet var først ikke definert og lurte på om jeg burde lagre alle verdiene i et array for så å inkremere dem, men syntes dette var tungt. Vi fant en løsning ved

    
    if (idHK == Number(handlekurvEl[i].id)) {
        lagttil = true;
                
        handlekurvEl[i].antall += 1;
                
        break;
              
    }  

    Nå gjenstår betalingsmeldingen igjen!


    -----------------------------------------------------------------------Logg-----

    21.06.2018 BILDEKARUSELL PROTOTYPE

    Idag vill jeg fullføre bildekarusellen for nettsiden og legge til en kundebeskjed. Jeg bruker eksempelbilde jeg tok av Emma.

    Da jeg skulle lage bildekarusellen ønsket jeg og lage den uten å se på tidligere eksempler for å prøve å gjøre det utenatt. Klarte å lage en ødedlagt versjon av noe som lignet på en bildekarusell men bildene oppførte seg ikke som ønsket.

    For å gjøre det ordentlig brukte jeg tidligere eksempler, og nå skal jeg prøve å beskrive hvordan koden fungerer slik at jeg kan bruke det senere uten å se på tidligere kode.


    ---------------------------------------------------------------------------------------------------------------------------------
    | Jeg lagde først en beholder for bildene som skulle være i  karusellen                                                         |
    | html : <div id="bildekarusell>                                                                                                |
    |         </div>                                                                                                                |
    |                                                                                                                               |
    | I Js lagde jeg en liste med objekter hvor alle bildedne lå og utifra hvor mange elementer som lå i listen, skulle like mange  | div elementer bli lagt til karusellen.
    
      Js: for(var i = 0; i < bilder.lenght; i++){
      Lag div elementer og legg til karusellen med samme className    
      }

     Etter det lagde jeg en variabel som skulle holde alle disse div elementene med dems className og sa at bildene[i] .style.backgroundImage = arrayets bilder[i].src. I samme for løkke sjekket jeg om hvis i ikke var 0, så skulle de  settes til display = "none".
    
      Etter det definerte jeg noen variabler:  synligBilde = 0, nesteBilde; og tid på 5000.
    
     Til slutt lagde jeg selve funksjonen som skulle flytte bildene. Denne funksjonen sa at om synligBilde(0) === bildene.length - 1 (antallElementer), så skulle neste bilde = 0.  om dette ikke var tilfellet så skulle neste bilde = synligBilde + 1 (1), denne ville øke etterhvert. 
     Til slutt måtte det neste bildet gjøres klar til å gå inn, mens det allerede synlige bilde måtte gå ut av rammen. Når denne  syklusen er over, skal det synlige bilde ha lik verdi som det neste bildet og funksjojnen skal gjenta seg med funksjonen setTimeout.
    
    Siden det første bilde allerede hadde index 0 så kunne vi si at neste bilde hadde index 1 i bildene arrayet. Detter er viktig logikk for at rekkefølgen blir riktig!
    ---------------------------------------------------------------------------------------------------------------------------------
    Nå skal jeg legge til beskrivelsen som er angitt til hvert bilde.


    23.06.2018 STARTE MED NETTSIDEN

    Idag skal jeg starte med nettsiden. Har fått design ide av ragnhild og skal prøve så godt jeg kan og etterligne hva hun har lagd. Har allerede laget en versjon av bakgrunnen jeg brukte med bilde redigeringsprogram, men jeg tror jeg bør gjøre bilde bedre ved at det ikke er ujevne linjer, men profesjonelle glatte linjer. Dette skal jeg jobbe med.


    Fikset en nettside versjon av det ragnhild hadde lagd. Den ble ganske lignende, men la ikke til OM OSS bilde delen enda fordi jeg skal høre om det er det vi bør putte på startsiden. Det var ingen store bugs og var ganske greit og enkelt og kode. Må ha god orden på php filene mine og css filene mine.

    Det eneste som ikke er "bra" med designet er at font og grafikk ikke er ordentlig gjort, men bare raskt funnet for å se det visuelt for å sjekke hvordan viben blir.



25.06.2018 LEGGE TIL KONTAKT OSS SEKSJONEN

idag vil jeg legge til kontakt oss seksjonen, som vil sende en e-post til emailen min. Koden skrev jeg ved hjelp av udemy klassen php. Derfor ingen personalisering i e-mail funksjonen.

Jeg har nå lagt til kontakt siden på siden. Denne funker ikke helt enda fordi hadde problemer med php-en. Men jeg fikset også slik at vi kan linke til ulike CSS filer og ulike paths for filer utifra hvor i programmet man er. Dette er kritisk, for om vi ikke definerer disse variablene vil nettsiden ikke fungere. 

26.06.2018 Idag skal jeg lage språk instillingene slik at når du går over språk teksten, vil en drop down liste med de tilgjengleige språkene vises, jeg skal også gjøre ferdig footer elementet og prøve å fikse bildekarusellen ved å lage min egen versjon.

*BUGG* Kom over en bugg som ikke oppdaterte Css stilen min. Ingenting skjedde selvom jeg refresha siden. Prøvde å sjekke om det samme skjedde på macbooken min eller om det var konflikter mellom de to MAMP aplikasjonene.

På internett fant jeg at i noen tilfeller blir ikke alle filene vist riktig fordi nettsiden har lagret kopier av tidligere versjoner for å slippe og laste ned sidene hver gang det blir refresha og dermed kan det forekomme at en ikke riktig datert fil blir vist. 

*FIX*
på MAC : cmd + shift + r
på PC: ctr + shift + r


02.07.2018 FORTSETTE PÅ BILDEKARUSELLEN

Idag skal jeg prøve å få ferdig bilde karusellen. Jeg støtte på et problem hvor alle de displayIndex dot elementene ikke fungerte som de skulle fordi man ikke kunne se dem. Jeg brukte lang tid på å finne ut hva som skjedde og fant ut at siden parent elementene var sett til overflow:hidden så ble elementene stylet, men man kunne ikke se det fordi hele elementet ikke ble vist uanset

*BUG* CSS styles ble ikke lagt til på dot elementene
*FIX* gjøre parent elementene om fra overflow:hidden til at det ikke skulle være hidden.

Har nå en funkende bildeKarusell som senere skal fungere slik at den kan gå tilbake når man trykker på en av knappene. Dette er enda ikke ferdig, men har en standard bildekarusell som jeg kan ha i mellom tiden til jeg har kommet lenger på siden. Hvis jeg virkelig vil bli ferdig idag så gjør jeg funksjonen ferdig idag, ellers så starter jeg på en admin side.

03.07.2018 GJØRE FERDIG DE UFERDIEGE ENDRINGENE FØR JEG STARTER PÅ ADMIN SIDEN

*BUG* I kontakt skjemaet så hadde jeg først problemer med at php ikke fungerte. Prøvde å echo ut ting, men det ble ikke noe. Nå så jeg at jeg manglet action og method på form elementet. Jeg kan ikke huske at jeg glemte det forrige gang jeg prøvde å lage det alene, men nå funker det hvertfall

*FIX* HUSK method og action attribute på form elementet



**14.00** Til nå har jeg gjort unna 2 tasks fra todo list. Jeg har linket alle footer elementene til de forskjellige sidene også har jeg fikset email funksjonen på kontakt siden. Denne skal i teorien funke nå, men kan ikke sjekke det enda fordi det er på local host og MAMP har ikke email funksjoner.

Senere idag skal jeg prøve å lage de andre sidene (Resturant og om oss side), eller så begynner jeg på en admin side
**14.00**


05.07.2018 SKAL LAGE ADMIN SIDEN

Idag skal jeg lage en admin side med log in funksjonalitet ved å følge en video (https://www.youtube.com/watch?v=xb8aad4MRx8&t=758s)

skrive ned trinnene her så jeg kan se på det senere og huske hva jeg gjorde.

#1 Localhost-PhpMyAdmin
Først gikk vi inn i phpmyadmin på localhost tjeneren og lagdetabellen vi skal bruke senere. 

    CREATE TABLE users(
        user_id int(11) not null AUTO_INCREMENT PRIMARY KEY,
        user_first varchar(256) not null,
        user_last varchar(256) not null,
        user_email varchar(256) not null,
        user_uid varchar(256) not null,
        user_pwd varchar(256) not null
    );


#Lage php  fil for å koble opp til databasen
Skrev inn de forskjellige detaljene man må ha med for å koble til databasen min

ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL | E_STRICT);

**DET MAN MÅ HA FOR Å KOBLE SEG TIL**
   $dbServername = "localhost";
   $dbUsername = "root";
   $dbPassword = "root"; // I Mamp er passordet "root", men i XXamp er passordet " ";!
   $dbName = "loginsystem";

   $connection = mysqli_connect($dbServername, $dbUsername, $dbPassword, $dbName);

#Det er viktig at formen din har action =" " der du har denne php filen for at den kan sjekke riktig informasjon! Da må man angi file path til filen som 
#skal ta seg av sjekkingen

action="../loginsystem/dbh.php">


#Derifra begynner jeg og sjekk (om input felt er tomme, og om de faktisk stemmer med databasen jeg har satt opp) //Det er inni en nested if else statment!

if(empty($uid) || empty($pwd)){
    header("Location: ../admin.php?login=empty"); //Redirects u
    exit()
}


**SJEKKER BRUKERNAVN**
$sql = "SELECT * FROM users WHERE user_uid = '$uid'";
$result = mysqli_query($connection, $sql);
$resultCheck = mysqli_num_rows($result);

*Må være minst en rad for at php ikke skal sende deg tilbake*
if($resultCheck < 1){
    header("Location: ../admin.php?login=error");
    exit();    
}       
    
*Vi gjør det samme med passordet og hvis dette kommer tilbake true får du logget deg inn*
if ($resultCheck == false){
        header("Location: ../admin.php?login=error");
        exit();
} else if( $resultCheck == true){
            header("Location: ../loginsystem/login.php?login=success"); //sender deg til loginscriptet
            exit();
}


Dette var det jeg fikk gjort idag. Lagde et enkelt loginsystem som ikke er sikkert i det hele tatt, og heller ikke beskyttet mot hacking, men det funker for nå. Endringer skal gjøres senere.




14.07.2018 DESIGNE ADDMIN SIDEN

Idag har jeg endelig tenkt til å style admin siden så jeg kan få frem varene mine på hjemmesiden ved å lage en database for alt jeg har! 


**LOGOUT**

Prøvde først : window.location.href("../adminPhp.php"); //Feilemelding, du har ikke tilgang

**Update**

Den funket allikavel? Men tydligvis er replace bedre fordi "because replace() does not keep the originating page in the session history, meaning the user won't get stuck in a never-ending back-button fiasco"

----------------------------

Dermed : bodyEl.innerHTML += "<?php  header("Location: ../adminPhp.php"); ?> // dette funket ikke

------------------------------

Til Slutt: window.location.replace("../adminPhp.php"); //Dette funket

--------------------------------


Har laget en admin side med utvalgsseksjon, ingenting på siden funker enda, men  det visuelle er någenlunde på plass. Har en logut button også, men den er ikke session aktivert så om man skriver inn url kan man komme seg inn på admin siden. Lagde også en database på PHP my admin som jeg skal koble opp til senere

15.07.2018 BLI FERDIG MED LEGG TIL VARER ADMIN SIDEN

Idag skal jeg implementere gamle funksjoner som jeg lagde før jeg startet på prosjektet for å legge til utvalg i nettsiden

Jeg fikk til og koble til min database i phpmyadmin og den funker som den skal. Nå kan jeg legge til varer i databasen. 
Hadde et problem med at jeg hadde laget skjemaet i js, men dette er ikke gunstig da det er veldig mer avansert og koble til databasene, så dermed tenker jeg at jeg ikke skal skrive så veldig mye js, men heller bruke php for å oppnå ønskede resultater. JS er tross alt bare "bakgrunns" aktivitet, og har ikke så mye med servere og gjøre. derfor er det bedre å ha "mange php filer" enn å prøve å lage alle sidene med ett js script!

**SPØRSMÅL**
Da jeg skulle legge til elementer i databasen min gikk det ikke med mindre jeg hadde denne setningen i programmet:

if($connection -> query($sql)){
    echo "spørringen $sql ble gjennomført";
} else {
    echo "noe gikk galt";
}

Noe jeg synes er rart fordi denne skal bare sjekke og gi beskjed om at noe funket eller ikke. Ønsker derfor kanskje å ha denne meldingen som en pop up istedenfor!

**SVAR**
Det var ganske åpenbart hvorfor det ikke funket. Glemte denne setningen. Det jeg hadde før var bare en variabel med kommandoer. for at noe faktisk skulle skje måtte jeg gjøre en mysqli_query! 

$result = mysqli_query($connection, $sql);


*SPØRSMÅL*
Men da lurer jeg fortsatt på hvorfor det første funket selvom jeg aldri gjorde en mysqli_query. Jeg bare sjekket for at noe skjedde, men tydligvis så utføte den spørringen i samme slengen.



17.07.2018 STARTE MED Å HENTE UT INFORMASJON FRA DATABASE TIL TABELL

Idag skal jeg lage tabellen på adminsiden. Valgte å lage den første delen av tabellen på php siden, mens resten skal lages ved bruk av php kode. Hver gang jeg trykker på legg til vare skal en tabell oppdateres. Har litt OCD over at AI i sql ikke blir til 0 igjen men fortsetter og øker selvom elementene blir slettet på siden. Det har jo såklart ikke så mye og si siden koden vil fortsatt fungere helt fint, det er bare personlige problemer

**BUG**

Hadde en bug hvor det ikke gikk ann og hente informasjon fra databasen fordi $connection tydligvis ikke var tilgjengelig for funksjonen

**LØSNING**
Måtte angi parametere med ($connection) både i funksjonen og i den som kallet funksjonen for at det skulle funke.

Valgte etter å ha lett etter den beste løsningen og skrive js kode i php kode ved bruk av script taggen slik at jeg kunne hente ut tabellen og endre den indre html med en ny <tr> tagg og veridier.

**BUG**
Tabellen endte opp med å ikke være definert (NULL) selvom scriptet var på bunden av siden

**LØSNING**
Tror at siden funksjonen og tabellen var så nærme hverandre så skapte dette problemet, men vet ikke helt. Jeg løste dette ved å kalle funksjonen en gang over i løpet av at siden lastet ned. 

**BUG**
Ville at <th> ikke skulle scrolle når overflow var nådd, men fant ikke en løsning på dette (enda), tenker at det ikke er så farlig, siden dette er en amatør nettside uansett. I fremmtiden ønsker jeg å finne ut dette



12.07.2018 LAGE SLETTE KNAPPEN PÅ ADMIN SIDEN OG SÅ SKAL JEG PRØVE Å LØEGGE TIL FEATURE OG BILDER

Idag skal jeg gjøre det mulig og slette elementer på admin siden. Dette er nok lett, derretter skal jeg legge til en ny input type ="file" og endre tabellen selections slik at jeg kan ha et bilde som hører til. (Kanskje best å ha en max størrelse på bildet også). Når det er ferdig skal jeg prøve å ha en status knapp som sier om bildet skal være på featured siden  eller ikke. Jeg tenker at bildekarusellen skal jeg personlig kode for selv slik at jeg kan ha knapper og slikt som passer til bildene.

*BUG*

Hadde store problemer med å slette innholdet på siden. Først og fremst ante jeg ikke hvilken vinkel jeg vill komme fra. Tenkte først og bruke Javascript for da kunne man legge til evenlistener på knappene og derifra få id til knappen. Da jeg prøvde dette var problemet og skrive sql kode, for da trenger man å bruke php for å få tilgang til serveren. Derfor prøvde jeg å skrive php kode i js, og hadde på et tidspunkt et div element som bare skulle fungere som et php vindu for å sette i gang en funksksjon. Problemet med denne løsningen var at det var veldig vanskelig og få e.target.id til å bli konvertert over til en php variabel som kunne brukes. Først skrev jeg JS i et script, men trodde det ikke klarte å fyre av komandoen fra to separate filer, så prøvde å skrive det i selections.php siden min. Prøvde å skrive JS i php og PHP i JS. Dette funket dårlig for meg. 

*LØSNING*
Det som gjorde det mulig og slette innholdet på siden min var ved å bytte ut <button> taggene med input type submit knapper som var linket opp mot en form. Kunn slik kunne jeg sjekke om en knapp var blitt trykket i php. dette hørtes veldig komplisert ut, og var derfor jeg ikke prøvde det når jeg slet litt, fordi jeg vill se om det var løselig på en annen måte (men nei). Derfor er alle "knappene" i en form som blir aktivert når de klikkes. for å vite hvilken knapp jeg trykket på sa jeg at valuen til knappen skulle være $selection_id. Dete hele ser slik ut:


<form method = 'POST' action = ' '><input type='submit' name='delete' class='deleteButtonVarer' value = '$selection_id'></form>


if(isset($_POST['delete'])){
    $value = $_POST['delete'];

    $sql = "DELETE FROM selections WHERE selection_id = '$value'";
    $result = $connection -> query($sql);
}

I heighnseght kunne jeg spart masse tid ved å bare gjøre dette, men selvom jeg visste at dette kanskje var den beste løsningen, ville jeg ikke ta den fordi
Jeg vil prøve å løse ting jeg sliter med, ikke kode ting jeg vet jeg kan fikse lett


*BUG*
Hadde også et problem med bildeupload. Nå har jeg laget et upload skjema som blir lagret i databasen som type blob, men problemet er å vise bildet. 
Tenker at det ikke er så farlig enda, fordi jeg skal jo ha det på den hovedsiden, ikke admin siden. Men jeg er fortsatt usikker på om

base64_encode er den riktige løsningen... vi får se.


22.07.2018 LAGE FEATURE SIEDN OG VISE DEN PÅ INDEX SIDEN

Idag skal jeg bli ferdig med å få feature siden til å funke. Har tenkt til å bruke feature checkbox for å si om de skal være med på siden. Kan også ha at max fetured items kan være et antaall, eller så kan jeg ha unlimited antall, men at man må bla for å se alle. Noe som ikke høres bra ut.


For å løse dette lagde jeg en ny kolonne kalt selection_status som enten kunne være 1 eller 0. Brukte to forskjellige update setninger utifra hva som allerede var i denne kolonnen.

**BUG**
Prøvde å gjøre slik at når man har trykket på feature knappen så skulle knappen endre farge for å indikere at den er aktiv. Prøvde i JS, men problemet er at siden feature knappen er en submit knapp, så oppdateres siden og js blir refreshed... dette er dumt. Valgene ,å lagres, som jeg har, men vet ikke hvordan man skal skrive css kode i php utifra verdier i sql database.

07.08.2018 / 08.08.2018FIKSE FEATURE KNAPPEN

Idag skal jeg fikse feature knappen slik at den lyser grønt når den skal

Har endret litt på kode strukturen slik at den er mer delt opp og enklere og lese. Den gir mer mening nå.

**BUG**
Har slitt velig med å implementere feature knappen fordi jeg ikke vet hvordan jeg skal angripe problemet:

#1 Hvordan skal jeg skrive JS i PHP eller omvendt for å endre CSS
#2 Hvordan kan jeg enklest måte få knappene grønne
#3 Hvorfor er det så jævlig vanskelig


**LØSNING**
Fant ut en løsning og nå fungerer knappene slik de skal! Det tok faen meg lang tid ahaha. Jeg prøvde og failet en del, men jeg kom nærmere svaret etter at jeg eleminerte metoder som garantert ikke ville gå. Til slutt fant jeg den beste løsningen, men kanskje ikke den mest effektive!

FØRST måtte jeg gjøre om på strukturen av koden min fordi den var rotete og uroganisert og ga ikke mye mening. Jeg endte opp med å lage elementene på siden først fordi jeg fikk undefined elementer når jeg skulle velge ut featurebutton elementene. Jeg hadde orginalt satt dem på bunden for jeg tenkte at om de slettet innholdet så måtte man ikke trykke to ganger på delete knappen for at det skulle registreres. *FIX* jeg bare satte at man skulle lage tabellen øverst også med delete funksjonaliteten over den, mens resten av koden skulle komme under.

Hadde egentlig lyst til å endre farge med en gang når man skulle skifte statusen, men det funket ikke slik jeg ville og endte opp med at enten den siste eller første knappen bestemte alle knappenes farge. Trodde først at det var fordi scriptet gikk så fort og at elementene ikke loaded inn, men kan hende det funker nå siden jeg endret strukturen på koden

Endte opp med å gjøre en fullstendig sjekk på slutten som skulle ta ID og status into concideration og bare endre alle hver gang en feature knapp ble trykket på. Dette var fordi jeg ikke kunne bruke e.target i JS fordi siden kom til å refreshe og JS ville bli resettet.

Lagde to php arrays som jeg tok i bruk når jeg skrev for løkken min. Det er best og skrive JS i PHP ved bruk av echo! da kan man ta i bruk variabler fra php uten å få error: undefined variable

    for($i = 0; $i < sizeof($ID); $i++){
        echo "<script>
                        
        var button = document.getElementsByClassName('featureButtonVarer');
                        
        if($ID[$i] != button[$i].value){
                        
            console.log('ingen match')
                        
        } else {
            if($statusB[$i] == 1){
                button[$i].style.backgroundColor = 'green';
            } else if($statusB[$i] == 0){
                button[$i].style.backgroundColor = 'yellow';
            }
        }

        </script>";
    }
 

Nå fungerer den som den skal!!



08.08.2018 AVANSERT BILDEKARUSELL

Idag vil jeg lage 'avansert bildekarusell' hvor brukeren ser hvilket bilde de ser på ved å se på de dottene for de skal nemlig skifte farge utifra hvilket bilde man ser på.


Gikk greit lett, men jeg prøvde å lage hele bildekarusell filen litt mer rydddig med funksjoner som trigget hverandre og som sendte variablene videre ned, men fikk problemer med at bildene ble unddefined etter 1 runde.


11.08.2018 FIKSE BILDE UPLOAD

Idag har jeg tenkt til å fikse bilde upload på admin pagen også displaye en på featured siden.

**BUG**

Hadde en bug som jeg måtte rette opp i mens jeg skulle prøve å fikse bildene og dedt var at når man ladet siden igjen fikk man error melding om at checkstatus($connection) ikke var definert. Jeg lurte på hvorfor jeg fikke error da jeg trodde alt var perfekt med systemet, men det kan hende det var fordi jeg ikke prøvde og relode siden eller sjekke om den var helt sikker.

**FIX**

Måtte endre logikken og rekkefølgen på hvordan funksjonene skulle kjøre. Endret ingenting i koden spesifikt men puttet checkStatus() utenfor lag tabell funksjonen. Tror det funker nå.


**SESSION**

Frida hjalp meg med session funksjonen så nå kan man ikke komme på admin siden med mindre man har en session going. 

**BUGG** Trodde session ikke funket som den skulle, men det viste seg at jeg lurte meg selv. Først og fremst så hadde jeg et logout script som var aktivt og som logget ut brukeren "uansett" om du hadde isset() funksjonen. Derfor ble man lurt fordi jeg manglet en <form> rundt input taggen unsett. Prøvde først og cleare browser cache som funket litt, ved at man ikke kunne logge in for første gang, men man sikk aldri en $_SESSION['login'] = false og ville om man hadde logget in 1 gang, komme inn uansett.

**FIX**
Jeg fjernet logout scriptet og la til en form rundt logut knappen. Dermed endret jeg statusen til logged out og for å være på den sikre siden satte jeg SESSION_UNSET(); som fjerner alle virkende session variablene som er registrert. Dermed skrev jeg SESSION_DESTROY(); som vil ødelegge sessionen og dermed relovate til admin siden Header('Location', 'loginsystem/admin.php?login=loged out');

**HOW IT WORKS**

Først starter man en SESSION_START(); som gjør at variabler kan bli overført til andre php scripts og funke som en måte å holde styr på brukeren (Om personen er logget in, hvem det er, hva personen har gjort i sin session, osv...). Dermed kan man bruke variabler ofte startet med $_SESSION['noe'] = noe;
slik kan man kontrolere aktiviteten til brukeren over flere sider. Når man er ferdig og skal logge ut må man ødelegge sessionen. Man kan gjøre dette enten ved å sette $_SESSION['login'] = false. Eller så kan du være på den sikre siden og si SESSION_UNSET(); og SESSION_DESTROY(); før du omdirigerer brukeren til en annen side(log out siden);


14.08.2018 LAGE FEATURED SLIDEND UTEN BILDER FOR NÅ OG PRØVE OG LIMITE TIL 4 FEATURES MAX


Lagde feature siden uten bildene foreløpig. Den funker som den skal og det er flexboxer så uansett hvor mange features man har så vil plassen bli fordelt likt. Tror jeg ikke vil sette restriction på antall features fordi noen vil kanskje vise mer enn bare 4, kan heller skrive i tabellen "(Recomended (3-4))", for det ser sikkert best ut, men det funker uten å ha en max limit. Fikset også SESSION funksjonen på admin siden.


17.08.2018 / 18.08.2018 / 19.08.2018 FORTSETTE DER JEG SLAPP MED Å ENDRE LITT PÅ WEBSIDE LAYOUTEN

Idag må jeg ordne opp i det estetiske

Jeg endret bildekarusellen så nå ligner den på den prototypen ragnhild først sendte til meg. Tror den funker og man kan trykke fram og tilbake på bildekarusellen og se bildene slik. Må bug teste litt til, men virker lovende. Var ikke vanskelig og få det til. Måtte bare ha noen div elementer med eventlistener og om de ble trykket ned endret jeg bilde utifra hvilken vei jeg klikket.


**BUG**

30.08.2018 FIKK HJELP AV TOBIAS MED BLOB BILEOPPLASTING
Bildeopplasting.
Lagret navn, men ikke bilde data.

**FIX**
I formen la til funksjon for filopplastning (enctype="multipart/form-data")

I POST handleren bruker $_FILES for å lese filnavn og data, ikke $_POST
La til selection_picture_name i DB for å kunne lagre navn og det faktiske bilde i databsen.
Laget image.php som henter bilde data, og sender videre bilde som kan vises i browseren.
"<img src='/php/includes/image.php?id=".$selection_id."'>" viser bilde.


01.09.2018 REVAMP NETTSIDEN
idag har jeg lyst til å komme meg lenger på nettsiden fordi jeg endelig har løst bilde problemene. Nå skal jeg følge designet jeg har sketchet for meg selv og lage nettsiden ferdig

**BUG**

Fikk en bug hvor da jeg skulle skrive description til en av rettene brukte jeg " " for å lage hermetegn og dette ødela koden. Siden $currentSentence allerede er lagd med "" så endte de setningen slik at koden ikke ble riktig. For å løse problemet måtte jeg bare fjerne den retten som hadde "" og da funket det igjen. Trodde det var noe galt med funksjonene som tidligere hadde funket, men det hjalp og se hvilken linje feilen var på ved å gå i inspektor tool i browseren.

Det står at navn er 0, men det kjønner jeg ikke noe av

Har fikset ferdig index siden på nettsiden. Nå ligner den så og si på det jeg sketchet. Må altids tweake litt, har ikke lagt meg ned i detaljene som font eller farger, men gjør det når det bare må polishe på siden. for nå funker det.

mangler bare en knapp som fører brukeren til topen av siden.

05.09.2018 FIKSE PÅ HJEMMESIDEN, OM OSS SIDEN OG DESIGNE ONLINE SIDEN

Nå ser hjemskjermen helt prikk lik skissene. Har lagt til en knapp som blar opp til starten av siden, men man må tydligvis å ha jQuery for å lage en smoothe scrolling. Kan hende jeg fikser det senere. I teorien så er det bare handle siden som gjenstår. På de andre sidene og språksidene, må jeg bare bestemme meg for hva som skal stå der. 

Jeg må sikkert også hele tiden endre utseende, for blir aldri helt fornøyd. Skal også endre font. Når kjøpesiden er ferdig skal jeg jobbe med admin siden, og ha vedlikedhold helt til jeg føler at siden er god nok til å publiseres. 

Skal designe online siden nå på ark og følge den slik.


19.09.2018 LAGE ONLINE SIDEN

Idag og i morgen / helgen må jeg bli ferdig med online siden. Eneste grunnen for at den ikke har blitt ferdig, er fordi jeg vet ikke helt hvordan jeg ønsker at den skal se ut, men idag har jeg en anelse.

Laget en side i online som jeg er fornøyd med til nå, den må ha litt mere funksjonalitet og så kanskje gjøres finere etterhvert. De problemene som oppstod var å definere bakgrundsbildet til hver av elementene og tenke på den beste måten å legge til de overlayene jeg ønsket at brukeren skulle få. Css var lettere enn JS CSS bør egentlig alltid brukes når noe med styling skal skje! JS bør brukes kunn til å endre styles og legge til funksjoner. Dette ble pathen:

    style = 'background-image:url(/php/includes/image.php?id=$selection_id)';>".   

Jeg begynner å nerme meg en endelig versjon når det kommer til det funksjonelle.




20.09.2018 BLI FERDIG MED ONLINE SIDEN

Idag ble jeg ferdig med Online siden, hvertfall det visuelle. Nå har vi en fungerende handlekurv og informasjon på alle rettene. Måtte endre koden litt fra min prototype, for da hadde jeg en handlekurv som skulle vises når musen gikk over den. Nå er handlekurven fixed på skjermen, og den funker ganske bra. Et triks jeg brukte var å ha en:

    var currentSentece = ""

Dette var veldig bra! Nå gjennstår bare å lage ordensskjemaet og fikse litt på admin siden, og legge til språk? (om jeg gidder...)
Designvis er det fortsatt mye som gjenstår.

02.10.2018 OPTIMISERING & ORDENSSKJEMA

Idag skal jeg optimisere handlelisten, og lage et fungerende ordensskjema.

Lagde ordenskjema, og har nå + og - knapp i selve handlelisten. Kjøpe knappen er ikke tilgjengelig før man legger noe i handlevognen og trykker man på den mens vognen er tom, får man alert, om at handlekurven er tom. Nå må jeg koble det opp mot en tabell i en database også er den delen ferdig.

**BUG**
Fant en bug som gjorde at når jeg klikket meg ut av skjemaet, og begynte å trykke på pluss og minus knappene litt random, så ville noe rart skje med handlelisten min, og noen av elementene ville ikke bli vist på siden. Tror kanskje at dette har noe med id og gjøre, men er enda ikke helt sikker. Dette skjer kunn når du har vært på ordenskjemaet, ikke før, ifølge mine observasjoner.

Hadde også en bug om at input type hidden av ordre ble udefinert, viste seg bare å være at jeg skrev handelkurv[i].navn isteden for handlekurv[i].vare

Nå har jeg gjort mye, skal koble opp alt til en tabell i morgen, vise den på admin siden, og konfigurere orderbekreftelse på e-mail. Kanskje jeg også bør ha en preview av hva kunden har kjøpt, men det er ikke kritisk nå.

03.10.2018 VISE ORDE PÅ ADMIN SIDEN
Idag skal jeg koble opp ordrene på admin siden.