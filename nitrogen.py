
'''
This is a "nitro generator" it wont actually give you all real codes,
you may get a few but you would have to click on them individually.
Maybe try making a function that checks them via requests and only
sends active codes or sum idk have fun.
'''
import random

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
