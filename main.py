#import send_mail_with_gmail
import yazıcı_kontrol
import duzenle
import to_the_sql
import datetime
import send_mail_with_yaani
def see_ya():
    send_mail_with_yaani.ilk_çalışma()
    adres = "http://192.168.0.252:8000/rps/"
    ne_geldi = yazıcı_kontrol.go(adres)
    makine_tum_durum, makine_ad, makine_arıza = ne_geldi
    makine_tum_durum = duzenle.make_better(makine_tum_durum)
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')
    to_the_sql.sql_ekle(to_the_sql.sadece_numara(makine_tum_durum))

    icerik=adres+" "+makine_ad+" "+str(formatted_time) + makine_tum_durum

    #gönder = send_mail_with_gmail.send_message("cagdas20001@gmail.com", "sencigot@gmail.com", adres+"\t"+makine_ad+"  "+str(formatted_time), makine_tum_durum, user_id='me')
    send_mail_with_yaani.gonder("cagdas20001@gmail.com",icerik)
see_ya()
