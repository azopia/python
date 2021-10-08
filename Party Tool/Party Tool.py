import PySimpleGUI as sg
import requests, json, random, nmap, argparse, os, asyncio, webbrowser
from aiohttp import ClientSession, web
from xbox.webapi.authentication.manager import AuthenticationManager
from xbox.webapi.authentication.models import OAuth2TokenResponse
from xbox.webapi.scripts import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, TOKENS_FILE
from xbox.webapi.api.client import XboxLiveClient
from xbox.webapi.common.exceptions import AuthenticationException
from xbox import *

ip_blacklist = ["1.1.1.1"]

sg.theme('Dark')

global auth_mgr

def xresolve():
	resolve = [[sg.Text('Resolve User'), sg.Input(key='user'), sg.Button('Resolve')],
			   [sg.Text(size=(60,1), key='ips')]]

	window = sg.Window('Resolver', resolve)

	while True:
		event, values = window.read()
		if event == sg.WIN_CLOSED:
			break
		elif event == 'Resolve':
			window['ips'].update(' ')
			ips = []
			user = values['user']
			with open('xbox_resolves.json', 'r') as f:
				xbox = json.load(f)

			for x in xbox[user]:
				ips.append(x)

			window['ips'].update('Logged IPs: ' + ", " . join(ips))

def auth():
	queue = asyncio.Queue(1)


	async def auth_callback(request):
		error = request.query.get("error")
		if error:
			description = request.query.get("error_description")
			print(f"Error in auth_callback: {description}")
			return
		asyncio.create_task(queue.put(request.query["code"]))
		return web.Response(
			headers={"content-type": "text/html"},
			text="<script>window.close()</script>",
		)


	async def async_main(
		client_id: str, client_secret: str, redirect_uri: str, token_filepath: str
	):

		async with ClientSession() as session:
			auth_mgr = AuthenticationManager(
				session, client_id, client_secret, redirect_uri
			)

			if os.path.exists(token_filepath):
				with open(token_filepath, mode="r") as f:
					tokens = f.read()
				auth_mgr.oauth = OAuth2TokenResponse.parse_raw(tokens)
				await auth_mgr.refresh_tokens()

			if not (auth_mgr.xsts_token and auth_mgr.xsts_token.is_valid()):
				auth_url = auth_mgr.generate_authorization_url()
				webbrowser.open(auth_url)
				code = await queue.get()
				await auth_mgr.request_tokens(code)

			with open(token_filepath, mode="w") as f:
				f.write(auth_mgr.oauth.json())

			xbl_client = XboxLiveClient(auth_mgr)
			profile = await xbl_client.profile.get_profile_by_gamertag("Kyraqq")
			print('Profile under SomeGamertag gamer tag:')
			print(profile)
			print()

			friendslist = await xbl_client.people.get_friends_own()
			print('Your friends:')
			print(friendslist)
			print()

			presence = await xbl_client.presence.get_presence_batch(["2533274794093122", "2533274807551369"])
			print('Statuses of some random players by XUID:')
			print(presence)
			print()

			messages = await xbl_client.message.get_inbox()
			print('Your messages:')
			print(messages)
			print()


	def main():
		parser = argparse.ArgumentParser(description="Authenticate with XBL")
		parser.add_argument(
			"--tokens",
			"-t",
			default=TOKENS_FILE,
			help=f"Token filepath. Default: '{TOKENS_FILE}'",
		)
		parser.add_argument(
			"--client-id",
			"-cid",
			default=os.environ.get("CLIENT_ID", CLIENT_ID),
			help="OAuth2 Client ID",
		)
		parser.add_argument(
			"--client-secret",
			"-cs",
			default=os.environ.get("CLIENT_SECRET", CLIENT_SECRET),
			help="OAuth2 Client Secret",
		)
		parser.add_argument(
			"--redirect-uri",
			"-ru",
			default=os.environ.get("REDIRECT_URI", REDIRECT_URI),
			help="OAuth2 Redirect URI",
		)
		print(CLIENT_ID)
		print(CLIENT_SECRET)

		args = parser.parse_args()

		app = web.Application()
		app.add_routes([web.get("/auth/callback", auth_callback)])
		runner = web.AppRunner(app)

		loop = asyncio.get_event_loop()
		loop.run_until_complete(runner.setup())
		site = web.TCPSite(runner, "localhost", 8080)
		loop.run_until_complete(site.start())
		loop.run_until_complete(
			async_main(args.client_id, args.client_secret, args.redirect_uri, args.tokens)
		)


	if __name__ == "__main__":
		main()


def tcp_ping(host, port):
	r = requests.get(f'http://107.172.141.135/PyPr/api.php?&host={host}&port={port}')
	res = r.text.strip()
	pscan = [[sg.Text(f'Pinging {host} on Port {port}')],
			 [sg.Text(res)]]

	window = sg.Window('TCP Ping', pscan)

	while True:
		event, values = window.read()
		if event == sg.WIN_CLOSED:
			break

def ping(host):
	r = requests.get(f'https://api.hackertarget.com/nping/?q={host}')
	res = r.text.strip()
	pscan = [[sg.Text(f'Pinging {host}')],
			 [sg.Text(res)]]

	window = sg.Window('ICMP Ping', pscan)

	while True:
		event, values = window.read()
		if event == sg.WIN_CLOSED:
			break

def pscan(host):
	r = requests.get(f'https://api.hackertarget.com/nmap/?q={host}')
	res = r.text.strip()
	pscan = [[sg.Text(f'Scanning {host}')],
			 [sg.Text(res)]]

	window = sg.Window('Port Scan', pscan)

	while True:
		event, values = window.read()
		if event == sg.WIN_CLOSED:
			break

def gen(types, amount):
	num = 0
	codes = []
	while num < int(amount):
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

		if types == 'admin':
			auth_keys[str(x)] = 'admin'
		elif types == 'public':
			auth_keys[str(x)] = 'public'

		with open('auth_keys.json', 'w') as f:
			json.dump(auth_keys, f, indent=4)

def resolve(host):
	r = requests.get(f"https://ipinfo.io/{host}?token=92c86362684fd1")
	res = r.json()
	ip = res['ip']
	hostname = res['hostname']
	city = res['city']
	region = res['region']
	country = res['country']
	geo = res['loc']
	org = res['org']
	postal = res['postal']
	timezone = res['timezone']

	resolve = [[sg.Text(f'IP: {ip}')],
			   [sg.Text(f'Hostname: {hostname}')],
			   [sg.Text(f'City: {city}')],
			   [sg.Text(f'Region: {region}')],
			   [sg.Text(f'Country: {country}')],
			   [sg.Text(f'Geo: {geo}')],
			   [sg.Text(f'Org: {org}')],
			   [sg.Text(f'Postal: {postal}')],
			   [sg.Text(f'Timezone: {timezone}')]]

	window = sg.Window('Resolver', resolve)
	while True:
		event, values = window.read()
		if event == sg.WIN_CLOSED:
			break

def key_gen():
	auth = [[sg.Text('Amount of Keys')],
			[sg.Input(key='amount')],
			[sg.Button('Public Keys'), sg.Button('Admin Keys')]]

	window = sg.Window('Auth Key Gen', auth)

	while True:
		event, values = window.read()
		if event == 'Exit' or event == sg.WIN_CLOSED:
			break
		elif event == 'Public Keys':
			amount = values['amount']
			gen('public', amount)
		elif event == 'Admin Keys':
			amount = values['amount']
			gen('admin', amount)


def tools_page():
	tools = [[sg.Text('IPv4')],
			 [sg.Input(key='host')],
			 [sg.Text('Port')],
			 [sg.Input(key='port')],
			 [sg.Text(size=(40,1), key='tools_error')],
			 [sg.Button('Resolve'), sg.Button('Ping'), sg.Button('TCP-Ping'), sg.Button('Pscan'), sg.Button('X-Resolve'), sg.Button('Clear'), sg.Button('Back')]]

	window = sg.Window('Tools', tools)

	while True:
		event, values = window.read()
		if event == 'Exit' or event == sg.WIN_CLOSED:
			break
		elif event == 'Back':
			window.close()
			menu_page()
		elif event == 'Resolve':
			host = values['host']
			if host in ip_blacklist:
				window['tools_error'].update(f'The IP: {host} is Blacklisted')
			elif host not in ip_blacklist:
				resolve(host)
			else:
				window['tools_error'].update(f'There was an error please try again')
		elif event == 'Pscan':
			host = values['host']
			pscan(host)
		elif event == 'Ping':
			host = values['host']
			ping(host)
		elif event == 'TCP-Ping':
			host = values['host']
			port = values['port']
			tcp_ping(host, port)
		elif event == 'Clear':
			window.close()
			tools_page()
		elif event == 'X-Resolve':
			xresolve()

def hub_page():
	hub = [[sg.Text('Party Tool')],
		   [sg.Text(size=(40,1), key='invite_toggle')],
		   [sg.Text(size=(40,1), key='hub_error')],
		   [sg.Button('Pull Party'), sg.Button('Kick User'), sg.Button('Nuke Party'), sg.Button('Toggle Invite'), sg.Button('Back')]]

	window = sg.Window('Party Tool', hub)

	while True:
		event, values = window.read()
		if event == 'Exit' or event == sg.WIN_CLOSED:
			break
		elif event == 'Back':
			window.close()
			menu_page()
		elif event == 'Pull Party':
			sg.popup('Working on')
		elif event == 'Kick User':
			sg.popup('Working on')
		elif event == 'Nuke Party':
			sg.popup('Working on')
		elif event == 'Toggle Invite':
			sg.popup('Working on')

def settings_page():
	settings = [[sg.Text('Xbox Live User')],
				[sg.Text(size=(40,1), key='settings_error')],
				[sg.Button('Link Xbox'), sg.Button('Back')]]

	window = sg.Window('Settings', settings)

	while True:
		event, values = window.read()
		if event == 'Exit' or event == sg.WIN_CLOSED:
			break
		elif event == 'Back':
			window.close()
			menu_page()
		elif event == 'Link Xbox':
			auth()

def admin_page():
	admin = [[sg.Text(f'Logged in as {user_name}')],
			 [sg.Text(size=(40,5), key='results')],
			 [sg.Text(size=(40,1), key='admin_error')],
			 [sg.Text('User')],
			 [sg.Input(key='user_edit')],
			 [sg.Button('Set Admin'), sg.Button('Remove Admin'), sg.Button('View User'), sg.Button('View Users'), sg.Button('Delete User'), sg.Button('Key Gen'), sg.Button('Back')]]

	window = sg.Window('Admin Panel', admin)

	while True:
		event, values = window.read()
		if event == 'Exit' or event == sg.WIN_CLOSED:
			break
		elif event == 'Back':
			window.close()
			menu_page()
		elif event == 'Set Admin':
			window['admin_error'].update(' ')
			window['results'].update(' ')
			user_edit = values['user_edit']
			with open('users.json', 'r') as f:
				users = json.load(f)

				if user_edit not in users:
					window['admin_error'].update(f'User: {user_edit} not found')
				elif users[user_edit][3] == "True":
					window['admin_error'].update(f'{user_edit} is already Admin')
				else:
					password = users[user_edit][0]
					email = users[user_edit][1]
					admin = users[user_edit][2]
					token = users[user_edit][3]
					users[user_edit] = [password, email, "True", token]

					with open('users.json', 'w') as f:
						json.dump(users, f, indent=4)
		elif event == 'Remove Admin':
			window['admin_error'].update(' ')
			window['results'].update(' ')
			user_edit = values['user_edit']
			with open('users.json', 'r') as f:
				users = json.load(f)

				if user_edit not in users:
					window['admin_error'].update(f'User: {user_edit} not found')
				elif users[user_edit][3] == "False":
					window['admin_error'].update(f'{user_edit} is not an Admin')
				else:
					password = users[user_edit][0]
					email = users[user_edit][1]
					admin = users[user_edit][2]
					token = users[user_edit][3]
					users[user_edit] = [password, email, "False", token]


					with open('users.json', 'w') as f:
						json.dump(users, f, indent=4)
		elif event == 'View User':
			window['admin_error'].update(' ')
			user_edit = values['user_edit']
			with open('users.json', 'r') as f:
				users = json.load(f)

				if user_edit not in users:
					window['admin_error'].update(f'User: {user_edit} not found')
				else:
					password = users[user_edit][0]
					email = users[user_edit][1]
					admin = users[user_edit][2]
					token = users[user_edit][3]
					window['results'].update(f'Username: {user_edit}\nPassword: {password}\nEmail: {email}\nAdmin: {admin}\nAuth Key: {token}')
		elif event == 'Key Gen':
			key_gen()
		elif event == 'Delete User':
			window['admin_error'].update(' ')
			window['results'].update(' ')
			user_edit = values['user_edit']
			with open('users.json', 'r') as f:
				users = json.load(f)

				if user_edit not in users:
					window['admin_error'].update(f'User: {user_edit} not found')
				else:
					users.pop(user_edit)

					with open('users.json', 'w') as f:
						json.dump(users, f, indent=4)
		elif event == 'View Users':
			window['admin_error'].update(' ')
			window['results'].update(' ')
			with open('users.json', 'r') as f:
				users = json.load(f)

				user_list = []

				for x in users:
					user_list.append(x)

				window['results'].update(", " . join(user_list))

def menu_page():
	menu = [[sg.Text('Welcome')],
			[sg.Text('What would you like to do?')],
			[sg.Text(size=(40,1), key='menu_error')],
			[sg.Button('Party Tool'), sg.Button('Tools'), sg.Button('Settings'), sg.Button('Admin'), sg.Button('Exit')]]

	window = sg.Window('Menu', menu)

	while True:
		event, values = window.read()
		if event == 'Exit' or event == sg.WIN_CLOSED:
			break
		elif event == 'Party Tool':
			window.close()
			hub_page()
		elif event == 'Tools':
			window.close()
			tools_page()
		elif event == 'Settings':
			window.close()
			settings_page()
		elif event == 'Admin':
			with open('users.json', 'r') as f:
				admin = json.load(f)
				if admin[str(user_name)][2] == 'True':
					window.close()
					admin_page()
				else:
					window['menu_error'].update('You need to be Admin for this')

def register_page():
	register = [[sg.Text('Enter Username')],
				[sg.Input(key='new_username')],
				[sg.Text('Enter Password')],
				[sg.Input(key='new_password')],
				[sg.Text('Enter Email')],
				[sg.Input(key='new_email')],
				[sg.Text('Enter Auth Key')],
				[sg.Input(key='auth_key')],
				[sg.Text(size=(40,1), key='register_error')],
				[sg.Button('Create'), sg.Button('Exit')]]

	window = sg.Window('Register', register)

	while True:
		event, values = window.read()
		if event == 'Exit' or event == sg.WIN_CLOSED:
			break
		elif event == 'Back':
			window.close()
			menu_page()
		elif event == 'Create':
			new_username = values['new_username']
			new_password = values['new_password']
			new_email = values['new_email']
			auth_key = values['auth_key']
			with open('auth_keys.json', 'r') as f:
				auth_keys = json.load(f)
			if auth_key not in auth_keys:
				window['register_error'].update('Auth Key Invalid')
			elif auth_key in auth_keys:
				if auth_keys[auth_key] == 'admin':
					with open('users.json', 'r') as f:
						users = json.load(f)

					users[new_username] = [new_password, new_email, "True", auth_key]

					with open('users.json', 'w') as f:
						json.dump(users, f, indent=4)

					with open('auth_keys.json', 'r') as f:
						auth_keys = json.load(f)

					auth_keys.pop(str(auth_key))

					with open('auth_keys.json', 'w') as f:
						json.dump(auth_keys, f, indent=4)
					window.close()
					login_page()
				elif auth_keys[auth_key] == 'public':
					with open('users.json', 'r') as f:
						users = json.load(f)

					users[new_username] = [new_password, new_email, "False", auth_key]

					with open('users.json', 'w') as f:
						json.dump(users, f, indent=4)

					with open('auth_keys.json', 'r') as f:
						auth_keys = json.load(f)

					auth_keys.pop(str(auth_key))

					with open('auth_keys.json', 'w') as f:
						json.dump(auth_keys, f, indent=4)
					window.close()
					login_page()
				

def login_page():
	login = [[sg.Text('Enter Username')],
			 [sg.Input(key='username')],
			 [sg.Text('Enter Password')],
			 [sg.Input(key='password')],
			 [sg.Text(size=(40,1), key='login_error')],
			 [sg.Button('Login'), sg.Button('Register'), sg.Button('Exit')]]

	window = sg.Window('Login', login)

	while True:
		event, values = window.read()
		if event == 'Exit' or event == sg.WIN_CLOSED:
			break
		elif event == 'Register':
			window.close()
			register_page()
		elif event == 'Login':
			username = values['username']
			password = values['password']
			global user_name
			user_name = str(username[0:20])
			pass_word = str(password[0:20])
			with open('users.json', 'r') as f:
				login = json.load(f)
				if user_name not in login:
					window['login_error'].update('Incorrect Username')
				if pass_word == login[str(user_name)][0]:
					window.close()
					menu_page()
				elif user_name in login and pass_word != login[str(user_name)][0]:
					window['login_error'].update('Incorrect Password')
				else:
					window['login_error'].update('Incorrect Password')
			return user_name

login_page()