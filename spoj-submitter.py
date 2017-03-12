import sys,requests,json,pathlib,time
username = "" #Specify your username here
password = "" #Specify your password here
if(username=="" or password==""):
	print('Looks like you haven\'t specified the username and password yet. Please edit line 2 and 3 of this script')
	exit(0)
try:
	qid = sys.argv[1]
	file = sys.argv[2]
except:
	print("Failed to start web scrapping. Please give a valid set of arguments.")
	print("Format: python spoj-submitter.py <problemcode> <filename>")
	print("Sample use: python spoj-submitter.py FOXLINGS myfile.cpp")
	exit(0)

#Code to check is the file exists
pfile = pathlib.Path(file)
if not pfile.is_file():
	print('\nNo such file \''+file+'\' found. Please check for the location')
	exit(0)
#End code for file exists

#Check the language code
lcodes = {1: 'C++ (gcc 6.3)', 2: 'Pascal (gpc 20070904)', 3: 'Perl (perl 5.24.1)', 4: 'Python (cpython 2.7.13)', 5: 'Fortran (gfortran 6.3)', 6: 'Whitespace (wspace 0.3)', 7: 'Ada95 (gnat 6.3)', 8: 'Ocaml (ocamlopt 4.01)', 9: 'Intercal (ick 0.3)', 10: 'Java (HotSpot 8u112)', 11: 'C (gcc 6.3)', 12: 'Branf**k (bff 1.0.6)', 13: 'Assembler 32 (nasm 2.12.01)', 14: 'Clips (clips 6.24)', 15: 'Prolog (swi 7.2.3)', 16: 'Icon (iconc 9.5.1)', 17: 'Ruby (ruby 2.3.3)', 18: 'Scheme (stalin 0.3)', 19: 'Pike (pike 8.0)', 20: 'D (gdc 6.3)', 21: 'Haskell (ghc 8.0.1)', 22: 'Pascal (fpc 3.0.0)', 23: 'Smalltalk (gst 3.2.5)', 24: 'JAR (JavaSE 6)', 25: 'Nice (nicec 0.9.13)', 26: 'Lua (luac 5.3.3)', 27: 'C# (gmcs 4.6.2)', 28: 'Bash (bash 4.4.5)', 29: 'PHP (php 7.1.0)', 30: 'Nemerle (ncc 1.2.0)', 31: 'Common Lisp (sbcl 1.3.13)', 32: 'Common Lisp (clisp 2.49)', 33: 'Scheme (guile 2.0.13)', 34: 'C99 (gcc 6.3)', 35: 'JavaScript (rhino 1.7.7)', 36: 'Erlang (erl 19)', 38: 'TCL (tcl 8.6)', 39: 'Scala (scala 2.12.1)', 40: 'SQLite (sqlite 3.16.2)', 41: 'C++ (g++ 4.3.2)', 42: 'Assembler 64 (nasm 2.12.01)', 43: 'Objective-C (gcc 6.3)', 44: 'C++14 (gcc 6.3)', 45: 'Assembler 32 (gcc 6.3 )', 46: 'Sed (sed 4)', 47: 'Kotlin (kotlin 1.0.6)', 48: 'Dart (dart 1.21)', 50: 'VB.net (mono 4.6.2)', 62: 'Text (plain text)', 81: 'C (clang 4.0)', 82: 'C++14 (clang 4.0)', 83: 'Objective-C (clang 4.0)', 84: 'D (ldc 1.1.0)', 85: 'Swift (swift 3.0.2)', 91: 'CoffeeScript (coffee 1.12.2)', 92: 'Fantom (fantom 1.0.69)', 93: 'Rust (rust 1.14.0)', 94: 'Pico Lisp (pico 16.12.8)', 95: 'Racket (racket 6.7)', 96: 'Elixir (elixir 1.3.3)', 97: 'Scheme (chicken 4.11.0)', 98: 'Gosu (gosu 1.14.2)', 99: 'Python (PyPy 2.6.0)', 102: 'D (dmd 2.072.2)', 104: 'AWK (gawk 4.1.3)', 105: 'AWK (mawk 1.3.3)', 107: 'Forth (gforth 0.7.3)', 108: 'Prolog (gnu prolog 1.4.5)', 110: 'BC (bc 1.06.95)', 111: 'Clojure (clojure 1.8.0)', 112: 'JavaScript (SMonkey 24.2.0)', 114: 'Go (go 1.7.4)', 115: 'Unlambda (unlambda 0.1.4.2)', 116: 'Python 3 (python  3.5)', 117: 'R (R 3.3.2)', 118: 'Cobol (opencobol 1.1.0)', 121: 'Groovy (groovy 2.4.7)', 122: 'Nim (nim 0.16.0)', 124: 'F# (mono 4.0.0)', 126: 'Python 3 nbc (python 3.4)', 127: 'Octave (octave 4.0.3)'}
slcodes = {1: 'C++ (gcc 6.3)', 4: 'Python (cpython 2.7.13)', 10: 'Java (HotSpot 8u112)', 11: 'C (gcc 6.3)', 17: 'Ruby (ruby 2.3.3)', 27: 'C# (gmcs 4.6.2)', 29: 'PHP (php 7.1.0)', 34: 'C99 (gcc 6.3)', 35: 'JavaScript (rhino 1.7.7)', 41: 'C++ (g++ 4.3.2)', 44: 'C++14 (gcc 6.3)', 62: 'Text (plain text)', 81: 'C (clang 4.0)', 82: 'C++14 (clang 4.0)', 99: 'Python (PyPy 2.6.0)', 112: 'JavaScript (SMonkey 24.2.0)', 116: 'Python 3 (python  3.5)', 126: 'Python 3 nbc (python 3.4)'}

while(1==1):
	lang = input("\nEnter the language code (0 to list the popular languages, -1 to list all): ")
	lang = int(lang)
	if(lang==0):
		print()
		for key in slcodes:
			print(str(key)+ "\t:\t" +lcodes[key])
		print()
	elif(lang==-1):
		print()
		for key in lcodes:
			print(str(key)+ "\t:\t" +lcodes[key])
		print()
	else:
		if(lang in lcodes):
			break
		else:
			print("\nInvalid code. Try again..")
			continue
#End language check

print("\nLanguage selected: "+lcodes[lang])
print("Specified File: "+file)

#Common headers for all requests
header = {'Host':'www.spoj.com','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Language':'en-US,en;q=0.5','Accept-Encoding':'gzip, deflate','Referer':'http://www.spoj.com/'}
#End common headers

#Check is the problem exists
url = 'http://www.spoj.com/submit/'+qid+'/'
try:
	r=requests.get(url,headers=header,allow_redirects=False)
except:
	print("Connection error. Make sure you are connected to Internet")
	exit(0)
if(r.status_code==404):
	print('\nNo such problem was found on the server.')
	exit(0)

print("Specified problem: "+qid)
#End check for problem

#Send login data
login_data = {'next_raw':'','autologin':'1','login_user':username,'password':password}
try:
	r=requests.post('http://www.spoj.com/login/',data=login_data,headers=header,allow_redirects=False)
except:
	print("\nConnection error. Falied to login")
	exit(0)
header['Cookie'] = r.headers['Set-Cookie'].split('; ')[0]
#Login data sent and session ID captured

#Check if login successful
if(len(r.headers['Set-Cookie'].split('autologin_hash'))<2):
	print('\nLogin failed')
	exit(0)
else:
	print('\nLogin successful')
#End code to check login

#All checks have passed now. Upload the file
file = {'subm_file': open(file,'rb')}
upload_data = {'lang': lang, 'problemcode': qid, 'file': '', 'submit':'Submit!'}
try:
	r = requests.post('http://www.spoj.com/submit/complete/', headers=header,files=file,data=upload_data)
except:
	print("\nConnection error. Problem couldn't be submitted")
	exit(0)
print("\nSolution submitted..")
#File upload complete

def clean(s):
	s = s.replace("\\n", "")
	s = s.replace("\\t", "")
	s = s.replace(" ","")
	s = s.strip()
	return s

#Check for the the result
print("\nRunning Judge..\n")
url = 'http://www.spoj.com/status/'+qid+','+username+'/'
while(1==1):
	try:
		r=str(requests.get(url,headers=header).content)
	except:
		print("Connection error. Failed to fetch status")
		exit(0)
	status=int(clean((r.split('" status="'))[1].split('"')[0]))
	if(status<10):
		time.sleep(3)
		continue
	s=""
	if(status==15):
		s="Accepted"
	elif(status==14):
		s="Wrong Answer"
	elif(status==13):
		s="Time Limit Exceeded"
	elif(status==12):
		s="Runtime Error"
	elif(status==11):
		s="Compilation Error"
	elif(status==10):
		s="Disqualified"
	else:
		s="Unknown status"
	t=clean((r.split('best solutions">'))[1].split('<')[0])
	m=clean((r.split('id="statusmem_'))[1].split('>')[1].split('<')[0])
	print("Status : "+s)
	print("Time : "+t)
	print("Memory : "+m)
	break
