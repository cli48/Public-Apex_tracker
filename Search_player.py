import requests
import os
import json


def Player_Data_Extraction(platform,player_name):
    path = 'players'
    url = f'https://api.mozambiquehe.re/bridge?player={player_name}&platform={platform}'
    headers = {'Authorization':'3b015cf39484ba5e62f91ae59a0d594d'}
    response =requests.get(url, headers = headers)
    print('Request has been sent!')
    if response.ok == True:
        print('Data was recieved!',response.ok)
        player_info = response.text
        path = os.path.join(path,player_name) #path to save player name into folder to stalk
        #print(path)
        with open(f'{path}.txt','w',encoding='utf-8') as file:
            file.write(str(player_info))
        sequence(player_name)
    else:
        print(f'Player {player_name} not found...')
    
def download_image(url,player_name):
    response = requests.get(url)
    with open(f'images/{player_name}.png','wb') as file:
        file.write(response.content)

def Player_images(player_name): #grab player images
    folder_path = 'players'
    json_files = [file for file in os.listdir(folder_path) if file.endswith('.txt')]
    
    if f'{player_name}.txt' in json_files:
        file_path = os.path.join(folder_path, f'{player_name}.txt')
        with open(file_path, 'r',encoding='utf-8') as json_file:
            player_json= json.load(json_file)
            #print(player_data.get('global'))
        imgRANKURL = player_json.get('global').get('rank').get('rankImg')
        download_image(imgRANKURL,f'{player_name}_rankImg')
        imgAVATARURL = player_json.get('global').get('avatar')
        download_image(imgAVATARURL,f'{player_name}_AvatarImg')

def Player_Read_JSON(player_name): #get player data from JSON
    folder_path = 'players'
    json_files = [file for file in os.listdir(folder_path) if file.endswith('.txt')]
    
    if f'{player_name}.txt' in json_files:
        file_path = os.path.join(folder_path, f'{player_name}.txt')
        with open(file_path, 'r',encoding='utf-8') as json_file:
            player_json= json.load(json_file)
        #Data to be taken in 
        IGN = player_json.get('global').get('name')
        UID = player_json.get('global').get('uid')
        platform = player_json.get('global').get('platform')
        level = player_json.get('global').get('level')
        rankScore = player_json.get('global').get('rank').get('rankScore')
        rankName = player_json.get('global').get('rank').get('rankName')

        print(f'In game name: {IGN}\nUnique playerID: {UID}\nPlayer Platform: {platform}\nPlayer level: {level}\nRanked points: {rankScore}\nRank: {rankName}\n')
    else:
        print('Player not found')

def sequence(player_name): 
    Player_Read_JSON(player_name)
    Player_images(player_name)
    

#print(html_content.get('global').get('bans').get('remainingSeconds')) 
# platform = input("What platform you playing on?\n")
# player_name = input("What is your in game name?\n")
platform = 'PC'
player_name = 'shikisandroid'
Player_Data_Extraction(platform,player_name)
