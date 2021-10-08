import discord, random, time, requests

token = "ODY3ODc2NzEyODUwMTI4OTA3.YPnfLA.0UwMHvFzCaR1S3BBvQq257NjiE0"
client = commands.Bot(command_prefix = "gimme ")

@client.command()
async def nitro(ctx, amount: int = 20):
	num = 0
	while num < amount:
		try:
			letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
			code = ''.join(random.choice(letters) for i in range(16))
			await ctx.send("https://discord.gift/{}".format(code))
			num = num + 1
		except:
			pass

client.run(token)