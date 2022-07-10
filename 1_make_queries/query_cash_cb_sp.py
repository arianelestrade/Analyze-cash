## Import de modules

from utils import download_tweets

## Paramètres de la fonction
lang="sp"


# Requête cash espagnole 

query = '(efectivo OR metálico OR billetes OR billete OR moneda OR monedas OR dinero OR efectivo OR líquido OR retiradas OR retirada OR cajero OR cajeros OR " cajero automático " OR " caja " OR " cajas ") AND (" pago " OR pagos OR pagar OR abonos OR abono OR abonar OR compra OR compras OR comprar OR retirar OR gastar OR gasto OR gastos)'

since="2018-01-01"
until="2018-10-01"
name_output = "query_sp_cash_part4"
download_tweets(query, lang,since,until, name_output)

query = '(efectivo OR metálico OR billetes OR billete OR moneda OR monedas OR dinero OR efectivo OR líquido OR retiradas OR retirada OR cajero OR cajeros OR " cajero automático " OR " caja " OR " cajas ") AND (" pago " OR pagos OR pagar OR abonos OR abono OR abonar OR compra OR compras OR comprar OR retirar OR gastar OR gasto OR gastos)'

since="2018-01-01"
until="2019-04-01"
name_output = "query_sp_cash_part3"
# download_tweets(query, lang,since,until, name_output)

since="2018-01-01"
until="2019-10-01"
name_output = "query_sp_cash_part2"
# download_tweets(query, lang,since,until, name_output)

# Requête cb espagnole
since="2018-01-01"
until="2021-02-01"

query = 'tarjeta OR tarjetas OR " tarjeta de débito" OR "sin contacto" OR " visa " OR mastercard OR "dinero en efectivo" OR " NFC " OR "Google Pay" OR "ApplePay" OR "Paylib" OR "Lydia" OR "Lyf Pay" OR "Alipay" OR "Samsung Pay" OR "Stocard Pay" OR "pagos móviles" OR "cheques") AND (" pago " OR pagos OR pagar OR abono OR abonos OR abonar OR compra OR compras OR comprar OR retirar OR transferencia OR transferencias OR transferir OR gastar OR gasto OR gastos)'
name_output = "query_sp_cb"
#download_tweets(query, lang,since, until, name_output)




