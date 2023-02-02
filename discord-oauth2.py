import requests
import os

def get_token(code : str , client_id : str , client_secret : str , redirect_uri : str) -> dict:

    headers = {
      'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = f'client_id={client_id}&client_secret={client_secret}&grant_type=authorization_code&code={code}&redirect_uri={redirect_uri}'
    response = requests.post('https://discordapp.com/api/oauth2/token',
                             headers=headers,
                             data=data)

    return response.json()

def add_to_guild(bot_token : str, access_token : str, userID : int, guildID : int , *roles) -> dict:
  url = f"https://discord.com/api/v10/guilds/{guildID}/members/{userID}"

  if roles == None:
    data = {
        "access_token": access_token,
    }
  else:
    if isinstance(roles , list):
        data = {
            "access_token": access_token,
            "roles": map(str , roles),
        }
    else:
        data = {
            "access_token": access_token,
            "roles": str(roles),
        }  

  headers = {"Authorization": f"Bot {bot_token}", 'Content-Type': 'application/json'}
  response = requests.put(url=url, headers=headers, json=data)

  return response.json()

def get_user_info(access_token : str) -> dict:
  url = f"https://discord.com/api/v10/users/@me"
  response = requests.get(url=url, headers={"Authorization": f"Bearer {access_token}", 'Content-Type': 'application/json'})

  return response.json()

def get_user_guilds(access_token : str, userID : int) -> dict:
    url = f"https://discord.com/api/v10/users/{userID}/guilds"
    response = requests.get(url=url, headers={"Authorization": f"Bearer {access_token}", 'Content-Type': 'application/json'})
 
    return response.json()

def get_guild_info(access_token : str, guildID : int) -> dict:
    url = f"https://discord.com/api/v10/guilds/{guildID}"
    response = requests.get(url=url, headers={"Authorization": f"Bearer {access_token}", 'Content-Type': 'application/json'})

    return response.json()

def get_guild_roles(access_token : str, guildID : int) -> dict:
    url = f"https://discord.com/api/v10/guilds/{guildID}/roles"
    response = requests.get(url=url, headers={"Authorization": f"Bearer {access_token}", 'Content-Type': 'application/json'})
    
    return response.json()

def get_guild_channels(access_token : str, guildID : int) -> dict:
   
    url = f"https://discord.com/api/v10/guilds/{guildID}/channels"
    response = requests.get(url=url, headers={"Authorization": f"Bearer {access_token}", 'Content-Type': 'application/json'})

    return response.json()

def get_guild_emojis(access_token : str, guildID : int) -> dict:
    
    url = f"https://discord.com/api/v10/guilds/{guildID}/emojis"
    response = requests.get(url=url, headers={"Authorization": f"Bearer {access_token}", 'Content-Type': 'application/json'})

    return response.json()

def get_guild_members(access_token : str, guildID : int) -> dict:
    url = f"https://discord.com/api/v10/guilds/{guildID}/members"
    response = requests.get(url=url, headers={"Authorization": f"Bearer {access_token}", 'Content-Type': 'application/json'})

    return response.json()

def get_guild_invites(access_token : str, guildID : int) -> dict:
    url = f"https://discord.com/api/v10/guilds/{guildID}/invites"
    response = requests.get(url=url, headers={"Authorization": f"Bearer {access_token}", 'Content-Type': 'application/json'})

    return response.json()
    
def get_guild_presences(access_token : str, guildID : int) -> dict:
    url = f"https://discord.com/api/v10/guilds/{guildID}/presences"
    response = requests.get(url=url, headers={"Authorization": f"Bearer {access_token}", 'Content-Type': 'application/json'})
    
    return response.json()

def get_guild_voice_states(access_token : str, guildID : int) -> dict:
    url = f"https://discord.com/api/v10/guilds/{guildID}/voice-states"
    response = requests.get(url=url, headers={"Authorization": f"Bearer {access_token}", 'Content-Type': 'application/json'})

    return response.json()
    
def get_guild_bans(access_token : str, guildID : int) -> dict:
    url = f"https://discord.com/api/v10/guilds/{guildID}/bans"
    response = requests.get(url=url, headers={"Authorization": f"Bearer {access_token}", 'Content-Type': 'application/json'})

    return response.json()

def get_user_friends(access_token : str, userID : int) -> dict:
    url = f"https://discord.com/api/v10/users/{userID}/friends"
    response = requests.get(url=url, headers={"Authorization" : f"Bearer {access_token}", 'Content-Type': 'application/json'})

    return response.json()

