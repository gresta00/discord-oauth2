# discord-oauth2
Python library for using Discord OAuth2
This repository is incomplete and may contain many bugs.
# How to use
## How to setup
Place discord-oauth2.py in the same hierarchy as your main program file.
## Get access token from code
```
import discord-oauth2 as oauth2

tokens = oauth2.get_token("code" , "client_id" , "client_secret" , "redirect_uri")

access_token = tokens["access_token"]
refresh_token = tokens["refresh_token"]
```
## Get user data from token
```
import discord-oauth2 as oauth2
user_data = oauth2.get_user_info("access_token")

print(user_data)

user_id = user_data["id"]
user_name = user_data["name"]
```
## Example 1 : Add to guild
```
import discord-oauth2 as oauth2

access_token = "Here your token"

user_data = oauth2.get_user_info(access_token)

user_id = user_data["id"]

res = oauth2.add_to_guild(access_token, str(uid), "guild_id")

print(res)
```
## Example 2 : Get user guilds
```
import discord-oauth2 as oauth2

access_token = "Here your token"

user_data = oauth2.get_user_info(access_token)

user_id = user_data["id"]

user_guilds = oauth2.get_user_guilds(access_token , user_id)

print(user_guilds)
```
