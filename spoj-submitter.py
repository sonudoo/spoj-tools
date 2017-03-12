import sys,requests,json,pathlib
try:
	from bs4 import BeautifulSoup
except:
	print("Please install BeautifulSoup before you continue")
	exit(0)
try:
	username = sys.argv[1]
	password = sys.argv[2]
	qid = sys.argv[3]
	file = sys.argv[4]
	lang = sys.argv[5]
except:
	print("Failed to start web scrapping. Please give a set of arguments.")
	print("Format: python spoj-submitter.py <user> <pass> <problemcode> <filename> <languagecode>")
	print("Sample use: python spoj-submitter.py user pass FOXLINGS myfile.cpp ")
	exit(0)

#Check the language code
lcodes = {1: 'C++ (gcc 6.3)', 2: 'Pascal (gpc 20070904)', 3: 'Perl (perl 5.24.1)', 4: 'Python (cpython 2.7.13)', 5: 'Fortran (gfortran 6.3)', 6: 'Whitespace (wspace 0.3)', 7: 'Ada95 (gnat 6.3)', 8: 'Ocaml (ocamlopt 4.01)', 9: 'Intercal (ick 0.3)', 10: 'Java (HotSpot 8u112)', 11: 'C (gcc 6.3)', 12: 'Branf**k (bff 1.0.6)', 13: 'Assembler 32 (nasm 2.12.01)', 14: 'Clips (clips 6.24)', 15: 'Prolog (swi 7.2.3)', 16: 'Icon (iconc 9.5.1)', 17: 'Ruby (ruby 2.3.3)', 18: 'Scheme (stalin 0.3)', 19: 'Pike (pike 8.0)', 20: 'D (gdc 6.3)', 21: 'Haskell (ghc 8.0.1)', 22: 'Pascal (fpc 3.0.0)', 23: 'Smalltalk (gst 3.2.5)', 24: 'JAR (JavaSE 6)', 25: 'Nice (nicec 0.9.13)', 26: 'Lua (luac 5.3.3)', 27: 'C# (gmcs 4.6.2)', 28: 'Bash (bash 4.4.5)', 29: 'PHP (php 7.1.0)', 30: 'Nemerle (ncc 1.2.0)', 31: 'Common Lisp (sbcl 1.3.13)', 32: 'Common Lisp (clisp 2.49)', 33: 'Scheme (guile 2.0.13)', 34: 'C99 (gcc 6.3)', 35: 'JavaScript (rhino 1.7.7)', 36: 'Erlang (erl 19)', 38: 'TCL (tcl 8.6)', 39: 'Scala (scala 2.12.1)', 40: 'SQLite (sqlite 3.16.2)', 41: 'C++ (g++ 4.3.2)', 42: 'Assembler 64 (nasm 2.12.01)', 43: 'Objective-C (gcc 6.3)', 44: 'C++14 (gcc 6.3)', 45: 'Assembler 32 (gcc 6.3 )', 46: 'Sed (sed 4)', 47: 'Kotlin (kotlin 1.0.6)', 48: 'Dart (dart 1.21)', 50: 'VB.net (mono 4.6.2)', 62: 'Text (plain text)', 81: 'C (clang 4.0)', 82: 'C++14 (clang 4.0)', 83: 'Objective-C (clang 4.0)', 84: 'D (ldc 1.1.0)', 85: 'Swift (swift 3.0.2)', 91: 'CoffeeScript (coffee 1.12.2)', 92: 'Fantom (fantom 1.0.69)', 93: 'Rust (rust 1.14.0)', 94: 'Pico Lisp (pico 16.12.8)', 95: 'Racket (racket 6.7)', 96: 'Elixir (elixir 1.3.3)', 97: 'Scheme (chicken 4.11.0)', 98: 'Gosu (gosu 1.14.2)', 99: 'Python (PyPy 2.6.0)', 102: 'D (dmd 2.072.2)', 104: 'AWK (gawk 4.1.3)', 105: 'AWK (mawk 1.3.3)', 107: 'Forth (gforth 0.7.3)', 108: 'Prolog (gnu prolog 1.4.5)', 110: 'BC (bc 1.06.95)', 111: 'Clojure (clojure 1.8.0)', 112: 'JavaScript (SMonkey 24.2.0)', 114: 'Go (go 1.7.4)', 115: 'Unlambda (unlambda 0.1.4.2)', 116: 'Python 3 (python  3.5)', 117: 'R (R 3.3.2)', 118: 'Cobol (opencobol 1.1.0)', 121: 'Groovy (groovy 2.4.7)', 122: 'Nim (nim 0.16.0)', 124: 'F# (mono 4.0.0)', 126: 'Python 3 nbc (python 3.4)', 127: 'Octave (octave 4.0.3)'}
if int(lang) not in lcodes:
	print("Invalid language code. Please choose one of below mentioned code\n")
	for key in lcodes:
		print(key,lcodes[key])
	exit(0)
#End language check

#Code to check is the file exists
pfile = pathlib.Path(file)
if not pfile.is_file():
	print('No such file \''+file+'\' found. Please check for the location')
	exit(0)
#End code for file exists

#Common headers for all requests
header = {'Host':'www.spoj.com','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Language':'en-US,en;q=0.5','Accept-Encoding':'gzip, deflate','Referer':'http://www.spoj.com/'}
#End common headers

#Check is the problem exists
url = 'http://www.spoj.com/submit/'+qid+'/'
r=requests.get(url,headers=header,allow_redirects=False)
if(r.status_code==404):
	print('No such problem was found on the server.')
	exit(0)
#End check for problem

#Send login data
login_data = {'next_raw':'','autologin':'1','login_user':username,'password':password}
r=requests.post('http://www.spoj.com/login/',data=login_data,headers=header,allow_redirects=False)
header['Cookie'] = r.headers['Set-Cookie'].split('; ')[0]
#Login data sent and session ID captured

#Check if login successful
if(len(r.headers['Set-Cookie'].split('autologin_hash'))<2):
	print('Login failed')
	exit(0)
else:
	print('Login successful')
#End code to check login

exit(0)
#All checks have passed now. Upload the file
file = {'subm_file': open(file,'rb')}
upload_data = {'lang': lang, 'problemcode': qid, 'file': '', 'submit':'Submit!'}
r = requests.post('http://www.spoj.com/submit/complete/', headers=header,files=file,data=upload_data)
#File upload complete

#Check for the the result
url = 
