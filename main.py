import yazıcı_kontrol
import duzenle
import to_the_sql
import datetime

import threading




import send_mail_with_yaani
current_time = datetime.datetime.now()
formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')


#waiting for all    links to acces


# List of URLs
urls = ["http://192.168.0.252:8000/",
"http://192.168.0.252:8000/","http://192.168.0.252:8000/","http://192.168.0.252:8000/","http://192.168.0.252:8000/","http://192.168.0.252:8000/","http://192.168.0.252:8000/","http://192.168.0.252:8000/","http://192.168.0.252:8000/","http://192.168.0.252:8000/",
]

send_mail_with_yaani.ilk_çalışma()

içeri=""
def add_hepsi(gelen):
    global içeri
    içeri=içeri+"         "+gelen
def get_hepsi():
    global içeri
    return içeri



def checking(adres):
    ne_geldi = yazıcı_kontrol.go(adres)
    """problem with returns"""
    makine_tum_durum, makine_ad ,bos= ne_geldi
    makine_tum_durum = duzenle.make_better(makine_tum_durum)
    
    return makine_tum_durum ,makine_ad,adres



def ana(x):
    makine_tum_durum=[]

    print(urls[x])
    makine_tum_durum = checking(urls[x])

    to_the_sql.sql_ekle(to_the_sql.sadece_numara(makine_tum_durum[0]))
    
    icerik=makine_tum_durum[2]+" "+makine_tum_durum[1]+" "+str(formatted_time) +"  \n"+ makine_tum_durum[0]
    add_hepsi(icerik)


x=0
# Create a list to hold thread objects
threads = []
import time
# Start a thread for each URL
for url in urls:
    thread = threading.Thread(target=ana,args=(x,))

    
    thread.start()
    time.sleep(10)

    x=x+1
    threads.append(thread)


# Wait for all threads to finish
for thread in threads:
    thread.join()



send_mail_with_yaani.gonder("sender mail GOES HERE",get_hepsi())