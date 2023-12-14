# Haaukins Intro

Dynamiske opgaver i NC3 CTF 2023 kører via CTF-platformen [Haaukins](https://ncctf.haaukins.dk).

**Lab Setup:**

Ved oprettelse af profil, får du adgang til egen instans på dit eget subnet. Du kan i øverste højre hjørne klikke `Get a lab` og vælge imellem `VPN` eller `Browser`. Dit lab er dit eget, og det er dermed kun dig, der har adgang til din egen instans.

Browser labbet giver dig adgang til en Kali Linux instans i din browser, hvorfra alle opgaver kan tilgås. VMen har en række værktøjer præinstalleret og har ikke internetadgang. Se `FAQ` i Haaukins for instruktion til copy+paste ind i boksen.

Vælges `VPN` skal du klikke `Download VPN Config` og hente Wireguard config fil ned. Se guide til installation i `FAQ` på Haaukins. På Linux kan med fordel bruges [install_wireguard.sh](https://raw.githubusercontent.com/Mymaqn/wireguardhaaukins/main/install_wireguard.sh) til Wireguard installation og [connectwireguard.py](https://raw.githubusercontent.com/Mymaqn/wireguardhaaukins/main/connectwireguard.py) til opsætning med config filen:

```bash
sudo python connectwireguard.py ./wg-conf-1.conf
```

**Challenge Access:**

Challenges starter alle som `Not running` og skal startes individuelt, når man vil løse dem. Hvis en opgave stopper med at virke, kan den resettes fra forsiden. Labbet resetter helt hver 5. time automatisk, men du kan forlænge denne tid fra forsiden, når der er under en time igen.

Nogle challenges har et hostname, fx `juletid.nc3` og kan tilgås gennem browser eller med netcat via dette. I Browser lab er det direkte tilgængeligt, i VPN skal du selv opdatere din `hosts` fil lokalt - se `Hosts` tab i Haaukins (husk at starte opgaven først).

I challenges uden hostname skal servicen findes med et `nmap` scan af dit lab subnet. I browser lab kan dit subnet findes med kommandoen `ip a` under `eth0`. I VPN står det i toppen af din downloadede config fil. Fremgangsmåden er beskrevet i opgaveteksten til `Haaukins Intro` på Haaukins.

**Sanity Check:**

Gav det mening? Så er det tid til et lille sanity check! Opret et lab på Haaukins, start opgaven `Haaukins Intro` og find den IP, der har en service kørende på port 6346.
Forbind til servicen for at få flaget!

**OBS: Alle flag skal submittes herinde på CTFd, ikke på Haaukins!**

[https://ncctf.haaukins.dk](https://ncctf.haaukins.dk)
