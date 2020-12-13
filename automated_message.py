import csv
import datetime as dt
import pywhatkit as wm

name_column_number=0 
phone_column_number=1
message_column_number=2

file_location= 'C:\\Users\\User\\Desktop\\test.csv'  #always use \\ in place of \ while specifing location


with open(file_location) as csvfile:   #opening csv file
    file=csv.reader(csvfile, delimiter=',') 
    next(file,None)    #skip headers
    for row in file:
        in1=row                                   #reading each row name, phone number and message
        name=in1[name_column_number]
        phone=in1[phone_column_number]
        message=in1[message_column_number]
        current_time=dt.datetime.now()
        hour=current_time.hour
        mint=current_time.minute+1
        #print(current_time.hour,current_time.minute) 
        wm.sendwhatmsg('+'+phone,message,hour,mint)           #sending message

        
