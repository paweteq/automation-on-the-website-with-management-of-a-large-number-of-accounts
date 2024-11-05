import tkinter as tk
import mysql_connector
import paths
import datetime
import os
import manager
import daily_free
import listener
import time
import threading
import requests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def update_info_label():
    num=os.listdir(path_to_daily)
    enabled_profiles = manager.get_enabled_profiles()
    info_daily.config(text=f"daily: {len(num)}/{len(enabled_profiles)}")

def enable(p, label):
    manager.enable_profile(p)
    label.config(fg="green")
def disable(p, label):
    manager.disable_profile(p)
    label.config(fg="red")
def set_as_deposited(p, label):
    manager.set_as_paid(p)
    manager.enable_profile(p)
    label.config(fg="green")
def listen(przycisk):
        kolor=przycisk.cget("bg")
        if kolor=='lightblue':
            przycisk.config(bg='red')
            t1 = threading.Thread(target=listener.main)
            t1.start()
def daily(przycisk):
    #Funkcja blokady 
    przycisk.config(state=tk.DISABLED)
    t1 = threading.Thread(target=daily_free.main)
    t1.start()
    t1.join()

    for i in range(90):
        t=90-i
        time.sleep(1)
        print(f"czekaj {t} sekund")
    #Funkcja do odblokowania
    przycisk.config(state=tk.NORMAL)

with open('token.txt', 'r') as file:
    token=file.read().strip()
    print(token)

while True:
        r_code=requests.get(f"http://{paths.read_ip()}/zadaniedomowe/?token={token}&przycisk=submit").status_code
        if r_code==200:
            print('dziala')
            break
        else:
            print('nie udało się połaczyć')
            time.sleep(60)



root = tk.Tk()
root.title("Tkinter Program")

if token=="":
    label = tk.Label(root, text="Nie podałeś tokenu",font=("Arial", 30))
    label.pack()
else:

    if not mysql_connector.login():
        label = tk.Label(root, text="podałeś błędny token",font=("Arial", 30))
        label.pack()
    else:
        # Ustawienie konfiguracji kolumn
        root.columnconfigure(0, weight=9)
        root.columnconfigure(1, weight=1)
        root.rowconfigure(0, weight=0)  # Nagłówek nie będzie się rozciągał
        root.rowconfigure(1, weight=1)  # Bloki będą zajmowały dostępną przestrzeń w pionie

        # Nagłówek
        header_label = tk.Label(root, text=f"Witam użytkownika {mysql_connector.login()[0]}",font=("Arial", 15))
        header_label.grid(row=0, column=0, columnspan=2)

        # Pierwszy blok - lewy blok
        left_block  = tk.Frame(root, bg="lightblue")
        left_block.grid(row=1, column=0, sticky="nsew")  # Rozciąga się na całą przestrzeń dostępną w kolumnie i wierszu

        # Podział lewego bloku na dwie sekcje
        left_block.columnconfigure(0, weight=1)
        left_block.rowconfigure(0, weight=7)  # 80% wysokości
        left_block.rowconfigure(1, weight=3)  # 20% wysokości

        # Sekcja z przewijanym obszarem
        scrollable_frame = tk.Frame(left_block)
        scrollable_frame.grid(row=0, column=0, sticky="nsew")

        canvas = tk.Canvas(scrollable_frame, bg="lightblue")
        scrollbar = tk.Scrollbar(scrollable_frame, orient="vertical", command=canvas.yview)

        scrollable_content = tk.Frame(canvas)
        scrollable_content.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=scrollable_content, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        all_profiles=manager.get_all_profiles()
        
        sorted_profiles = sorted(all_profiles, key=len)
        enabled_profiles=manager.get_enabled_profiles()
        deposited=manager.get_deposit_profiles()
        row_index = 0

        for profiles in sorted_profiles:
            if profiles in deposited:
                konto = tk.Label(scrollable_content, text=profiles, font=("Arial", 23), fg="orange")
            elif profiles in enabled_profiles:
                konto = tk.Label(scrollable_content, text=profiles, font=("Arial", 23), fg="green")
            else:
                konto = tk.Label(scrollable_content, text=profiles, font=("Arial", 23), fg="red")

            run_profile = tk.Button(
                scrollable_content, text="Run", font=("Arial", 23),
                command=lambda text=profiles: [manager.run_profile(text),update_info_label()],width=16
            )
            enable_button = tk.Button(
                scrollable_content, text="Enable", font=("Arial", 23),
                command=lambda p=profiles, l=konto: [enable(p, l),update_info_label()],width=16
            )
            disable_button = tk.Button(
                scrollable_content, text="Disable", font=("Arial", 23),
                command=lambda p=profiles, l=konto: [disable(p, l),update_info_label()],width=16
            )
            set_ass_deposit = tk.Button(
                scrollable_content, text="Set as paid", font=("Arial", 23),
                command=lambda p=profiles, l=konto: [set_as_deposited(p, l),update_info_label()],width=16
            )

            konto.grid(row=row_index, column=0, sticky="ew",padx=1)  # Ustawienie sticky na "ew" dla etykiety
            run_profile.grid(row=row_index, column=1, sticky="ew",padx=1)  # Ustawienie sticky na "ew" dla przycisku "Run"
            enable_button.grid(row=row_index, column=2, sticky="ew",padx=1)  # Ustawienie sticky na "ew" dla przycisku "Enable"
            disable_button.grid(row=row_index, column=3, sticky="ew",padx=1)  # Ustawienie sticky na "ew" dla przycisku "Disable"
            set_ass_deposit.grid(row=row_index, column=4, sticky="ew",padx=1)  # Ustawienie sticky na "ew" dla przycisku "Set as paid"
            row_index += 1

        # Ustawienie sticky na "nsew" dla przewijanego obszaru
        scrollable_content.grid_rowconfigure(0, weight=1)
        scrollable_content.grid_columnconfigure(0, weight=1)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Sekcja na zwykły blok
        regular_section = tk.Frame(left_block, bg="lightblue")
        regular_section.grid(row=1, column=0, sticky="nsew")

        # Dodawanie przycisków i etykiet do zwykłej sekcji
        left_buttons_frame = tk.Frame(regular_section, bg="lightblue")
        left_buttons_frame.pack(side="left", padx=10)

        right_info_frame = tk.Frame(regular_section, bg="lightblue")
        right_info_frame.pack(side="right", padx=10)

        # Dodawanie przycisków do lewego kontenera
        button=tk.Button(left_buttons_frame, text="Włącz nasłuchiwanie",width=50,height=1,font=("Arial", 24),bg='lightblue')
        button.pack()
        button.config(command=lambda : [listen(button),update_info_label()])


        button2=tk.Button(left_buttons_frame, text="Odbierz Daily Free",width=50,height=1,font=("Arial", 24),bg='lightblue')
        button2.pack()
        button2.config(command=lambda : [daily(button2),update_info_label()])
        

        #wykres 1
        gold_from_daily_free_montly=[]
        today = datetime.date.today()
        for i in range(30):
            date = today - datetime.timedelta(days=i)
            folder_name = date.strftime("%Y-%m-%d") 
            suma=0
            if os.path.exists(f"memory\\dailyfree\\{folder_name}"):
                lista_daily=os.listdir(f"memory\\dailyfree\\{folder_name}")
                for j in lista_daily:
                    with open(f"memory\\dailyfree\\{folder_name}\\{j}","r") as f:
                        wynik=f.read()
                    if '$' not in wynik and "E" not in wynik and not len(wynik)==0:
                        suma+=int(wynik)
                gold_from_daily_free_montly.append({
                            "date":f"{folder_name}",
                            "gold_value":suma})
        #wykres 2
        gold_from_codes_montly=[]
        for i in range(30):
            dzis = datetime.date.today()
            datka = dzis - datetime.timedelta(days=i) 
            folder_name1 = datka.strftime("%Y-%m-%d")
            if os.path.exists(f"memory\\received_codes_by_date\\{folder_name1}"):
                lista2=os.listdir(f"memory\\received_codes_by_date\\{folder_name1}")
                sumka=0
                for codes in lista2:
                    path=f"memory\\received_codes_amounts\\{codes}"
                    if os.path.exists(path):
                        wyniniczek=len(os.listdir(f"memory\\received_codes\\{codes}"))
                        with open(path,"r") as f:
                            wynik=f.read()
                            sumka+=int(wynik)*wyniniczek
                gold_from_codes_montly.append({
                                    "date":f"{folder_name1}",
                                    "gold_value":sumka
                        })
        lista_data_daily=[]
        lista_gold_daily=[]
        for i in gold_from_daily_free_montly:
            lista_data_daily.append(i['date'])
            lista_gold_daily.append(i['gold_value'])
        lista_data_daily.reverse()
        lista_gold_daily.reverse()

        lista_data=[]
        lista_gold=[]
        for i in gold_from_codes_montly:
            lista_data.append(i['date'])
            lista_gold.append(i['gold_value'])

        gold_all_montly=sum(lista_gold_daily)+sum(lista_gold)
        przychod=round(gold_all_montly/1400*4.3,2)
        lista_data.reverse()
        lista_gold.reverse()


        label_info = tk.Label(right_info_frame, text=f"Miesięczne zarobki:{przychod} zł", font=("Arial", 18), bg="lightblue")
        label_info.pack()
        label_info1 = tk.Label(right_info_frame, text=f"Miesięczny gold:{round(gold_all_montly/1000000,2)} mil złota", font=("Arial", 18), bg="lightblue")
        label_info1.pack()

        # Dodawanie etykiet do prawego kontenera
        path_to_daily=f"memory//dailyfree//{datetime.datetime.now().strftime('%Y-%m-%d')}"
        num=os.listdir(path_to_daily)

        info_daily=tk.Label(right_info_frame, text=f"daily:{len(num)}\{len(manager.get_enabled_profiles())}",font=("Arial", 18),bg='lightblue')
        info_daily.pack()

        if not os.path.exists(f"{paths.RECEIVED_CODES_BY_DATE_PATH}//{datetime.datetime.now().strftime('%Y-%m-%d')}"):
            os.makedirs(f"{paths.RECEIVED_CODES_BY_DATE_PATH}//{datetime.datetime.now().strftime('%Y-%m-%d')}")
        codes_today=os.listdir(f"{paths.RECEIVED_CODES_BY_DATE_PATH}//{datetime.datetime.now().strftime('%Y-%m-%d')}")
        for code in codes_today:
            for file in os.listdir(f"{paths.RECEIVED_CODES_PATH}"):
                if file == code:
                    wynik=len(os.listdir(f"{paths.RECEIVED_CODES_PATH}//{file}"))
            label = tk.Label(right_info_frame, text=f"{code}:{wynik}/{len(manager.get_enabled_profiles())}",font=("Arial", 15),bg='lightblue')
            label.pack()

        # Drugi blok - prawy blok
        block2 = tk.Frame(root, bg="lightblue")
        block2.grid(row=1, column=1, sticky="nsew")  # Rozciąga się na całą przestrzeń dostępną w kolumnie i wierszu

        # Podział prawego bloku na dwa bloki pod sobą
        block2.columnconfigure(0, weight=1)
        block2.rowconfigure(0, weight=1)
        block2.rowconfigure(1, weight=1)

        
                    
        fig1,ax1 = plt.subplots()
        
        ax1=plt.plot(lista_data_daily, lista_gold_daily, color='red')
        plt.gca().xaxis.set_major_locator(plt.MultipleLocator(7))
        plt.xlabel('Date')
        plt.ylabel('Gold')
        plt.title('Daily Free')

        #drugi wykres
        fig2,ax2 = plt.subplots() 
        
        ax2=plt.plot(lista_data, lista_gold, color='red')
        plt.gca().xaxis.set_major_locator(plt.MultipleLocator(7))
        plt.xlabel('Date')
        plt.ylabel('Gold')
        plt.title('Codes')

        # Tworzenie pierwszego wykresu


        # Pomniejszenie wykresu do 40% szerokości okna
        canvas1 = FigureCanvasTkAgg(fig1, master=block2)
        canvas1.draw()
        canvas1.get_tk_widget().grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        # Tworzenie drugiego wykresu

        # Pomniejszenie wykresu do 40% szerokości okna
        canvas2 = FigureCanvasTkAgg(fig2, master=block2)
        canvas2.draw()
        canvas2.get_tk_widget().grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        root.mainloop()
