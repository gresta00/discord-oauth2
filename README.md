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
## Get user id from token
```

```
