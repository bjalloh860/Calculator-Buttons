from datetime import datetime
import random



def warp(tag, text):
    split_tag_style = tag.split(' ')
    close_tag = split_tag_style[0][:1] + "/" + split_tag_style[0][1:]
    if close_tag[-1] != ">":
        close_tag += ">"
    return tag + "\n" + text + "\n" + close_tag




def getStyleElements(text_file_name):
 
    dic = {}

 
    with open(text_file_name, "r") as file:
        current_type = ""  
        img_or_letter = False  

        for line in file.readlines():


            line_array = " ".join(line.replace(
                '\n', '').replace('\t', ' ').split()).split()

            if line_array[0] == 'IMAGES' or line_array[0] == 'LETTERS' or img_or_letter:

              
                if len(current_type) == 0 and line_array[0] == "IMAGES":
                    current_type = line_array[0]
                    dic[current_type] = []
                    img_or_letter = True
                    continue

                elif len(current_type) == 0 and line_array[0] == "LETTERS":
                    current_type = line_array[0]
                    img_or_letter = True
                    continue

                if current_type == "IMAGES":

                    dic[current_type].append(line_array)

                    dic[current_type] = line_array[0]
                    break
                continue

            key, value = line_array[0], " ".join(line_array[1:])
            dic[key] = value

    return dic



def getCurrentDateTime():
    current_datetime = datetime.now()
    day_of_week = current_datetime.strftime('%a')
    month = current_datetime.strftime('%b')
    day = str(current_datetime.day)
    time = str(current_datetime.strftime('%H:%M:%S'))
    year = str(current_datetime.year)
    current_time_array = [day_of_week, month, day, time, year]
    return " ".join(current_time_array)



def getRowAndColumn(imgLetter):
    row = 0
    col = 0
    if type(imgLetter) == list:
        row = len(imgLetter)
        col = len(imgLetter[0])
    elif type(imgLetter) == str:
        row_x_col = imgLetter.split("x")
        row, col = int(row_x_col[0]), int(row_x_col[1])
    return row, col



def getType(dic):
    if "IMAGES" in dic:
        return "IMAGES"
    else:
        return "LETTERS"




def getCells(row, col, dic):
 
    current_type = getType(dic)
   
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    currentLength = len(letters) - 1

    currentColor = ""
    tr = ""  
    for i in range(row):
        num_of_td = ""  
        for j in range(col):

            if i % 2 != 0 and j % 2 != 0:
                currentColor = "second-background-color"

            elif i % 2 != 0 and j % 2 == 0:
                currentColor = "first-background-color"

    
            elif i % 2 == 0 and j % 2 != 0:
                currentColor = "first-background-color"

   
            elif i % 2 == 0 and j % 2 == 0:

                currentColor = "second-background-color"
            if current_type == "IMAGES":
                td = warp(
                    "<td class ='" + currentColor + "';>", "<img src ='images/" + dic["IMAGES"][i][j] + "'>")
                num_of_td += td


            elif current_type == "LETTERS":
                currentIdx = random.randint(0, currentLength)
                currentLetter = letters.pop(currentIdx)
                currentLength -= 1
                td = warp("<td class ='" + currentColor + "';>", currentLetter)
                num_of_td += td

        tr += warp("<tr>", num_of_td)
    return tr




def main(file_name):
    style_dic = getStyleElements(file_name) 
    current_datetime = getCurrentDateTime()
    
    row, column = getRowAndColumn(style_dic[getType(style_dic)])
    widthSize = (1/column) * 100 

    
    with open('pa1_.html', 'w') as html_file:

        html_file.write("<!DOCTYPE html>\n")
        html_file.write("<html>")
        # Style
        style = "body {background-color:" + style_dic["BODY_BACKGROUND"] + ";\n text-align:center;}\n" + \
            "table {margin-left:auto;\n margin-right:auto;\n width:60%;\n height:" + \
            (str(row * 100) + "px;" if getType(style_dic) == "LETTERS" else "32em;") + "\nborder-collapse:collapse;}\n" + \
            "td {border:" + style_dic["TABLE_BORDER_PX"] + \
            "px solid " + style_dic["TABLE_BORDER_COLOR"] + ";\n width:" + str(widthSize) + "%;\n font-size:xx-large;}\n" + \
            "tr {height:100px;}\n" + \
            ".first-background-color {background-color:" + style_dic["CELL_BACKGROUND1"] + ";}\n" +\
            ".second-background-color {background-color:" + \
            style_dic["CELL_BACKGROUND2"] + ";}"

        html_file.write(warp("<style>", style))

    
        html_file.write(warp("<header>", warp(
            "<title>", "Programming Assignment 1")))


        head = warp("<h1>", "--" + style_dic["TITLE"] + "--")

        td = getCells(row, column, style_dic)

       
        table = warp("<table>", td)

       
        time = warp(
            "<p>", "Created automaically for COM214 HW1 on: " + current_datetime)

    
        authors = warp("<p>", "Authors: " + style_dic["AUTHORS"])

   
        html_file.write(warp("<body>", head + table + time + authors))

        html_file.write("</html>")


main("config.txt")
