import numpy as np
import pandas as pd
import ast

movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')

movie_credits = movies.merge(credits, on='title')

#genres,id,keywords,title,overview,cast,crew

movie_credits=movie_credits[['genres','id','keywords','title','overview','cast','crew']]


movie_credits.dropna(inplace=True)

def convert(obj):
    L=[]
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L

def convert3(obj,limit=3):
    L=[]
    val=0
    for i in ast.literal_eval(obj):
        if val<limit:
            L.append(i['name'])
            val+=1
    return L

def job_finder(obj):
    L=[]
    for i in ast.literal_eval(obj):
        if i['job']=='Director':
            L.append(i['name'])
            break
    return L

movie_credits['genres']=movie_credits['genres'].apply(convert)
movie_credits['keywords']=movie_credits['keywords'].apply(convert)
movie_credits['cast']=movie_credits['cast'].apply(convert3)
movie_credits['crew']=movie_credits['crew'].apply(job_finder)
movie_credits['overview']=movie_credits['overview'].apply(lambda x:x.split())

movie_credits['genres'].apply(lambda x:[i.replace(" ","") for i in x])
movie_credits['keywords'].apply(lambda x:[i.replace(" ","") for i in x])
movie_credits['cast'].apply(lambda x:[i.replace(" ","") for i in x])
movie_credits['crew'].apply(lambda x:[i.replace(" ","") for i in x])
movie_credits['overview'].apply(lambda x:[i.replace(" ","") for i in x])

movie_credits['tags']=movie_credits['overview']

df=movie_credits[['id','title','tags']]


print(movie_credits['overview'])
