import requests
import json
# Replace 'origin' with the platform you want to query (e.g., 'origin', 'xbl', 'psn')
platform = 'PC'
# Replace 'MrAzn69' with the player name you want to query
player_name = 'shikisandroid'
#{PLATFORM}/{NAME}'.format(PLATFORM='origin', NAME='MrAzn69')
#url = f'https://api.mozambiquehe.re/bridge?auth=YOUR_API_KEY&player={}&platform={}'.format(PLATFORM='origin', NAME ='MrAzn69')
url = f'https://api.mozambiquehe.re/bridge?player={player_name}&platform={platform}'

headers = {
    'Authorization': '3b015cf39484ba5e62f91ae59a0d594d'
}

response = requests.get(url, headers=headers)

print('Request was successful:', response.ok)
#print(dir(response))

#print(response.text)

with open('shikisandroid.txt', 'w',encoding='utf-8') as file:
    # Convert the variable to a string and write it to the file.
    file.write(str(response.text))

with open('shikisandroid.txt', 'r',encoding='utf-8') as json_file:
    player_json= json.load(json_file)

playername = player_json.get('global').get('name')
print(playername)