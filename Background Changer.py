## Change League of Legends Background

## LCU Driver
from lcu_driver import Connector
# Timer
import time

connector = Connector()
backgroundId = ""

## Get League of Legends account nickname! 
async def nickname(connection):
    nick = await connection.request('get', '/lol-summoner/v1/current-summoner')

    if nick.status != 200:
        print(nick)
    else:
        nickname = await nick.json()
        print(f"Welcome, {nickname['displayName']}")

async def change_background(connection):
    backgroundId = input("Background ID: ")
    background = await connection.request('post', "/lol-summoner/v1/current-summoner/summoner-profile", data={"key": "backgroundSkinId", "value": backgroundId} )

    if background.status != 200:
        print("An error has ocurred...")
    else:
        print("Success!!")
        time.sleep(5)

@connector.ready
async def connect(connection):
    print('LCU API is ready to be used.')

    await nickname(connection)
    await change_background(connection)

connector.start()