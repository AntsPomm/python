
# This script creats an empty file

import datetime

filename =datetime.datetime.now()

def create_file():
    with open(filename.strftime("%y-%m-%d")+".txt","w")as file:
        file.write("")

create_file()
