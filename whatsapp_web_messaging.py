import webbrowser
import csv
import time
import pyautogui as gui

interval = 4 #time to open the webpage
interval_2= 20 #time to open whatsapp web


position1 =700,325 #position for 1st click
position2 =694,392 #position for 2nd click


name_column_number=0 
phone_column_number=1
message_column_number=2

file_location= 'C:\\Users\\User\\Desktop\\test.csv'  #always use \\ in place of \ while specifing location


with open(file_location) as csvfile:   #opening csv file
    file=csv.reader(csvfile, delimiter=',') 
    next(file,None)    #skip headers
    for row in file:
        in1=row                                   #reading each row
        name=in1[name_column_number]
        phone=int(in1[phone_column_number])
        message=in1[message_column_number]
        
        url ='http://wa.me/{}?text={}'.format(phone,message)

        #webclicking
        webbrowser.open(url)  
        time.sleep(interval)
        gui.click(position1)
        time.sleep(interval)
        gui.click(position2)
        time.sleep(interval_2)
        gui.press('enter')
        time.sleep(2)
