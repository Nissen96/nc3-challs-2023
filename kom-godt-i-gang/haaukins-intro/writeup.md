# Writeup

Opret en profil på Haaukins og start introopgaven.
Følg instruktionerne til at finde opgaveserverens IP-adresse.

Ved forbindelse til serveren printes et lille banner med en enkelt karakter på en umiddelbart tilfældig placering.
Dette kan bekræftes ved at lave flere forbindelser og se, at karakterer printes på andre tilfældige placeringer:

```
$ nc 0.0.0.0 6346
################################################
                                   3            
################################################

$ nc 0.0.0.0 6346
################################################
                 u                              
################################################

$ nc 0.0.0.0 6346
################################################
                n                               
################################################
```

Mon ikke, det er karakterer fra flaget?
Vi kan skrive et lille script, der fortsætter med at oprette nye forbindelser og hive karakterer ud, indtil de alle er udfyldt (fuldt script kan ses i [solve.py](solution/solve.py)):

```py
flag = [32] * len("################################################")
remaining = len(flag)

while remaining > 0:
    with remote("0.0.0.0", 6346) as io:
        io.recvline()
        line = io.recvline()

    for i, c in enumerate(line):
        if c != " ":
            flag[i] = c
            if flag.count(32) < remaining:
                remaining -= 1
                print(bytes(flag).decode())
            break
```

*Note: Scriptet bruger `pwntools`, et Python library der egentlig er designet til binary exploitation, men som har et utroligt intuitivt og let anvendeligt API til client-server connections. Det er derfor anbefalelsesværdigt til alle typer opgaver, hvor man skal snakke sammen med en server.*

Køres scriptet får vi følgende output:

```
               _                                
               _                          4     
               _              t           4     
               _  _           t           4     
               _  _3          t           4     
             3 _  _3          t           4     
   {         3 _  _3          t           4     
   {         3 _  _3     k    t           4     
   {         3 _  _3r    k    t           4     
   {     f   3 _  _3r    k    t           4     
   {     f   3 _  _3r    k   _t           4     
   {     f   3 _  _3r    kl  _t           4     
   {     f   3 _  _3r    kl  _t         y 4     
   {     f   3 _  _3r d  kl  _t         y 4     
   {     f   3 _n _3r d  kl  _t         y 4     
   {     f   3 _n _3r_d  kl  _t         y 4     
   {     f   3 _n _3r_d  kl  _t         y 4m    
   { 0   f   3 _n _3r_d  kl  _t         y 4m    
   {g0   f   3 _n _3r_d  kl  _t         y 4m    
   {g0 t f   3 _n _3r_d  kl  _t         y 4m    
   {g0 t f   3t_n _3r_d  kl  _t         y 4m    
   {g0 t f   3t_nu_3r_d  kl  _t         y 4m    
   {g0 t f   3t_nu_3r_d  kl  _t     r   y 4m    
   {g0 t f   3t_nu_3r_d  kl  _t1    r   y 4m    
   {g0 t f   3t_nu_3r_d  kl  _t1    r   y 4m  ! 
   {g0 t_f   3t_nu_3r_d  kl  _t1    r   y 4m  ! 
   {g0 t_f   3t_nu_3r_d  kl  _t1    r   y 4m  !}
   {g0 t_f   3t_nu_3r_d  kl  _t1    r3  y 4m  !}
   {g0 t_f   3t_nu_3r_d  kl  _t1    r3_ y 4m  !}
   {g0 t_f   3t_nu_3r_d  kl4 _t1    r3_ y 4m  !}
   {g0 t_f   3t_nu_3r_d  kl4 _t1    r3_dy 4m  !}
   {g0 t_f n 3t_nu_3r_d  kl4 _t1    r3_dy 4m  !}
   {g0 t_f n 3t_nu_3r_d  kl4 _t1    r3_dy 4m1 !}
   {g0 t_f n 3t_nu_3r_d  kl4 _t1 _  r3_dy 4m1 !}
 C {g0 t_f n 3t_nu_3r_d  kl4 _t1 _  r3_dy 4m1 !}
NC {g0 t_f n 3t_nu_3r_d  kl4 _t1 _  r3_dy 4m1 !}
NC {g0 t_f n 3t_nu_3r_d  kl4 _t1 _  r3_dyn4m1 !}
NC {g0 t_f n 3t_nu_3r_d  kl4 _t1 _m r3_dyn4m1 !}
NC {g0 t_fun 3t_nu_3r_d  kl4 _t1 _m r3_dyn4m1 !}
NC {g0dt_fun 3t_nu_3r_d  kl4 _t1 _m r3_dyn4m1 !}
NC {g0dt_fun 3t_nu_3r_d  kl4r_t1 _m r3_dyn4m1 !}
NC {g0dt_fun 3t_nu_3r_d _kl4r_t1 _m r3_dyn4m1 !}
NC {g0dt_fun 3t_nu_3r_du_kl4r_t1 _m r3_dyn4m1 !}
NC {g0dt_fun 3t_nu_3r_du_kl4r_t1l_m r3_dyn4m1 !}
NC {g0dt_fund3t_nu_3r_du_kl4r_t1l_m r3_dyn4m1 !}
NC {g0dt_fund3t_nu_3r_du_kl4r_t1l_m3r3_dyn4m1 !}
NC3{g0dt_fund3t_nu_3r_du_kl4r_t1l_m3r3_dyn4m1 !}
NC3{g0dt_fund3t_nu_3r_du_kl4r_t1l_m3r3_dyn4m1k!}
```

**Flag**

`NC3{g0dt_fund3t_nu_3r_du_kl4r_t1l_m3r3_dyn4m1k!}`
