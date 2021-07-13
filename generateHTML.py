
import random
from datetime import datetime
import string
import re

# gets current day, month, date, time, and year on runtime

def dayTimeYear():
    now = datetime.now()
    dayOfWeek = now.strftime('%a')
    month = now.strftime('%b')
    day = str(now.day)
    time = str(now.strftime('%H:%M:%S'))
    year = str(now.year)
    time_array = [dayOfWeek, month, time, year]
    return ' '.join(time_array)

# gets user input from config and returns it as string

def getUserInput(starting, ending):
    with open('config.txt', 'r') as f:
        current_type = ''
        for line in f:
            current_type += line

        start = current_type.find(starting) + len(starting)
        if ending == '-1':
            return current_type[start:].strip()

        end = current_type.find(ending)
        substring = current_type[start:end]

        return substring.strip()

# checks whether element is img or letters and wraps tag around it
# e.g "<body>", "Hello world" --> <body>Hello world<body/>

def wrap(tag, element):
    if tag == '':
        return element
    if tag.find(' ') == -1:
        tag_close = '</' + tag[1:]
        return tag+element+tag_close
    elif tag.find(' ') > -1:
        tag_close = '</'+tag[1:tag.find(' ')]+'>'
        return tag+element+tag_close

    return wrap


def generateHTML():

    with open("config.txt", 'r') as config_file:
        imgs =[]
        text = ' '
        table = ' '
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        letters_random = random.shuffle(letters)
        for word in config_file.read().split(): 
            if word == "IMAGES":
                TITLE = getUserInput("TITLE","IMAGES")
                IMAGES = getUserInput("IMAGES","-1")
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
                # print(table)
                    
        

            elif word == "LETTERS":
                TITLE = getUserInput("TITLE", "LETTERS")
                LETTERS = getUserInput("LETTERS", "-1")
                row= getUserInput("LETTERS","x")
                col = getUserInput("x","-1")

                a =""
                count = 0
                for i in range(int(row)):
                    a = wrap("<tr>",a)
                    count -=1
                    for j in range(int(col)):
                        if count%2== 0:
                            a = a+wrap("<th>",letters_random.pop())
                        else:
                            a = a+wrap("<td>",letters_random.pop())
                        count +=1
                # print(a)

                        
                table = wrap("<table>", wrap("<tr>",wrap("",a)))
        return text, table
            


    BODY_BACKGROUND = getUserInput("BODY_BACKGROUND", "CELL_BACKGROUND1")
    CELL_BACKGROUND_1 = getUserInput("CELL_BACKGROUND1","CELL_BACKGROUND2")
    CELL_BACKGROUND_2 = getUserInput("CELL_BACKGROUND2","TABLE_BORDER_COLOR")
    TABLE_BORDER_COLOR = getUserInput("TABLE_BORDER_COLOR", "TABLE_BORDER_PX")
    TABLE_BORDER_PX = getUserInput("TABLE_BORDER_PX","AUTHORS")
    AUTHORS = getUserInput("AUTHORS", "TITLE")
    
    
    
    head = wrap("<head>",wrap("<title>",TITLE))
    body = wrap("<html>",wrap("<h1>","-- "+TITLE+" -- "))
    p = wrap("<p>","Created automatically for COM214 HW1 on: "
    	+dayTimeYear())+wrap("<p>","Authors: "+AUTHORS )      
    styleBackground = wrap("<style>","body{background-color: "+BODY_BACKGROUND+";}") 
    styleTable = wrap("<style>","table,th,td,tr{font-weight:900;font-size: xx-large; border: "+
    	TABLE_BORDER_PX +"px solid " + TABLE_BORDER_COLOR 
    	+"; border-collapse: collapse;width: 600px; height: auto; text-align: center; margin-left: auto;margin-right: auto;}")
    cellBackground1 = wrap("<style>","th{background-color: "+CELL_BACKGROUND_1+";}")
    cellBackground2 = wrap("<style>","td{background-color: "+CELL_BACKGROUND_2+";}")
    styleimage =  wrap("<style>","img{ max-width: 100px; max-height:100px; min-width: 50px; min-height: 50px;}")
    styleph1 = wrap("<style>","p,h1{text-align: center; font-weight: 900;")
    
    
                      
    #writing html file
    HTMLfile = open("pa1.html","w")
    HTMLfile.write(styleBackground+head+body+table+styleTable+p+cellBackground1+cellBackground2+styleimage+ styleph1 )
    HTMLfile.close()

generateHTML()
