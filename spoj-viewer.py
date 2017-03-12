import sys

x = ''


# 4 files needed

#put initial code between div tags in test.txt

#test.txt contains initial code between divs
#test1.txt -> code after removing ending tags
#test2.txt -> code after removing starting tags
#test3.txt -> code after removing images


#final output -> test3.txt

fo = open("test.txt", "r")
line = fo.readline()

fi = open("test1.txt", "w")

while (line):
    x = line
    while (True):
        k = 0
        p = x.find("</p>")
        if (p>-1):
            x = x[:p]+"\n"+x[p+4:]
            k+=1
        p = x.find("</i>")
        if (p>-1):
            x = x[:p]+x[p+4:]
            k+=1
        p = x.find("</b>")
        if (p>-1):
            x = x[:p]+"'"+x[p+4:]
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
            x = x[:p]+x[p+6:]
            k+=1
        p = x.find("</em>")
        if (p>-1):
            x = x[:p]+x[p+5:]
            k+=1

       
        p = x.find("</P>")
        if (p>-1):
            x = x[:p]+"\n"+x[p+4:]
            k+=1
        p = x.find("</I>")
        if (p>-1):
            x = x[:p]+x[p+4:]
            k+=1
        p = x.find("</B>")
        if (p>-1):
            x = x[:p]+"'"+x[p+4:]
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
            x = x[:p]+x[p+6:]
            k+=1
        p = x.find("</EM>")
        if (p>-1):
            x = x[:p]+x[p+5:]
            k+=1
        if (k == 0):
            break
    fi.write(x)
    line = fo.readline()

fo.close()
fi.close()


#Remove opening 


fo = open("test1.txt", "r")
line = fo.readline()

fi = open("test2.txt", "w")

while (line):
    x = line
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
                x = x[:p]+x[p1+1:]
                k+=1
        p = x.find("<b")
        if (p>-1):
            p1 = x.find(">", p+1)
            if (p1 > -1):
                x = x[:p]+"'"+x[p1+1:]
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
                x = x[:p]+x[p1+1:]
                k+=1
        p = x.find("<em")
        if (p>-1):
            p1 = x.find(">", p+1)
            if (p1 > -1):
                x = x[:p]+x[p1+1:]
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
                x = x[:p]+x[p1+1:]
                k+=1
        p = x.find("<B")
        if (p>-1):
            p1 = x.find(">", p+1)
            if (p1 > -1):
                x = x[:p]+"'"+x[p1+1:]
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
                x = x[:p]+x[p1+1:]
                k+=1
        p = x.find("<EM")
        if (p>-1):
            p1 = x.find(">", p+1)
            if (p1 > -1):
                x = x[:p]+x[p1+1:]
                k+=1
        if (k == 0):
            break
    fi.write(x)
    line = fo.readline()

fo.close()
fi.close()


#   Remove Image Elements

fo = open("test2.txt", "r")
line = fo.readline()

fi = open("test3.txt", "w")

while (line):
    x = line
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
        if (k == 0):
            break
    fi.write(x)
    line = fo.readline()

fi.close()
fo.close()

