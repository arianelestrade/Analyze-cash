## Import de modules

from utils import download_tweets

## Paramètres de la fonction
lang="fr"
since="2018-01-01"
until="2021-05-01"

# Requête disparition du cash

query='(espece OR especes OR billets OR billet OR piece OR pieces OR monnaie OR cash OR liquide OR retraits OR retrait OR distributeur OR distributeurs OR " DAB " OR guichet OR guichets) AND (disparition OR fin OR recul OR declin OR suppression OR extinction OR mort OR substitution OR remplacement OR avenir OR futur OR dématérialisation OR abolition OR abrogation OR arrêt)'

name_output="query_disparition_cash_part1"
download_tweets(query, lang,since,until, name_output)

#since="2018-01-01"
#until="2018-09-01"
#query='(espece OR especes OR billets OR billet OR piece OR pieces OR monnaie OR cash OR liquide OR retraits OR retrait OR distributeur OR #distributeurs OR " DAB " OR guichet OR guichets) AND (disparition OR fin OR recul OR declin OR suppression OR extinction OR mort OR #substitution OR remplacement OR avenir OR futur OR dématérialisation OR abolition OR abrogation OR arrêt)'
#name_output="query_disparition_cash_part2"
#download_tweets(query, lang,since,until, name_output)

# https://github.com/aio-libs/aiohttp/issues/3904
# https://stackoverflow.com/questions/59162321/exception-handling-from-imported-package


