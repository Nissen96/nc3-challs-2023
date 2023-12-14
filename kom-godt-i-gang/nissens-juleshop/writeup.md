# Writeup

Ved forbindelse til Nissens Juleshop får vi følgende menu:

```
Velkommen til Nissens Juleshop!

Du har i øjeblikket 1000 JULESNE på din konto
Hvad vil du købe?
        1) Julelys (85 JULESNE)
        2) Gavepapir (40 JULESNE)
        3) Sneskovl (230 JULESNE)
        4) Juletræ (760 JULESNE)
        5) Flag (1000000 JULESNE)
> 
```

Hvis vi vælger et produkt, bliver vi spurgt hvor mange, vi vil købe og herefter fratrækkes det samlede beløb fra vores konto.

Hvis vi prøver at købe et produkt, vi ikke har råd til, får vi en fejlbesked - så hvordan får vi købt flaget?

```
> 5
Den går ikke, du har ikke engang råd til 1x Flag
```

Hmm, når vi vælger et produkt og et antal opdateres vores konto umiddelbart til

```
total = total - pris * antal
```

Hvis vi kan få `pris * antal` til at blive et negativt tal, så ender vi i stedet med at *indsætte* julesne på vores konto. Vi kan ikke sætte prisen, men vi styrer selv antal - måske Nissen har glemt at tjekke for negative tal?

```
Du har i øjeblikket 1000 JULESNE på din konto
Hvad vil du købe?
        1) Julelys (85 JULESNE)
        2) Gavepapir (40 JULESNE)
        3) Sneskovl (230 JULESNE)
        4) Juletræ (760 JULESNE)
        5) Flag (1000000 JULESNE)
> 4

Hvor mange vil du købe?
> -100000

Du har købt -100000 stk. Juletræ for i alt -76000000 JULESNE

Du har i øjeblikket 76001000 JULESNE på din konto
```

Nu har vi mere end rigeligt på kontoen til at købe flaget!

```
> 5
Du har købt flaget for 1000000 JULESNE:
NC3{hv4d_sk3t3_d3r_4lt_bl3v_uds0lg7_på_10_m1n?!?}
```

**Flag**

`NC3{hv4d_sk3t3_d3r_4lt_bl3v_uds0lg7_på_10_m1n?!?}`
