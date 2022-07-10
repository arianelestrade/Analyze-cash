from datetime import date
import logging
import json
import os
import time
import re

import numpy as np
import geopandas as gpd
import pandas as pd
import tweepy
import preprocessor as p
import requests
import tqdm


def query_to_words(query):
    query = str.lower(query)
    query = query.replace("(", "").replace(")", "")
    query = query.replace('"', '')
    splitted = re.split(pattern=" or | and ", string=query)
    splitted = [word.strip() for word in splitted]
    return splitted
 

#def score_english(string):
#    return sum([word in WORDS_ENGLISH for word in string.split()])

def score_language(string, words):
    return sum([word in words for word in string.split()])

def clean_users_with_geoloc(users):     
    if(len(users)==len(np.unique(users['id_str']))):
        
        users = users.drop("Unnamed: 0", axis=1)
        users.columns = users.columns + "_profile"
        users = users.rename(columns={'id_str_profile' : 'user_id'})
         
        users["location_profile"] =  users.location_profile.str.lower().str.replace("\.|:|,|'|’", " ").str.replace(r'http\S+','').str.replace(r'tco+','')
        users["location_profile"] = " " + users["location_profile"] +" "
        
        result = users
        
    else:
        
        result = "erreur : les id_string ne sont pas uniques"
        print(result)
    
    return(result)

# Functions used by 2_geoloc_users

USER_FIELDS =  (
    "id_str", "name", "screen_name",
    "location", "profile_location", "description", "url",
    "protected", "verified", "created_at", "utf_offset", "time_zone", "geo_enabled", 
    "statuses_count", "lang"
)

p.set_options(p.OPT.URL, p.OPT.EMOJI, p.OPT.SMILEY)

def clean_location(string):
    string = p.clean(string)
    string = string.replace("|", ",")
    string = string.replace("#", "")
    string = string.replace("/", ",")
    #string = string.replace("\", ",")
    string = string.replace(";", ",")
    string = string.replace("~", " ")
    
    return string

def define_logger(logname="geoloc"):
    logging.basicConfig(
    filename=f'{logname}_{date.today().isoformat()}.log',level=logging.INFO, filemode="w",
    format='%(asctime)s;%(levelname)s;%(message)s',
    force=True
    )

def get_twitter_api():
    # voir : https://developer.twitter.com/en/docs/twitter-api/v1/rate-limits
    auth = tweepy.OAuthHandler("bXahkkxebXiTtjEURUUrKO17f", "a1Kw3GYB0UTajjGS7LYybYr4sTsRNfKrPvjQbgTAQJ37HBAmC7")
    auth.set_access_token("839396154790064130-7eEpLUX1qA5KHfUpshaHT6qRvWbqVT2", "D8IadK8BVYBMILBIOPdfxMdToTZM9McOZV9lkd7Op1JCE")
    api = tweepy.API(auth_handler=auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    
    return api

def save_user_profiles(api, list_users_id, fname = "users_profiles.csv", base_path=".", print_every=1000):
    
    os.makedirs(base_path, exist_ok=True)
    full_path = f"{base_path}/{fname}"
    
    try:
        os.remove(full_path)
    except:
        pass
    
    len_list = len(list_users_id)
    logging.info(f"Beginning parsing list of {len_list} user ids")
    # Create header
    pd.DataFrame([], columns=USER_FIELDS).to_csv(full_path, index=False, mode="a", header=True)

    # Add row for each user profile
    print("Add row for each user profile")
    for i, user_id in tqdm.tqdm(enumerate(list_users_id)):
        if print_every:
            logging.info(f"{i} user ids parsed so far") if (i % print_every) == 0 else None
        current_user = get_user(api, user_id)
        if current_user:
            pd.DataFrame([current_user]).to_csv(full_path, index=False, mode="a", header=False)
        else:
            pass
    logging.info(f"Finishing parsing list of {len_list} user ids")

def get_user(api, user_id):
    try:
        user_info = api.get_user(user_id)
    except tweepy.TweepError as err:
        logging.error(f"user_id:{user_id}, {err}")
        return
    else:
        return user_to_userful_dict(user_info)
    
def user_to_userful_dict(user):
    try:
        user_json = user._json
    except Exception:
        return None
    else:
        d = {
            key:user_json.get(key, None) 
            for key in USER_FIELDS
        }
    return d

def save_profiles_geoloc(locations_to_geoloc, fname, base_path=".", print_every=100, **kwargs):
    
    os.makedirs(base_path, exist_ok=True)
    full_path = f"{base_path}/{fname}"
    
    try:
        os.remove(full_path)
    except:
        pass
    
    len_list = len(locations_to_geoloc)
    logging.info(f"Beginning parsing list of {len_list} locations")
    
    pd.DataFrame([], columns=["json"]).to_csv(full_path, index=False)

    for i, location in tqdm.tqdm(enumerate(locations_to_geoloc.location)):
        if print_every:
            logging.info(f"{i} user geoloc parsed so far") if (i % print_every) == 0 else None
        geoloc = get_photon_geolocation(location, **kwargs)
        if geoloc is not None:
            df = pd.DataFrame([dict(json=json.dumps(geoloc))])
            df.to_csv(full_path, index=False, mode="a", header=False)
        else:
            logging.info(f"Location:{repr(location)} not found")
    
    logging.info(f"Finishing parsing list of {len_list} locations")

# avec API photon, données OpenStreetMap (https://photon.komoot.io/)
def get_photon_geolocation(location, limit=1, sleep=0.5, verbose=False):
    if verbose:
        print(f"Geoloc: {location}")
    url = f"https://photon.komoot.io/api/?q={location}&limit={limit}"
    r = requests.get(url=url)
    if sleep > 0:
        time.sleep(sleep)
    try:
        d = r.json()
        d["input_location"] = location
    except Exception:
        return None
    else:
        return d
    
def read_geoloc(fname, verbose=False):
    df = pd.read_csv(fname, engine="python")
    #return zip(df.json, df.json.apply(lambda s: json.loads(s)["input_location"]).to_list())
    out = []
    input_locations = df.json.apply(lambda s: json.loads(s)["input_location"]).to_list()
    for js, loc in zip(df.json, input_locations):
        try:
            gdf = gpd.GeoDataFrame.from_features(json.loads(js))
        except Exception as err:
            if verbose:
                print(f"Error:{err}; input: {js}")
        else:
            if gdf is not None:
                gdf["input_location"] = loc
            out += [gdf]
    gdf = pd.concat(out)
    gdf.set_crs("EPSG:4326", inplace=True)
    return gdf
