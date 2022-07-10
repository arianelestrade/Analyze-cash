## Import de modules

from utils import download_tweets

## Paramètres de la fonction
lang="fr"
since="2018-01-01"
until="2021-02-01"

# Requête cash francophone

query='(espece OR especes OR billets OR billet OR piece OR pieces OR monnaie OR cash OR liquide OR retraits OR retrait OR distributeur OR distributeurs OR " DAB " OR guichet OR guichets) AND (paiement OR paiements OR payer OR reglements OR reglement OR regler OR achat OR achats OR acheter OR retirer OR depenser OR depense OR depenses)'
name_output="query_fr_cash"
download_tweets(query, lang,since,until, name_output)

# https://github.com/aio-libs/aiohttp/issues/3904
# https://stackoverflow.com/questions/59162321/exception-handling-from-imported-package

# Requête cb francophone

query='(carte OR cartes OR " CB " OR "sans contact" OR " visa " OR mastercard OR "cash back" OR " NFC " OR "Google Pay" OR "ApplePay" OR "Paylib" OR "Lydia" OR "Lyf Pay" OR "Alipay" OR "Samsung Pay" OR "Stocard Pay" OR "paiements mobiles" OR "chèques") AND (paiement OR paiements OR payer OR reglement OR reglements OR regler OR achat OR achats OR acheter OR retirer OR virement OR virements OR virer OR depenser OR depense OR depenses)'
name_output="query_fr_cb"
download_tweets(query, lang,since, until, name_output)

