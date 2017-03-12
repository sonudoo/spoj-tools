import requests
username = input("Enter your username: ")
l = list(map(str,input("Enter space seperated list of friends: ").split()))

su = set() #Problem solved by user
sf = set() #Problems solved by friends

#Common headers for all requests
header = {'Host':'www.spoj.com','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Language':'en-US,en;q=0.5','Accept-Encoding':'gzip, deflate','Referer':'http://www.spoj.com/'}
#End common headers

#Scrapping the submission of the user
print("\nExtracting your info")
url = "http://www.spoj.com/users/"+username+"/"
try:
	r=str(requests.get(url,headers=header).content)
except:
	print("Connection error..")
	exit(0)
r=r.split('<td align="left" width="14%"><a href="')
if(len(r)==1):
	print("No such username found or you have not solved any of the problem")
else:
	for i in range(1,len(r)):
		s = r[i].split('>')[1].split('</a')[0]
		if(s!=''):
			su.add(s)
#End scrapping

print()

#Scrapping the submission of friends
for friend in l:
	print("Extracting data for friend '"+friend+"'")
	url = "http://www.spoj.com/users/"+friend+"/"
	try:
		r=str(requests.get(url,headers=header).content)
	except:
		print("Connection error..")
		exit(0)
	r=r.split('<td align="left" width="14%"><a href="')
	if(len(r)==1):
		print("No such friend '"+friend+"' found or he/she has not solved any of the problem")
	else:
		for i in range(1,len(r)):
			s = r[i].split('>')[1].split('</a')[0]
			if(s!=''):
				sf.add(s)
#End scrapping

print()

#Scrap for number of accepted solutions for each problem
d={}
for i in (sf-su):
	print("Extracting info for '"+i+"'")
	url = "http://www.spoj.com/ranks/"+i+"/"
	try:
		r=str(requests.get(url,headers=header).content)
	except:
		print("Connection error..")
		exit(0)
	r=r.split('<td class="text-center">')
	j = r[1].split('</td>')[0]
	d[i] = j
#End of scrapping number of users

print("\nYou have not solved "+str(len(d))+"that your friends have solved. The list is as follows\n")

print(d)
