import requests

# r = requests.get('https://apex.tracker.gg/')

# # print(r.text) #prints the entire https file

# print(dir(r)) #shows the fields and categories

# print(r.content)

# print(r.content)
# with open('comic.png','wb') as f: #reads and writes the byte data via 
#     f.write(r.content)



# #attempt
# username = "MrAzn69"

# # Format the URL with the entered username
# url = f"https://apex.tracker.gg/apex/profile/origin/{username}/overview"

# # Send GET request to the player's profile URL
# response = requests.get(url)

# print(dir(response))
# print(response.content)

# with open('MrAzn69.txt','wb') as f: #reads and writes the byte data via 
#     f.write(response.content)

#GET https://public-api.tracker.gg/v2/apex/standard/profile/origin/MrAzn69


# import requests

# api_key = '9c95bb04-0016-4031-9878-38667a1e1c48'
# headers = {
#     "Content-Type": "application/json",
#     'TRN-Api-Key': api_key
# }

# url = 'https://public-api.tracker.gg/v2/apex/standard/profile/{PLATFORM}/{NAME}'.format(PLATFORM='origin', NAME='MrAzn69')
# response = requests.get(url, headers=headers)

# # Process the response
# if response.status_code == 200:
#     data = response.json()
#     print(data)
#     # Do something with the data
# else:
#     print('Error:', response.status_code)












#3b015cf39484ba5e62f91ae59a0d594d
import requests
from bs4 import BeautifulSoup
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

with open('MrAzn69.txt', 'w') as file:
    # Convert the variable to a string and write it to the file.
    file.write(str(response.text))

html_content = response.json()
#print(html_content)
#poopy = BeautifulSoup(html_content,'html.parser')

# for link in html_content: #getting the individual JSONs header
#     print(link)


#print(html_content.get('global').get('bans').get('remainingSeconds')) 

# for link in html_content.get('legends'):
#     print(link)

# for key,value in html_content.items():
#      print(key,value)

# print(html_content.get('total'))
# with open('Lindalovy.txt', 'w') as file:
#     # Convert the variable to a string and write it to the file.
#     file.write(str(response.content))

#print(html_content.get('legends'))       
# links = poopy.find_all('a')
# print(poopy)
# for link in links:
#     print(link['href'])  # Print the value of the 'href' attribute for each link
