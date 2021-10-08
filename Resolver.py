'''
This is a simple python gui ip geoloaction tool,
I was learning how to use pysimplegui and wanted
to work with an api so i made this.
'''
import PySimpleGUI as sg
import requests, json

blacklist = ["1.1.1.1"]
users = ["pynx", "root"]
pasws = ["iota", "root"]

sg.theme('Dark')


layout = [[sg.Text('Enter Username:'), sg.Input(key='username')],
		 [sg.Text('Enter Password:'), sg.Input(key='password')],
		 [sg.Text(size=(40,1), key='error')],
		 [sg.Button('Login'), sg.Button('Exit')]]


layout2 = [[sg.Text('Enter IP:'), sg.Input(key='host')],
		  [sg.Text(size=(40,1), key='ip')],
		  [sg.Text(size=(40,1), key='hostname')],
		  [sg.Text(size=(40,1), key='city')],
		  [sg.Text(size=(40,1), key='region')],
		  [sg.Text(size=(40,1), key='country')],
		  [sg.Text(size=(40,1), key='loc')],
		  [sg.Text(size=(40,1), key='org')],
		  [sg.Text(size=(40,1), key='postal')],
		  [sg.Text(size=(40,1), key='timezone')],
		  [sg.Button('Resolve'), sg.Button('Clear'), sg.Button('Exit')]]

window = sg.Window('Login', layout)

while True:
	event, values = window.read()
	if event == 'Exit' or event == sg.WIN_CLOSED:
		break
	elif event == 'Login':
		username = values['username']
		password = values['password']
		if username in users and password in pasws:
			window.close()
			sg.popup(f'Logged in as {username}')
			window = sg.Window('IP Resolver', layout2)
		else:
			window['error'].update('Incorrect Username or Password.')
	elif event == 'Resolve':
		host = values['host']
		if host in blacklist:
			window['ip'].update('Sorry this is a blacklisted IP')
			window['hostname'].update(' ')
			window['city'].update(' ')
			window['region'].update(' ')
			window['country'].update(' ')
			window['loc'].update(' ')
			window['org'].update(' ')
			window['postal'].update(' ')
			window['timezone'].update(' ')
		else:
			r = requests.get(f"https://ipinfo.io/{host}?token=92c86362684fd1")
			res = r.json()
			window['ip'].update(f'IP: ' + res['ip'])
			window['hostname'].update(f'Hostname: ' + res['hostname'])
			window['city'].update(f'City: ' + res['city'])
			window['region'].update(f'Region: ' + res['region'])
			window['country'].update(f'Country: ' + res['country'])
			window['loc'].update(f'Geo: ' + res['loc'])
			window['org'].update(f'Org: ' + res['org'])
			window['postal'].update(f'Postal: ' + res['postal'])
			window['timezone'].update(f'Timezone: ' + res['timezone'])
	elif event == 'Clear':
		window['ip'].update(' ')
		window['hostname'].update(' ')
		window['city'].update(' ')
		window['region'].update(' ')
		window['country'].update(' ')
		window['loc'].update(' ')
		window['org'].update(' ')
		window['postal'].update(' ')
		window['timezone'].update(' ')

window.close()
