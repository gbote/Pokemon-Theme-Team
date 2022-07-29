from random import randint
from django.shortcuts import render
import requests as requestAPI
import pprint
import random

def index(request):
    def get_info(url):
        my_api = requestAPI.get(url)                    #requests api information 
        poki_data = my_api.json()
        return {'name': poki_data['species']['name'], 'base_exp': poki_data['base_experience'], 'pok_type': poki_data['types'][0]['type']['name'], 'pic': poki_data['sprites']['front_default']}  
    #this gets the pokemon type url

    def get_type(url):
        poki_api = requestAPI.get(url)
        poki_data = poki_api.json()
        # here you return the type
        return poki_data['types'][0]['type']['url']         #https://pokeapi.co/api/v2/type/3
         
    def get_five_poki(url):
        my_api = requestAPI.get(url)
        poki_data = my_api.json()
        arr_nums = random.sample(range(1, 50), 5)
        arr_urls = [poki_data['pokemon'][nums]['pokemon']['url'] for nums in arr_nums]
        return [get_info(i) for i in arr_urls]

    random_number = str(randint(1,500))
    
    first_pokemon_link = 'https://pokeapi.co/api/v2/pokemon/' + random_number

    first_pokemon_info = get_info(first_pokemon_link)

    first_pic = first_pokemon_info['pic']

    type_link = get_type(first_pokemon_link)

    five_pic_link = get_five_poki(type_link)
    


    return render(request,'index.html',{'pic': first_pic, 'info': first_pokemon_info, 'list': five_pic_link})
