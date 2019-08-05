import discord, requests, time

r = requests.get('https://api.weather.gov/alerts/active/zone/<find your county code ex. NYZ001>')

hold = r.json()

client = discord.Client()

@client.event
async def on_ready():
	if hold['features'] != []:
		headline = hold['features']['properties']['headline']
		severity = hold['features']['properties']['severity']
		description = hold['features']['properties']['description']
		client.loop.create_task(alarm_message())
	else:
		quit()	

async def alarm_message():
	await client.wait_until_ready()
	for i in client.servers:
		for mem in i.members:
			if str(mem)  != "Emergency#1478":
				await client.send_message(mem,content = headline)
				await client.send_message(mem,content = severity)
				await client.send_message(mem,content = description)
	quit()

'''	if r.ok:
		print("hello")
		hold = r.json()
		if hold['features'] == []:
			print('yea')
			trigger = True
			headline = hold['features']#['properties']["parameters"]['NWSheadline']
	#		description = hold['features']['properties']['description']
			for i in client.servers:
				for mem in i.members:
					if str(mem)  != "Emergency#1478":
						print(mem)
						client.send_message(mem,content ="test")
'''

client.run('token here')
