## Import de modules

from utils import download_tweets

## Paramètres de la fonction
lang="ge"
since="2018-01-01"
#since="2021-01-01"
until="2021-02-01"

# Requête cash germanophone

query = '(bargeld OR banknoten OR banknote OR münze OR münzen OR kleingeld OR " bar " OR abhebungen OR abhebung OR geldautomat OR geldautomaten OR " GAA " OR schalter) AND (zahlung OR zahlungen OR zahlen OR bezahlungen OR bezahlung OR bezahlen OR kauf OR käufe OR kaufen OR abheben OR ausgeben OR ausgabe OR ausgaben)'

name_output = "query_ge_cash"
#download_tweets(query, lang,since,until, name_output)

# Requête cb anglophone

query = '(karte OR karten OR " CB " OR kontaktlos OR visa OR mastercard OR cashback OR " NFC " OR "Google Pay" OR ApplePay OR Paylib OR Lydia OR "Lyf Pay" OR  Alipay OR "Samsung Pay" OR "Stocard Pay" OR "mobiles bezahlen" OR schecks) AND ("zahlung" OR "zahlungen" OR "zahlen" OR bezahlung OR bezahlungen OR bezahlen OR kauf OR käufe OR kaufen OR abheben OR Überweisung OR überweisungen OR überweisen OR ausgeben OR ausgabe OR ausgaben)'

name_output = "query_ge_cb"
download_tweets(query, lang,since, until, name_output)

