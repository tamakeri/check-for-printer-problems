
import time
import send_mail_with_gmail
import yazıcı_kontrol
import duzenle


adres="http://192.168.0.252:8000/rps/"

ne_geldi=yazıcı_kontrol.go(adres)
makine_tum_durum , makine_ad , makine_arıza = ne_geldi
makine_tum_durum=duzenle.make_better(makine_tum_durum)

current_time = time.strftime("%H:%M:%S",time.localtime())

gönder=send_mail_with_gmail.send_message("cagdas20001@gmail.com","sencigot@gmail.com",adres+"\t"+makine_ad+"  "+current_time , makine_tum_durum,user_id='me')

