import mysql.connector as mysql
import datetime
import sqlite3


def sql_ekle(evet):
    mycursor = sqlite3.connect('meraba.db')
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
    b="insert into masa (dtarih,cyan,magenta,yellow,black) VALUES (\'"+formatted_time+"\', \'"+evet[0]+"\', \'"+evet[1]+"\', \'"+evet[2]+"\',\'"+evet[3]+"\');"
    mycursor.execute(b)
    mycursor.commit()


def sadece_numara(gelen):
    veriler = []
    for x in range(len(gelen)):
        if (gelen[x] == '%'):
            if (gelen[x-1].isdigit()):
                if (gelen[x-2].isdigit()):
                    if (gelen[x-3].isdigit()):
                        veriler.append(gelen[x-3]+gelen[x-2]+gelen[x-1])
                    else:
                        veriler.append(gelen[x-2]+gelen[x-1])
                else:
                    veriler.append(gelen[x-1])
            else:
                pass
    return veriler
