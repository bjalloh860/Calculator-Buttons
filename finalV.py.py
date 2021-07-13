import re
import time
import string
import random

#this will insert opening and closing HTML tags around the given text
#passed as a parameter
def wrap(tag,text):
    if tag == "":
        return text
    
    if tag.find(" ") == -1:
        closetag = "</"+tag[1:]
        return tag+text+closetag
    
    elif -1<tag.find(" "):
        closetag = "</"+tag[1:tag.find(" ")]+">"
        return tag+text+closetag   
    
    return wrapedText


# reads the config.txt from the file and finds the user input then returns it to a string  
def getInput(st,ed):
    f = open("config.txt","r")
    word =""
    for line in f:
        word= word+line

    start = word.find(st)+len(st)

    if ed == "-1":
        return word[start:].strip()

    end = word.find(ed)
    substring = word[start:end]
    return substring.strip()




def generateHTML():
    f = open("config_1.txt","r")
    imgs =[]
    text = ""
    table = ""
    alphabet_string = string.ascii_lowercase +string.ascii_uppercase
    alphabet_list = list(alphabet_string)
    random.shuffle(alphabet_list)
    for word in f.read().split(): 
        if word == "IMAGES":
            TITLE = getInput("TITLE","IMAGES")
            IMAGES = getInput("IMAGES","-1")
            row = len(IMAGES.splitlines())
            print(row)
            col = len(IMAGES.splitlines()[0].split())
            print(col)
            for img in IMAGES.split():
                imgs.append(img)
            rimage=imgs[::-1]    
            print(rimage)
            

            k =""
            count = 0
            
            if (row%2 == 1 and col%2 ==0) or (row%2 == 0 and col%2 ==1) or (row%2 == 1 and col%2 ==1):
                for i in range(int(row)):
                    k = wrap("<tr>",k)
                    count +=1
                    for j in range(int(col)):
                        if count%2== 0:
                            k = k+wrap("<td>","<img src=\"" + rimage.pop()+ "\">")
                        else:
                            k = k+wrap("<th>","<img src=\"" +rimage.pop()+ "\">")
                        

            else:    
                for i in range(int(row)):
                    k = wrap("<tr>",k)
                    count -=1
                    
                    for j in range(int(col)):
                        if count%2== 0:
                            k = k+wrap("<td>","<img src=\"" + rimage.pop()+ "\">")
                        else:
                            k = k+wrap("<th>","<img src=\"" +rimage.pop()+ "\">")
                        count +=1
                    
            print(k)

            table = wrap("<table>", wrap("<tr>",wrap("",k)))
            print(table)
                
    

        elif word == "LETTERS":
            TITLE = getInput("TITLE", "LETTERS")
            LETTERS = getInput("LETTERS", "-1")
            row= getInput("LETTERS","x")
            col = getInput("x","-1")

            a =""
            count = 0
            for i in range(int(row)):
                a = wrap("<tr>",a)
                count -=1
                for j in range(int(col)):
                    if count%2== 0:
                        a = a+wrap("<th>",alphabet_list.pop())
                    else:
                        a = a+wrap("<td>",alphabet_list.pop())
                    count +=1
            print(a)

                    
            table = wrap("<table>", wrap("<tr>",wrap("",a)))
            
            
    BODY_BACKGROUND = getInput("BODY_BACKGROUND", "CELL_BACKGROUND1")
    CELL_BACKGROUND1 = getInput("CELL_BACKGROUND1","CELL_BACKGROUND2")
    CELL_BACKGROUND2 = getInput("CELL_BACKGROUND2","TABLE_BORDER_COLOR")
    TABLE_BORDER_COLOR = getInput("TABLE_BORDER_COLOR", "TABLE_BORDER_PX")
    TABLE_BORDER_PX = getInput("TABLE_BORDER_PX","AUTHORS")
    AUTHORS= getInput("AUTHORS", "TITLE")
    

    
    
    head = wrap("<head>",wrap("<title>",TITLE))
    body = wrap("<html>",wrap("<h1>","-- "+TITLE+" -- "))
    p = wrap("<p>","Created automatically for COM214 HW1 on: "+time.asctime(time.localtime(time.time())))+wrap("<p>","Authors: "+AUTHORS )      
    styleBackground = wrap("<style>","body{background-color: "+BODY_BACKGROUND+";}") 
    styleTable = wrap("<style>","table,th,td,tr{font-weight:900;font-size: xx-large; border: "+TABLE_BORDER_PX +"px solid " + TABLE_BORDER_COLOR +"; border-collapse: collapse;width: 600px; height: auto; text-align: center; margin-left: auto;margin-right: auto;}")
    cellBackground1 = wrap("<style>","th{background-color: "+CELL_BACKGROUND1+";}")
    cellBackground2 = wrap("<style>","td{background-color: "+CELL_BACKGROUND2+";}")
    styleimage =  wrap("<style>","img{ max-width: 50px; max-height:50px; min-width: 50px; min-height: 50px;}")
    styleph1 = wrap("<style>","p,h1{text-align: center; font-weight: 900;")
    
    
                        
    #writing html file
    HTMLfile = open("pa1.html","w")
    HTMLfile.write(styleBackground+head+body+table+styleTable+p+cellBackground1+cellBackground2+styleimage+ styleph1 )
    HTMLfile.close()


    

generateHTML()
