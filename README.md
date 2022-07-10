# Analyze-cash

Analyse the use of cash versus cashless payments with Twitter data 

2 main means of payment can be distinguished:

    Fiduciary money: coins and banknotes.
    non-cash money: cheques, bank transfers, direct debits and cards.

These 2 means of payment are associated with 2 queries:

    cash in the cash query
    cashless money in the cb query

Warning: As it stands, most scripts analyse French-language queries, not foreign-language queries.

Queries

A query corresponds to a set of words. The result of the query is the set of tweets containing this combination of words. To obtain this data, the project relies on the twint package.

However, the use of this package is complicated by the fact that the collection (relative to the query) sometimes stops at certain arbitrary dates, even though data is available before that date. It has therefore been necessary to modify some scripts accordingly.

The results of these queries are stored in CSV format in the location data/queries. This has not been done, but it might be beneficial to put this data into an SQL database (e.g. SQLite) to allow faster loading or to load only certain observations.

All the scripts used to carry out the queries are in scripts/1_make_queries. Also, the query scripts are available by language: fr, ge, sp, en. The translation of these keywords into the different languages was done with the help of the Banque de France's team of translators.

Once the collection is complete, a cleaning stage is necessary. The cleaning is done at two levels:

    Exclude tweets containing certain (regular) expressions
    Exclude tweets from users who are not in France (Germany, Spain, UK for foreign language queries)

The scripts related to these cleaning operations can be found in scripts/2_prep_queries.

Also, a relevance score is calculated at the tweet level by counting the number of words of the query appearing in this tweet.

Organisation of scripts

The scripts directory contains the scripts used to query, prepare and analyse the data. The directory contains 3 sub-directories:

    1_make_queries: makes queries from twint.
    2_prep_queries: cleans the data
    3_analysis: different independent scripts to analyse the data.

Downloaded data and outputs are not available.
