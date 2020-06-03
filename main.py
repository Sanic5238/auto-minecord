#  _________             .__        
# /   _____/____    ____ |__| ____  
# \_____  \\__  \  /    \|  |/ ___\ 
# /        \/ __ \|   |  \  \  \___ 
#/_______  (____  /___|  /__|\___  >
#        \/     \/     \/        \/
#   _____  .__                                     .___   _________            .__        __   
#  /     \ |__| ____   ____   ____  ___________  __| _/  /   _____/ ___________|__|______/  |_ 
# /  \ /  \|  |/    \_/ __ \_/ ___\/  _ \_  __ \/ __ |   \_____  \_/ ___\_  __ \  \____ \   __\
#/    Y    \  |   |  \  ___/\  \__(  <_> )  | \/ /_/ |   /        \  \___|  | \/  |  |_> >  |  
#\____|__  /__|___|  /\___  >\___  >____/|__|  \____ |  /_______  /\___  >__|  |__|   __/|__|  
#        \/        \/     \/     \/                 \/          \/     \/         |__|

try:
    import os
    import shelve
    if os.path.filename('config/config.dat') == True and os.path.filesize('config/config.dat') > 0:
        with shelve.open('config/config') as config:
            token = config['token']
            botid = config['botid']
            botchanid = config['botchan']
    else:
    	print('Running First Time Setup!')
    	config['token'] = input('Please input your user token.\n')
    	config['botid'] = input('Please input the ID of the bot.\n')
    	config['botchan'] = input('Please input the channel you want to use.\n')
    	print('Please restart')
    	quit()

except Exception as e:
	print(e)
	quit()


import discord
import asyncio

botchan = None
name = None

async def setup():
	await asyncio.sleep(10)
	global botchanid
	global botchan

	botchan = client.get_channel(botchanid)
	name = client.user.name

async def mine():
	await asyncio.sleep(15)

	global botchan
	global name

	while True:
		await botchan.send('m!mine')
		await asyncio.sleep(5)

async def fight():
	await asyncio.sleep(15)

	global botchan
	global name

	while True:
		await botchan.send('m!fight')
		await asyncio.sleep(30)

client.loop.create_task(fight())
client.loop.create_task(setup())
client.loop.create_task(mine())
try:
	client.run(token, bot=False)
except:
	print('Token was incorrect please input a new token')
	with shelve.open('config/config') as config:
		config['token'] = input('Please input your user token.\n')
