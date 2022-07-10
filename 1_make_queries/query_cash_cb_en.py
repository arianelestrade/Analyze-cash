## Import de la fonction

from utils import download_tweets

## Paramètres de la fonction
lang="en"
since="2018-01-01"
#since="2021-01-01"
until="2021-02-01"

# Requête cash anglophone

query = '(cash OR banknotes OR banknote OR " note " OR " coin " OR " coins " OR money OR currency OR withdrawals OR withdrawal OR ATM OR ATMs OR "cash machines" OR branch OR counter) AND (payment OR payments OR " pay " OR settle OR " buy " OR purchases OR purchase OR withdraw OR spend OR expenses OR spending OR expenditure)'
name_output = "query_en_cash"
#download_tweets(query, lang,since,until, name_output)

# Requête cb anglophone

query = '(card OR cards OR "contactless" OR " visa " OR mastercard OR "cash back" OR " NFC " OR "Google Pay" OR "ApplePay" OR "Paylib" OR "Lydia" OR "Lyf Pay" OR "Alipay" OR "Samsung Pay" OR "Stocard Pay" OR "mobile payments" OR "cheques") AND (payment OR payments OR " pay " OR settle OR " buy " OR purchases OR purchase OR withdraw OR spend OR expenses OR spending OR expenditure)'
name_output = "query_en_cb"
download_tweets(query, lang,since, until, name_output)

