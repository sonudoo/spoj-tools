import sys,requests
try:
	qid = sys.argv[1]
except:
	print('You have not mentioned the problem code in the parameter.\n\nUsage: python spoj-viewer.py <problemcode>\nEg: python spoj-viewer.py PRIME1')
	exit(0)

#Common headers for all requests
header = {'Host':'www.spoj.com','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Language':'en-US,en;q=0.5','Accept-Encoding':'gzip, deflate','Referer':'http://www.spoj.com/'}
#End common headers

r=requests.get("http://www.spoj.com/problems/"+qid+"/",headers=header)
problem=""
try:
	problem = str(r.content).split('<div id="problem-body">')[1].split('</div>')[0]
except:
	print('\nNo such problem found on spoj. Try again')

problem = problem.split('\\r\\n')
problem = "\n".join(problem)

x = ''
x = problem
while (True):
    k = 0
    p = x.find("</p>")
    if (p>-1):
        x = x[:p]+x[p+4:]
        k+=1
    p = x.find("</i>")
    if (p>-1):
        x = x[:p]+"'"+x[p+4:]
        k+=1
    p = x.find("</b>")
    if (p>-1):
        x = x[:p]+"'"+x[p+4:]
        k+=1
    p = x.find("</strong>")
    if (p>-1):
        x = x[:p]+"'"+x[p+9:]
        k+=1
    p = x.find("</span>")
    if (p>-1):
        x = x[:p]+x[p+7:]
        k+=1
    p = x.find("</h>")
    if (p>-1):
        x = x[:p]+x[p+4:]
        k+=1
    p = x.find("</h1>")
    if (p>-1):
        x = x[:p]+x[p+5:]
        k+=1
    p = x.find("</h2>")
    if (p>-1):
        x = x[:p]+x[p+5:]
        k+=1
    p = x.find("</h3>")
    if (p>-1):
        x = x[:p]+x[p+5:]
        k+=1
    p = x.find("</h4>")
    if (p>-1):
        x = x[:p]+x[p+5:]
        k+=1
    p = x.find("</h5>")
    if (p>-1):
        x = x[:p]+x[p+5:]
        k+=1
    p = x.find("</h6>")
    if (p>-1):
        x = x[:p]+x[p+5:]
        k+=1
    p = x.find("</pre>")
    if (p>-1):
        x = x[:p]+"\n"+x[p+6:]
        k+=1
    p = x.find("</em>")
    if (p>-1):
        x = x[:p]+"'"+x[p+5:]
        k+=1
     
    p = x.find("</P>")
    if (p>-1):
        x = x[:p]+"\n\n"+x[p+4:]
        k+=1
    p = x.find("</I>")
    if (p>-1):
        x = x[:p]+"'"+x[p+4:]
        k+=1
    p = x.find("</B>")
    if (p>-1):
        x = x[:p]+"'"+x[p+4:]
        k+=1
    p = x.find("</STRONG>")
    if (p>-1):
        x = x[:p]+"'"+x[p+9:]
        k+=1
    p = x.find("</SPAN>")
    if (p>-1):
        x = x[:p]+x[p+7:]
        k+=1
    p = x.find("</H>")
    if (p>-1):
        x = x[:p]+x[p+4:]
        k+=1
    p = x.find("</H1>")
    if (p>-1):
        x = x[:p]+x[p+5:]
        k+=1
    p = x.find("</H2>")
    if (p>-1):
        x = x[:p]+x[p+5:]
        k+=1
    p = x.find("</H3>")
    if (p>-1):
        x = x[:p]+x[p+5:]
        k+=1
    p = x.find("</H4>")
    if (p>-1):
        x = x[:p]+x[p+5:]
        k+=1
    p = x.find("</H5>")
    if (p>-1):
        x = x[:p]+x[p+5:]
        k+=1
    p = x.find("</H6>")
    if (p>-1):
        x = x[:p]+x[p+5:]
        k+=1
    p = x.find("</PRE>")
    if (p>-1):
        x = x[:p]+"\n"+x[p+6:]
        k+=1
    p = x.find("</EM>")
    if (p>-1):
        x = x[:p]+"'"+x[p+5:]
        k+=1
    if (k == 0):
        break
problem = x
x = problem
while (True):
    k = 0
    p = x.find("<p")
    if (p>-1):
        p1 = x.find(">", p+1)
        if (p1 > -1):
            x = x[:p]+"\n"+x[p1+1:]
            k+=1
    p = x.find("<i")
    if (p>-1):
        p1 = x.find(">", p+1)
        if (p1 > -1):
            x = x[:p]+"'"+x[p1+1:]
            k+=1
    p = x.find("<b")
    if (p>-1):
        p1 = x.find(">", p+1)
        if (p1 > -1):
            x = x[:p]+"'"+x[p1+1:]
            k+=1
    p = x.find("<strong")
    if (p>-1):
        p1 = x.find(">", p+1)
        if (p1 > -1):
            x = x[:p]+"'"+x[p1+1:]
            k+=1
    p = x.find("<span")
    if (p>-1):
        p1 = x.find(">", p+1)
        if (p1 > -1):
            x = x[:p]+x[p1+1:]
            k+=1
    p = x.find("<h")
    if (p>-1):
        p1 = x.find(">", p+1)
        if (p1 > -1):
            x = x[:p]+x[p1+1:]
            k+=1
    p = x.find("<h1")
    if (p>-1):
        p1 = x.find(">", p+1)
        if (p1 > -1):
            x = x[:p]+x[p1+1:]
            k+=1
    p = x.find("<h2")
    if (p>-1):
        p1 = x.find(">", p+1)
        if (p1 > -1):
            x = x[:p]+x[p1+1:]
            k+=1
    p = x.find("<h3")
    if (p>-1):
        p1 = x.find(">", p+1)
        if (p1 > -1):
            x = x[:p]+x[p1+1:]
            k+=1
    p = x.find("<h4")
    if (p>-1):
        p1 = x.find(">", p+1)
        if (p1 > -1):
            x = x[:p]+x[p1+1:]
            k+=1
    p = x.find("<h5")
    if (p>-1):
        p1 = x.find(">", p+1)
        if (p1 > -1):
            x = x[:p]+x[p1+1:]
            k+=1
    p = x.find("<h6")
    if (p>-1):
        p1 = x.find(">", p+1)
        if (p1 > -1):
            x = x[:p]+x[p1+1:]
            k+=1
    p = x.find("<pre")
    if (p>-1):
        p1 = x.find(">", p+1)
        if (p1 > -1):
            x = x[:p]+"\n"+x[p1+1:]
            k+=1
    p = x.find("<em")
    if (p>-1):
        p1 = x.find(">", p+1)
        if (p1 > -1):
            x = x[:p]+"'"+x[p1+1:]
            k+=1
    p = x.find("<P")
    if (p>-1):
        p1 = x.find(">", p+1)
        if (p1 > -1):
            x = x[:p]+"\n"+x[p1+1:]
            k+=1
    p = x.find("<I")
    if (p>-1):
        p1 = x.find(">", p+1)
        if (p1 > -1):
            x = x[:p]+"'"+x[p1+1:]
            k+=1
    p = x.find("<B")
    if (p>-1):
        p1 = x.find(">", p+1)
        if (p1 > -1):
            x = x[:p]+"'"+x[p1+1:]
            k+=1
    p = x.find("<STRONG")
    if (p>-1):
        p1 = x.find(">", p+1)
        if (p1 > -1):
            x = x[:p]+"'"+x[p1+1:]
            k+=1
    p = x.find("<SPAN")
    if (p>-1):
        p1 = x.find(">", p+1)
        if (p1 > -1):
            x = x[:p]+x[p1+1:]
            k+=1
    p = x.find("<H")
    if (p>-1):
        p1 = x.find(">", p+1)
        if (p1 > -1):
            x = x[:p]+x[p1+1:]
            k+=1
    p = x.find("<H1")
    if (p>-1):
        p1 = x.find(">", p+1)
        if (p1 > -1):
            x = x[:p]+x[p1+1:]
            k+=1
    p = x.find("<H2")
    if (p>-1):
        p1 = x.find(">", p+1)
        if (p1 > -1):
            x = x[:p]+x[p1+1:]
            k+=1
    p = x.find("<H3")
    if (p>-1):
        p1 = x.find(">", p+1)
        if (p1 > -1):
            x = x[:p]+x[p1+1:]
            k+=1
    p = x.find("<H4")
    if (p>-1):
        p1 = x.find(">", p+1)
        if (p1 > -1):
            x = x[:p]+x[p1+1:]
            k+=1
    p = x.find("<H5")
    if (p>-1):
        p1 = x.find(">", p+1)
        if (p1 > -1):
            x = x[:p]+x[p1+1:]
            k+=1
    p = x.find("<H6")
    if (p>-1):
        p1 = x.find(">", p+1)
        if (p1 > -1):
            x = x[:p]+x[p1+1:]
            k+=1
    p = x.find("<PRE")
    if (p>-1):
        p1 = x.find(">", p+1)
        if (p1 > -1):
            x = x[:p]+"\n"+x[p1+1:]
            k+=1
    p = x.find("<EM")
    if (p>-1):
        p1 = x.find(">", p+1)
        if (p1 > -1):
            x = x[:p]+"'"+x[p1+1:]
            k+=1
    if (k == 0):
        break
problem = x
x = problem
while (True):
    k = 0
    p = x.find("<img")
    if (p > -1):
        p1 = x.find("/img>")
        if (p1>-1):
            x = x[:p]+"\n"+x[p1+5:]
            k+=1
    p = x.find("<IMG")
    if (p > -1):
        p1 = x.find("/IMG>")
        if (p1>-1):
            x = x[:p]+"\n"+x[p1+5:]
            k+=1
    p = x.find("<script")
    if (p > -1):
        p1 = x.find("/script>")
        if (p1>-1):
            x = x[:p]+x[p1+8:]
            k+=1
    p = x.find("<SCRIPT")
    if (p > -1):
        p1 = x.find("/SCRIPT>")
        if (p1>-1):
            x = x[:p]+x[p1+8:]
            k+=1
    if (k == 0):
        break
problem = x
print(problem.replace('\\n\\t',''))
