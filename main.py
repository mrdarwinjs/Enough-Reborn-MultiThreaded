from time import sleep
from os import system
from sms import SendSms
import threading
from rich.console import Console
from rich.prompt import Prompt
import os
import multiprocessing

#rich
console = Console()

"""
also change turkish variable names to english.
make multi process
and lastly add func tools lr cache?
"""


servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_sms.append(attribute)

while 1:
    system("cls||clear")
    console.print(f"""[bold green]
    ███████╗███╗   ██╗ ██████╗ ██╗   ██╗ ██████╗ ██╗  ██╗
    ██╔════╝████╗  ██║██╔═══██╗██║   ██║██╔════╝ ██║  ██║
    █████╗  ██╔██╗ ██║██║   ██║██║   ██║██║  ███╗███████║
    ██╔══╝  ██║╚██╗██║██║   ██║██║   ██║██║   ██║██╔══██║
    ███████╗██║ ╚████║╚██████╔╝╚██████╔╝╚██████╔╝██║  ██║
    ╚══════╝╚═╝  ╚═══╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝
    [/bold green] [bold purple]
    ███╗   ███╗██╗   ██╗██╗  ████████╗██╗████████╗██╗  ██╗██████╗ ███████╗ █████╗ ██████╗ ███████╗██████╗ 
    ████╗ ████║██║   ██║██║  ╚══██╔══╝██║╚══██╔══╝██║  ██║██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗
    ██╔████╔██║██║   ██║██║     ██║   ██║   ██║   ███████║██████╔╝█████╗  ███████║██║  ██║█████╗  ██║  ██║
    ██║╚██╔╝██║██║   ██║██║     ██║   ██║   ██║   ██╔══██║██╔══██╗██╔══╝  ██╔══██║██║  ██║██╔══╝  ██║  ██║
    ██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║   ██║   ██║  ██║██║  ██║███████╗██║  ██║██████╔╝███████╗██████╔╝
    ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═════╝ 
    [/bold purple]
                                                         
    
    [italic purple]Toplam Sms: {len(servisler_sms)}[/italic purple]           [bold gray]by @tingirifistik[/bold gray]\n
    \n[italic cyan] updated by mrdarwin 🚀[/italic cyan]
    """)
    try:
        #menu = (input(Fore.LIGHTMAGENTA_EX + " 1- SMS Gönder (Normal)\n\n 2- SMS Gönder (Turbo)\n\n 3- Çıkış\n\n" + Fore.LIGHTYELLOW_EX + " Seçim: "))
        menu = Prompt.ask("[italic white] 1 - ✉️  SMS Gönder \n\n 2 - ✉️⚡ SMS Gönder (Turbo)\n\n 3 - ⚙️  Multiprocess - mrdarwin\n\n 4 - 🚪 Çıkış\n\n[/italic white][magenta] Seçim:[/magenta]",default="1")
        if menu == "":
            continue
        menu = int(menu) 
    except ValueError:
        system("cls||clear")
        console.print("[red]Hatalı giriş yaptın. Tekrar deneyiniz.[/red]")
        sleep(3)
        continue
    if menu == 1:
        system("cls||clear")
        console.print("[yellow3]Telefon numarasını başında '+90' olmadan yazınız (Birden çoksa 'enter' tuşuna basınız):[/yellow3]", end="")
        tel_no = input()
        tel_liste = []
        if tel_no == "":
            system("cls||clear")
            console.print("[yellow3]Telefon numaralarının kayıtlı olduğu dosyanın dizinini yazınız: [/yellow3]",end="")
            dizin = input()
            try:
                with open(dizin, "r", encoding="utf-8") as f:
                    for i in f.read().strip().split("\n"):
                        if len(i) == 10:
                            tel_liste.append(i)
                sonsuz = ""
            except FileNotFoundError:
                system("cls||clear")
                console.print("[yellow 3]Hatalı dosya dizini. Tekrar deneyiniz.[/yellow 3]")
                sleep(3)
                continue
        else:
            try:
                int(tel_no)
                if len(tel_no) != 10:
                    raise ValueError
                tel_liste.append(tel_no)
                sonsuz = "(Sonsuz ise 'enter' tuşuna basınız)"  
            except ValueError:
                system("cls||clear")
                console.print("[yellow3] Hatalı telefon numarası. Tekrar deneyiniz.[/yellow3]") 
                sleep(3)
                continue
        system("cls||clear")
        try:
            console.print("[yellow3]Mail adresi (Bilmiyorsanız 'enter' tuşuna basın):[/yellow3]", end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            console.print("[yellow3]Hatalı mail adresi. Tekrar deneyiniz.[/yellow]") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            console.print(f"[yellow3]Kaç adet SMS göndermek istiyorsun  [/yellow3]{sonsuz}:", end="")
            kere = input()
            if kere:
                kere = int(kere)
            else:
                kere = None
        except ValueError:
            system("cls||clear")
            console.print("[yellow3]Hatalı giriş yaptın. Tekrar deneyiniz.[/yellow3]") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            console.print("[yellow3]Kaç saniye aralıkla göndermek istiyorsun: [/yellow]",end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            console.print("[yellow3]Hatalı giriş yaptın. Tekrar deneyiniz.[/yellow3]") 
            sleep(3)
            continue
        system("cls||clear")
        if kere is None: 
            sms = SendSms(tel_no, mail)
            while True:
                for attribute in dir(SendSms):
                    attribute_value = getattr(SendSms, attribute)
                    if callable(attribute_value):
                        if attribute.startswith('__') == False:
                            exec("sms."+attribute+"()")
                            sleep(aralik)
        for i in tel_liste:
            sms = SendSms(i, mail)
            if isinstance(kere, int):
                    while sms.adet < kere:
                        for attribute in dir(SendSms):
                            attribute_value = getattr(SendSms, attribute)
                            if callable(attribute_value):
                                if attribute.startswith('__') == False:
                                    if sms.adet == kere:
                                        break
                                    exec("sms."+attribute+"()")
                                    sleep(aralik)
        print("\n[yellow3]Menüye dönmek için 'enter' tuşuna basınız..[/yellow3]")
        input()
    elif menu == 3:
        console.print("[red]suan yapim asamsinda.[/red]")
        sleep(1.5)
        system("cls||clear")
        
    elif menu == 4:
        system("cls||clear")
        console.print("[red]Çıkış yapılıyor...[/red]")
        break
    elif menu == 2:
        system("cls||clear")
        console.print("[yellow3]Telefon numarasını başında '+90' olmadan yazınız: [/yellow3]",end="")
        tel_no = input()
        try:
            int(tel_no)
            if len(tel_no) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            console.print("[yellow3]Hatalı telefon numarası. Tekrar deneyiniz.[/yellow3]") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            console.print("[yellow3]Mail adresi (Bilmiyorsanız 'enter' tuşuna basın):[/yellow3]", end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            console.print("[yellow3]Hatalı mail adresi. Tekrar deneyiniz.[/yellow3]") 
            sleep(3)
            continue
        system("cls||clear")
        send_sms = SendSms(tel_no, mail)
        dur = threading.Event()
        def Turbo():
            while not dur.is_set():
                thread = []
                for fonk in servisler_sms:
                    t = threading.Thread(target=getattr(send_sms, fonk), daemon=True)
                    thread.append(t)
                    t.start()
                for t in thread:
                    t.join()
        try:
            Turbo()
        except KeyboardInterrupt:
            dur.set()
            system("cls||clear")
            console.print("\nCtrl+C tuş kombinasyonu algılandı. Menüye dönülüyor..")
            sleep(2)