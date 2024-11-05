import socketio
import receiver
import manager
import autologin
import mysql_connector
import os
import paths
import requests
import time
import datetime
sio = socketio.Client()

running=False

with open('telegram_token.txt', 'r', encoding='utf-8') as file: TOKEN=file.read()

with open('chat_id.txt', 'r', encoding='utf-8') as file: chat_id=file.read()

def main():
    

    if not mysql_connector.check_your_access():
        return False
    
    @sio.event
    def connect():
        print('connected to server')

    

    @sio.on('recive-message')
    def on_code(data):
        global running
        if len(data)==17 and data.isalnum():
            print('kod:',data)
            profiles = manager.get_enabled_profiles()
            if running==True:
                print('Odbiera się kod')
            elif os.path.exists(f'{paths.MEMORY_PATH}\\received_codes\\{data}'):
                
                running=True
                failed_profiles=manager.get_failed_profiles(data)
                receiver.collect(failed_profiles, data)
                login_required = manager.get_login_profiles()
                autologin.autologin_threads(login_required)
                running=False                
            else:
                running=True
                start_data=datetime.datetime.now().strftime('%H:%M:%S')
                if not receiver.collect(profiles, data):
                    end_date=datetime.datetime.now().strftime('%H:%M:%S')
                    print(f'Czas trwania: {start_data} - {end_date}')
                    time.sleep(10)
                    failed_profiles=manager.get_failed_profiles(data)
                    receiver.collect(failed_profiles, data)
                    time.sleep(10)
                    failed_profiles=manager.get_failed_profiles(data)
                    receiver.collect(failed_profiles, data)
                    time.sleep(10)
                    failed_profiles=manager.get_failed_profiles(data)
                    receiver.collect(failed_profiles, data)
                    time.sleep(10)
                    failed_profiles=manager.get_failed_profiles(data)
                    receiver.collect(failed_profiles, data)
                    login_required = manager.get_login_profiles()
                    autologin.autologin_threads(login_required)
                else:
                    failed_profiles=manager.get_failed_profiles(data)
                    receiver.collect(failed_profiles, data)
                    login_required = manager.get_login_profiles()
                    autologin.autologin_threads(login_required)
                    
                try:
                        if TOKEN == "" or chat_id == "":
                            print('nie masz tokenu')
                        else:
                            collected=len(os.listdir(f"{paths.MEMORY_PATH}\\received_codes\\{data}"))
                            enable_account=len(manager.get_enabled_profiles())
                            deposit=len(manager.get_deposit_profiles())
                            with open(f'{paths.MEMORY_PATH}\\received_codes_amounts\\{data}', 'r', encoding='utf-8') as file:
                                gold=int(file.read())
                            text = f"Odebrano kod:{data}\n {collected}\{enable_account} profili 🤑 \n{gold} Golda 💰 \nTotal {collected*gold} Gold\n{round(collected*gold/1400*4.3,2)} PLN 💎\nWplać na {deposit} Profile"
                            requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?parse_mode=html&chat_id={chat_id}&text={text}")
                except Exception as error:
                    print(error)
                    print('nie udało się wysłać')
                running=False    
    sio.connect(f'http://{paths.read_ip()}:3000')
    sio.wait()