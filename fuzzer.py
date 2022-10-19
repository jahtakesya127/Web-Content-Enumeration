import requests,argparse, concurrent, builtwith, sys, pyfiglet
import simple_colors as c
from concurrent.futures import ThreadPoolExecutor

print(pyfiglet.figlet_format('web \n content \n enumeration',  font='speed', justify='right'))

parser = argparse.ArgumentParser()
parser.add_argument('--url', type=str, required=True)
parser.add_argument('-w', '--wordlist', default=None, required=False)
parser.add_argument('-t', '--threads', default=20, type=int, required=False)
parser.add_argument('-hc', '--hide404', action='store_true')
parser.add_argument('-rh', '--headers', action='store_false')
parser.add_argument('--enum', action='store_false')
parser.add_argument('--ext', default="", type=str, required=False)
args = parser.parse_args()

url = args.url
filename = args.wordlist
threads = args.threads
hideStatusCode = args.hide404
rHeaders = args.headers
techID = args.enum
ext = args.ext

if rHeaders == True and filename == None:
	r = requests.get(url)
	print(c.magenta(r.headers))
	sys.exit(0)
if techID == True and filename == None:
	print(c.magenta(builtwith.parse(url)))
	sys.exit(0)
else:
	pass

f = open(filename)
def request(f):
	r =  (url +  "/" + f).replace('\n', '')
	r = requests.get(r)
	sc = r.status_code
	fullurl = (url + "/" + f).replace('\n','')
	if hideStatusCode == True:
		if sc == 200:
			print(c.green("[*] " + str(sc) + " " + fullurl , ['underlined', 'bright', 'italic']))
		else:
			pass	
	else:
		if sc == 200:
			print(c.green("[*] " + str(sc) + " " + fullurl , ['underlined', 'bright', 'italic']))
		else:
			print(c.red("[*] " + str(sc) + " " + fullurl , ['italic', 'bright']))	

with ThreadPoolExecutor(max_workers=threads) as executor:
	future_to_url = {executor.submit(request, i + ext) for i in f}
	


