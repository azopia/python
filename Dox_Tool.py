import time, os, colorama, requests, json, webbrowser
from colorama import Fore, Back, Style, init

init()

BLUE = Fore.BLUE
CYAN = Fore.CYAN
RED = Fore.RED
GREEN = Fore.GREEN
BLUE = Fore.BLUE
PINK = Fore.MAGENTA
WHITE = Fore.WHITE

def clear():
	os.system('clear')

def ip_recon():
	clear()
	print(f"""
{CYAN}██{BLUE}╗{CYAN}██████{BLUE}╗     {CYAN}██████{BLUE}╗ {CYAN}███████{BLUE}╗ {CYAN}██████{BLUE}╗ {CYAN}██████{BLUE}╗ {CYAN}███{BLUE}╗   {CYAN}██{BLUE}╗
{CYAN}██{BLUE}║{CYAN}██{BLUE}╔══{CYAN}██{BLUE}╗    {CYAN}██{BLUE}╔══{CYAN}██{BLUE}╗{CYAN}██{BLUE}╔════╝{CYAN}██{BLUE}╔════╝{CYAN}██{BLUE}╔═══{CYAN}██{BLUE}╗{CYAN}████{BLUE}╗  {CYAN}██{BLUE}║
{CYAN}██{BLUE}║{CYAN}██████{BLUE}╔╝    {CYAN}██████{BLUE}╔╝{CYAN}█████{BLUE}╗  {CYAN}██{BLUE}║     {CYAN}██{BLUE}║   {CYAN}██{BLUE}║{CYAN}██{BLUE}╔{CYAN}██{BLUE}╗ {CYAN}██{BLUE}║
{CYAN}██{BLUE}║{CYAN}██{BLUE}╔═══╝     {CYAN}██{BLUE}╔══{CYAN}██{BLUE}╗{CYAN}██{BLUE}╔══╝  {CYAN}██{BLUE}║     {CYAN}██{BLUE}║   {CYAN}██{BLUE}║{CYAN}██{BLUE}║╚{CYAN}██{BLUE}╗{CYAN}██{BLUE}║
{CYAN}██{BLUE}║{CYAN}██{BLUE}║         {CYAN}██{BLUE}║  {CYAN}██{BLUE}║{CYAN}███████{BLUE}╗╚{CYAN}██████{BLUE}╗╚{CYAN}██████{BLUE}╔╝{CYAN}██{BLUE}║ ╚{CYAN}████{BLUE}║
{BLUE}╚═╝╚═╝         ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
""")
	host = input(f'{CYAN}Enter IP{BLUE}:{CYAN} ')
	r = requests.get(f"https://ipinfo.io/{host}?token=92c86362684fd1")
	res = r.json()
	print(f'{BLUE}╔═════════════════════════════════╗')
	print(f'{BLUE}║ {RED}IP:{CYAN} ' + res['ip'])
	print(f'{BLUE}║ {RED}Hostname:{CYAN} ' + res['hostname'])
	print(f'{BLUE}║ {RED}City:{CYAN} ' + res['city'])
	print(f'{BLUE}║ {RED}Region:{CYAN} ' + res['region'])
	print(f'{BLUE}║ {RED}Country:{CYAN} ' + res['country'])
	print(f'{BLUE}║ {RED}Geo:{CYAN} ' + res['loc'])
	print(f'{BLUE}║ {RED}Org:{CYAN} ' + res['org'])
	print(f'{BLUE}║ {RED}Postal:{CYAN} ' + res['postal'])
	print(f'{BLUE}║ {RED}Timezone:{CYAN} ' + res['timezone'])
	print(f'{BLUE}╚═════════════════════════════════╝')
	time.sleep(10)
	menu()


def number_recon():
	clear()
	print(f"""
{CYAN}███{BLUE}╗   {CYAN}██{BLUE}╗{CYAN}██{BLUE}╗   {CYAN}██{BLUE}╗{CYAN}███{BLUE}╗   {CYAN}███{BLUE}╗{CYAN}██████{BLUE}╗ {CYAN}███████{BLUE}╗{CYAN}██████{BLUE}╗     {CYAN}██████{BLUE}╗ {CYAN}███████{BLUE}╗ {CYAN}██████{BLUE}╗ {CYAN}██████{BLUE}╗ {CYAN}███{BLUE}╗   {CYAN}██{BLUE}╗
{CYAN}████{BLUE}╗  {CYAN}██{BLUE}║{CYAN}██{BLUE}║   {CYAN}██{BLUE}║{CYAN}████{BLUE}╗ {CYAN}████{BLUE}║{CYAN}██{BLUE}╔══{CYAN}██{BLUE}╗{CYAN}██{BLUE}╔════╝{CYAN}██{BLUE}╔══{CYAN}██{BLUE}╗    {CYAN}██{BLUE}╔══{CYAN}██{BLUE}╗{CYAN}██{BLUE}╔════╝{CYAN}██{BLUE}╔════╝{CYAN}██{BLUE}╔═══{CYAN}██{BLUE}╗{CYAN}████{BLUE}╗  {CYAN}██{BLUE}║
{CYAN}██{BLUE}╔{CYAN}██{BLUE}╗ {CYAN}██{BLUE}║{CYAN}██{BLUE}║   {CYAN}██{BLUE}║{CYAN}██{BLUE}╔{CYAN}████{BLUE}╔{CYAN}██{BLUE}║{CYAN}██████{BLUE}╔╝{CYAN}█████{BLUE}╗  {CYAN}██████{BLUE}╔╝    {CYAN}██████{BLUE}╔╝{CYAN}█████{BLUE}╗  {CYAN}██{BLUE}║     {CYAN}██{BLUE}║   {CYAN}██{BLUE}║{CYAN}██{BLUE}╔{CYAN}██{BLUE}╗ {CYAN}██{BLUE}║
{CYAN}██{BLUE}║╚{CYAN}██{BLUE}╗{CYAN}██{BLUE}║{CYAN}██{BLUE}║   {CYAN}██{BLUE}║{CYAN}██{BLUE}║╚{CYAN}██{BLUE}╔╝{CYAN}██{BLUE}║{CYAN}██{BLUE}╔══{CYAN}██{BLUE}╗{CYAN}██{BLUE}╔══╝  {CYAN}██{BLUE}╔══{CYAN}██{BLUE}╗    {CYAN}██{BLUE}╔══{CYAN}██{BLUE}╗{CYAN}██{BLUE}╔══╝  {CYAN}██{BLUE}║     {CYAN}██{BLUE}║   {CYAN}██{BLUE}║{CYAN}██{BLUE}║╚{CYAN}██{BLUE}╗{CYAN}██{BLUE}║
{CYAN}██{BLUE}║ ╚{CYAN}████{BLUE}║╚{CYAN}██████{BLUE}╔╝{CYAN}██{BLUE}║ ╚═╝ {CYAN}██{BLUE}║{CYAN}██████{BLUE}╔╝{CYAN}███████{BLUE}╗{CYAN}██{BLUE}║  {CYAN}██{BLUE}║    {CYAN}██{BLUE}║  {CYAN}██{BLUE}║{CYAN}███████{BLUE}╗╚{CYAN}██████{BLUE}╗╚{CYAN}██████{BLUE}╔╝{CYAN}██{BLUE}║ ╚{CYAN}████{BLUE}║
{BLUE}╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
""")
	number = input(f'{CYAN}Enter Number{BLUE}:{CYAN} ')
	r = requests.get(f"https://api.telnyx.com/anonymous/v2/number_lookup/{number}")
	res = r.json()['data']
	print(f'{BLUE}╔═════════════════════════════════╗')
	print(f'{BLUE}║ {RED}National Format:{CYAN} ' + res['country_code'])
	print(f'{BLUE}║ {RED}National Format:{CYAN} ' + res['national_format'])
	print(f'{BLUE}║ {RED}Phone Number:{CYAN} ' + res['phone_number'])
	res = r.json()['data']['carrier']
	print(f'{BLUE}║ {RED}Mobile Country Code:{CYAN} ' + res['mobile_country_code'])
	print(f'{BLUE}║ {RED}Mobile Network Code:{CYAN} ' + res['mobile_network_code'])
	print(f'{BLUE}║ {RED}Name:{CYAN} ' + res['name'])
	print(f'{BLUE}║ {RED}Type:{CYAN} ' + res['type'])
	print(f'{BLUE}╚═════════════════════════════════╝')
	time.sleep(10)
	menu()

def social_recon():
	clear()
	print(f"""
{CYAN}███████{BLUE}╗ {CYAN}██████{BLUE}╗  {CYAN}██████{BLUE}╗{CYAN}██{BLUE}╗ {CYAN}█████{BLUE}╗ {CYAN}██{BLUE}╗         {CYAN}██████{BLUE}╗ {CYAN}███████{BLUE}╗ {CYAN}██████{BLUE}╗ {CYAN}██████{BLUE}╗ {CYAN}███{BLUE}╗   {CYAN}██{BLUE}╗
{CYAN}██{BLUE}╔════╝{CYAN}██{BLUE}╔═══{CYAN}██{BLUE}╗{CYAN}██{BLUE}╔════╝{CYAN}██{BLUE}║{CYAN}██{BLUE}╔══{CYAN}██{BLUE}╗{CYAN}██{BLUE}║         {CYAN}██{BLUE}╔══{CYAN}██{BLUE}╗{CYAN}██{BLUE}╔════╝{CYAN}██{BLUE}╔════╝{CYAN}██{BLUE}╔═══{CYAN}██{BLUE}╗{CYAN}████{BLUE}╗  {CYAN}██{BLUE}║
{CYAN}███████{BLUE}╗{CYAN}██{BLUE}║   {CYAN}██{BLUE}║{CYAN}██{BLUE}║     {CYAN}██{BLUE}║{CYAN}███████{BLUE}║{CYAN}██{BLUE}║         {CYAN}██████{BLUE}╔╝{CYAN}█████{BLUE}╗  {CYAN}██{BLUE}║     {CYAN}██{BLUE}║   {CYAN}{CYAN}██{BLUE}║{CYAN}██{BLUE}╔{CYAN}██{BLUE}╗ {CYAN}██{BLUE}║
{BLUE}╚════{CYAN}██{BLUE}║{CYAN}██{BLUE}║   {CYAN}██{BLUE}║{CYAN}██{BLUE}║     {CYAN}██{BLUE}║{CYAN}██{BLUE}╔══{CYAN}██{BLUE}║{CYAN}██{BLUE}║         {CYAN}██{BLUE}╔══{CYAN}██{BLUE}╗{CYAN}██{BLUE}╔══╝  {CYAN}██{BLUE}║     {CYAN}██{BLUE}║   {CYAN}██{BLUE}║{CYAN}██{BLUE}║╚{CYAN}██{BLUE}╗{CYAN}██{BLUE}║
{CYAN}███████{BLUE}║╚{CYAN}██████{BLUE}╔╝╚{CYAN}██████{BLUE}╗{CYAN}██{BLUE}║{CYAN}██{BLUE}║  {CYAN}██{BLUE}║{CYAN}███████{BLUE}╗    {CYAN}██{BLUE}║  {CYAN}██{BLUE}║{CYAN}███████{BLUE}╗╚{CYAN}██████{BLUE}╗╚{CYAN}██████{BLUE}╔╝{CYAN}██{BLUE}║ ╚{CYAN}████{BLUE}║
{BLUE}╚══════╝ ╚═════╝  ╚═════╝╚═╝╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝
""")
	user = input(f'{CYAN}Enter Username{BLUE}:{CYAN} ')
	webbrowser.open('https://pipl.com/search/?q='+user+'+')
	time.sleep(2)
	webbrowser.open('https://www.facebook.com/search/top/?init=quick&q='+user+' ')
	time.sleep(2)
	webbrowser.open('https://www.spokeo.com/'+user+'-')
	time.sleep(2)
	webbrowser.open('https://www.flickr.com/search/people/?username='+user+' ')
	time.sleep(2)
	webbrowser.open('https://www.linkedin.com/pub/dir/'+user+'/')
	time.sleep(2)
	webbrowser.open('https://plus.google.com/s/'+user+' '+'/people')
	time.sleep(2)
	webbrowser.open('https://www.tumblr.com/search/'+user+'+')
	time.sleep(2)
	webbrowser.open('http://www.youtube.com/results?search_query='+user+'+')
	time.sleep(2)
	webbrowser.open('https://www.peekyou.com/'+user+'_')
	time.sleep(2)
	webbrowser.open('https://twitter.com/search?f=users&vertical=default&q= '+user+' ')
	time.sleep(2)
	webbrowser.open('https://www.beenverified.com/lp/e030ee/1/loading?utm_id=peekyou_Peekyou_Contact_Address_Results_Button&age=&bvid=&city=&fn='+user+'&ln=')
	time.sleep(2)
	webbrowser.open('https://www.peoplelooker.com/lp/5ee6b8/1/loading?utm_id=peekyou_peekyou_PL_phonebook_widget_web&fn='+user+'&ln='+'&city=&state=&age=&bvid=&utm_source=peekyou&utm_medium=channel_partner&utm_campaign=peekyou_PL_phonebook_widget_web&utm_content=static#.')
	time.sleep(2)
	webbrowser.open('https://myspace.com/search?q='+user+' ')
	time.sleep(2)
	webbrowser.open('https://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui='+user+'+')
	time.sleep(2)
	webbrowser.open(f'http://www.libramemoria.com/avis/?Nom={user}')
	time.sleep(2)
	webbrowser.open(f'https://thatsthem.com/name/{user}')
	menu()

def dox_format():
	clear()
	reason = str(input(f'{CYAN}Reason{BLUE}:{CYAN} '))
	your_name = str(input(f'{CYAN}Dox Creator Name{BLUE}:{CYAN} '))
	print(f'{RED}<About>')
	full_name = str(input(f'{CYAN}Full Name{BLUE}:{CYAN} '))
	main_users = str(input(f'{CYAN}Main Usernames{BLUE}:{CYAN} '))
	home_address = str(input(f'{CYAN}Home Address{BLUE}:{CYAN} '))
	city = str(input(f'{CYAN}City{BLUE}:{CYAN} '))
	zip_postal = str(input(f'{CYAN}Zip/Postal{BLUE}:{CYAN} '))
	state_province = str(input(f'{CYAN}State/Province{BLUE}:{CYAN} '))
	country = str(input(f'{CYAN}Country{BLUE}:{CYAN} '))
	print(f'{RED}<Relatives>')
	print(f'{RED}<Mom>')
	mom_social_media = str(input(f'{CYAN}Social Media{BLUE}:{CYAN} '))
	print(f'{RED}<Dad>')
	dad_social_media = str(input(f'{CYAN}Social Media{BLUE}:{CYAN} '))
	print(f'{RED}<Sister(s)>')
	sis_social_media = str(input(f'{CYAN}Social Media{BLUE}:{CYAN} '))
	print(f'{RED}<Brother(s)>')
	bro_social_media = str(input(f'{CYAN}Social Media{BLUE}:{CYAN} '))
	print(f'{RED}<Cousin(s)>')
	cousins = str(input(f'{CYAN}Cousin(s) Name(s){BLUE}:{CYAN} '))
	print(f'{RED}<Close Friend(s)>')
	close_friends = str(input(f'{CYAN}Close Friend(s) Name(s){BLUE}:{CYAN} '))
	print(f'{RED}<Occupancy>')
	job = str(input(f'{CYAN}Job{BLUE}:{CYAN} '))
	mom_job = str(input(f'{CYAN}Moms Job{BLUE}:{CYAN} '))
	dad_job = str(input(f'{CYAN}Dads Job{BLUE}:{CYAN} '))
	sis_job = str(input(f'{CYAN}Sisters Job{BLUE}:{CYAN} '))
	bro_job = str(input(f'{CYAN}Brothers Job{BLUE}:{CYAN} '))
	print(f'{RED}<Social Media>')
	youtube = str(input(f'{CYAN}Youtube{BLUE}:{CYAN} '))
	facebook = str(input(f'{CYAN}Facebook{BLUE}:{CYAN} '))
	skype = str(input(f'{CYAN}Skype{BLUE}:{CYAN} '))
	twitter = str(input(f'{CYAN}Twitter{BLUE}:{CYAN} '))
	instagram = str(input(f'{CYAN}Instagram{BLUE}:{CYAN} '))
	myspace = str(input(f'{CYAN}Myspace{BLUE}:{CYAN} '))
	pastebin = str(input(f'{CYAN}Pastebin{BLUE}:{CYAN} '))
	tumblr = str(input(f'{CYAN}Tumblr{BLUE}:{CYAN} '))
	pinterest = str(input(f'{CYAN}Pinterest{BLUE}:{CYAN} '))
	linkedin = str(input(f'{CYAN}LinkedIn{BLUE}:{CYAN} '))
	print(f'{RED}<Emails>')
	work_email = str(input(f'{CYAN}Work Email{BLUE}:{CYAN} '))
	home_email = str(input(f'{CYAN}Home Email{BLUE}:{CYAN} '))
	emails = str(input(f'{CYAN}Other Emails{BLUE}:{CYAN} '))
	print(f'{RED}<Telephone Numbers>')
	work_number = str(input(f'{CYAN}Work Number{BLUE}:{CYAN} '))
	cell_number = str(input(f'{CYAN}Cell Number{BLUE}:{CYAN} '))
	home_number = str(input(f'{CYAN}Home Number{BLUE}:{CYAN} '))
	print(f'{RED}<Education>')
	school = str(input(f'{CYAN}School Name{BLUE}:{CYAN} '))
	school_address = str(input(f'{CYAN}School Address{BLUE}:{CYAN} '))
	school_number = str(input(f'{CYAN}School Number{BLUE}:{CYAN} '))
	school_website = str(input(f'{CYAN}School Website{BLUE}:{CYAN} '))
	print(f'{RED}<ISP Info>')
	ip_address = str(input(f'{CYAN}IP Address{BLUE}:{CYAN} '))
	ip_location = str(input(f'{CYAN}IP Location{BLUE}:{CYAN} '))
	lat_long = str(input(f'{CYAN}Latitude/Longitude{BLUE}:{CYAN} '))
	isp = str(input(f'{CYAN}ISP{BLUE}:{CYAN} '))
	domain = str(input(f'{CYAN}Domain{BLUE}:{CYAN} '))
	area_code = str(input(f'{CYAN}Area Code{BLUE}:{CYAN} '))
	time.sleep(2)
	clear()
	print('Creating Dox')
	time.sleep(0.5)
	print('#')
	time.sleep(0.5)
	clear()
	print('Creating Dox')
	print('####')
	clear()
	print('Creating Dox')
	print('########')
	clear()
	print('Creating Dox')
	print('##############')
	clear()
	print('Creating Dox')
	print('###################')
	clear()
	a = f"""

=======================================================================================================================================
= Reason for DOX: {reason}
=======================================================================================================================================

=== Dox by {your_name} ===

----- About -----
Full Name: {full_name}
Main Usernames: {main_users}
Home Address: {home_address}
City: {city}
Zip/Postal: {zip_postal}
State/Province: {state_province}
Country: {country}

----- Relatives -----
Mom:
Social Media: {mom_social_media}
-
Dad:
Social Media: {dad_social_media}
-
Sister(s):
Social Media: {sis_social_media}
-
Brother(s):
Social Media: {bro_social_media}
-
Cousins: {cousins}
-
Close Friend(s): {close_friends}

----- Occupancy -----
Persons Job: {job}
Moms Job: {mom_job}
Dads Job: {dad_job}
Sisters Job: {sis_job}
Brothers Job: {bro_job}

----- Social Media -----
Youtube: {youtube}
-
Facebook: {facebook}
-
Skype: {skype}
-
Twitter: {twitter}
-
Instagram: {instagram}
-
Myspace: {myspace}
-
Pastebin: {pastebin}
-
Tumblr: {tumblr}
-
Pinterest: {pinterest}
-
LinkedIn: {linkedin}

----- Emails -----
Work Email: {work_email}
-
Home Email: {home_email}
-
Other Emails: {emails}

----- Telephone Numbers -----
Work #: {work_number}
Cell #: {cell_number}
Home #: {home_number}

----- Education -----
School: {school}
Address: {school_address}
School #: {school_number}
Website: {school_website}

----- ISP Information -----
IP Address: {ip_address}
Location: {ip_location}
Latitude & Longitude: {lat_long}
ISP: {isp}
Domain: {domain}
Area Code: {area_code}
"""
	print(a)
	time.sleep(2)
	clear()
	f = open(f"{full_name}'s Dox.txt", "x")
	f = open(f"{full_name}'s Dox.txt", "w")
	f.write(a)
	f.close()
	time.sleep(2)
	menu()

def banner():
	clear()
	print(f"""
{CYAN}██████{BLUE}╗  {CYAN}██████{BLUE}╗ {CYAN}██{BLUE}╗  {CYAN}██{BLUE}╗{CYAN}████████{BLUE}╗ {CYAN}██████{BLUE}╗  {CYAN}██████{BLUE}╗ {CYAN}██{BLUE}╗     
{CYAN}██{BLUE}╔══{CYAN}██{BLUE}╗{CYAN}██{BLUE}╔═══{CYAN}██{BLUE}╗╚{CYAN}██{BLUE}╗{CYAN}██{BLUE}╔╝╚══{CYAN}██{BLUE}╔══╝{CYAN}██{BLUE}╔═══{CYAN}██{BLUE}╗{CYAN}██{BLUE}╔═══{CYAN}██{BLUE}╗{CYAN}██{BLUE}║     
{CYAN}██{BLUE}║  {CYAN}██{BLUE}║{CYAN}██{BLUE}║   {CYAN}██{BLUE}║ ╚{CYAN}███{BLUE}╔╝    {CYAN}██{BLUE}║   {CYAN}██{BLUE}║   {CYAN}██{BLUE}║{CYAN}██{BLUE}║   {CYAN}██{BLUE}║{CYAN}██{BLUE}║     
{CYAN}██{BLUE}║  {CYAN}██{BLUE}║{CYAN}██{BLUE}║   {CYAN}██{BLUE}║ {CYAN}██{BLUE}╔{CYAN}██{BLUE}╗    {CYAN}██{BLUE}║   {CYAN}██{BLUE}║   {CYAN}██{BLUE}║{CYAN}██{BLUE}║   {CYAN}██{BLUE}║{CYAN}██{BLUE}║     
{CYAN}██████{BLUE}╔╝╚{CYAN}██████{BLUE}╔╝{CYAN}██{BLUE}╔╝ {CYAN}██{BLUE}╗   {CYAN}██{BLUE}║   ╚{CYAN}██████{BLUE}╔╝╚{CYAN}██████{BLUE}╔╝{CYAN}███████{BLUE}╗
{BLUE}╚═════╝  ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
""")
	print(f'		{Fore.GREEN}+ {CYAN}Made By Azopia{BLUE}#{CYAN}0001 {RED}<3 {Fore.GREEN}+')

def options():
	print(f"""
{BLUE}╔════════════════════════╗
{BLUE}║                        {BLUE}║
{BLUE}║  {BLUE}[{CYAN}1{BLUE}]{CYAN} IP Recon          {BLUE}║
{BLUE}║  {BLUE}[{CYAN}2{BLUE}]{CYAN} Number Recon      {BLUE}║
{BLUE}║  {BLUE}[{CYAN}3{BLUE}]{CYAN} Social Recon      {BLUE}║
{BLUE}║  {BLUE}[{CYAN}4{BLUE}]{CYAN} Dox Format        {BLUE}║
{BLUE}║                        {BLUE}║
{BLUE}╚════════════════════════╝
""")
	x = input(f'{CYAN}Enter option{BLUE}[{CYAN}1{BLUE}/{CYAN}2{BLUE}/{CYAN}3{BLUE}/{CYAN}4{BLUE}/{CYAN}5{BLUE}]:{CYAN} ')
	if x == '1':
		ip_recon()
	elif x == '2':
		number_recon()
	elif x == '3':
		social_recon()
	elif x == '4':
		dox_format()
	elif x == '5':
		dos_menu()

def menu():
	clear()
	banner()
	options()

menu()


time.sleep(100)
