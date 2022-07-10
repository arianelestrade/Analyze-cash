import twint
import os
import nest_asyncio # pour résoudre le souci de compatibilité avec jupyter
nest_asyncio.apply()


def download_tweets(query, lang, since, until, name_output):
    fpath = f"/home/cash/data/queries/{name_output}.csv"
    
    if os.path.isfile(fpath) : 
        print(f"File {fpath} already exists")
    else : 
        config = twint.Config(
            Search=query,
            Lang=lang,
            Since=since,
            Until=until,
            Store_csv=True,
            Output=fpath,
            Hide_output=True
        )
        twint.run.Search(config)
    print("Request finished!")

    return

