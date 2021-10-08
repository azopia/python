import random, json

amount = int(input("Enter Amount: "))
types = input("[admin/public]: ")

if types.lower() == 'admin' or types.lower() == 'a':
	pick = 'admin'
elif types.lower() == 'public' or types.lower() == 'p':
	pick = 'public'
else:
	exit()

num = 0
codes = []
while num < amount:
	try:
		letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
		code = ''.join(random.choice(letters) for i in range(25))
		codes.append(code)
		num = num + 1
	except:
		break

for x in codes:
	with open('auth_keys.json', 'r') as f:
		auth_keys = json.load(f)

	auth_keys[str(x)] = pick

	with open('auth_keys.json', 'w') as f:
		json.dump(auth_keys, f, indent=4)