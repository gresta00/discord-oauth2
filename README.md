# discord-oauth2
Python library for using Discord OAuth2
# How to use
## Arrange the files as below
```
./
├─ main.py
└─ discord-oauth2.py
```
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
