# Akciju Tirgus Informācijas Iegūšanas Sistēma

## Projekta uzdevums

Šī projekta galvenais mērķis ir automatizēt biežu manuālu darbību — finanšu tirgus informācijas meklēšanu un apkopošanu dažādos avotos. Šī programma nodrošina lietotājam iespēju iegūt būtiskāko informāciju par akcijām (tickeriem), tostarp:

- aktuālās akciju cenas un izmaiņas,
- dividendes un peļņas rādītājus,
- lielāko akcionāru datus,
- uzņēmuma sektoru un industriju,
- aktuālās finanšu ziņas,
- gaidāmās IPO un peļņas paziņojumus,
- tirgus indeksu apskatu (Dow Jones, NASDAQ, S&P 500),
- tirgus līderus un zaudētājus (gainers/losers),
- top trending akcijas ar detalizētu analīzi.

Šis rīks spēj ietaupīt laiku un uzlabot informācijas iegūšanas efektivitāti ikdienas investīciju vai finanšu analīzes vajadzībām.

## Izmantotās Python bibliotēkas

Projektā tiek izmantotas šādas bibliotēkas:

- requests – HTTP pieprasījumu veikšanai uz tādiem resursiem kā Yahoo Finance, IPO Scoop u.c. Tā ļauj dinamiski iegūt datus no interneta.
- BeautifulSoup (no bs4) – HTML satura parsēšanai un vajadzīgās informācijas izgūšanai no tīmekļa lapām. Tā palīdz apstrādāt nesakārtotu HTML kodu un strukturēt datus.

Šīs bibliotēkas ir būtiskas tīmekļa skrāpēšanas funkcionalitātes nodrošināšanai, kas ir galvenais informācijas iegūšanas veids šajā projektā.

## Izmantotās datu struktūras

Projektā tiek izmantotas:

- saraksti (list) — lai uzglabātu ziņu virsrakstus, akciju rādītājus, īpašnieku sarakstus, top akcijas;
- vārdnīcas (dict) — indeksu ticker simbolu glabāšanai;

## Programmatūras izmantošanas instrukcija

1. Palaist projekts.py failu Python vidē.
   Nepieciešams Python 3.6+ un instalētas bibliotēkas:
   ```bash
   pip install requests bs4
