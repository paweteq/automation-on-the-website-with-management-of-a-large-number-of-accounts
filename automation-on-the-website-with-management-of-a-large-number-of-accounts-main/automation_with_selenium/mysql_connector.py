import manager
import autologin
import requests
import bs4
import paths
def login():
    with open('token.txt', 'r') as file:
        token=file.read().strip()
        if token=="":
            return False
    r=requests.get(f'http://{paths.read_ip()}/url/?token={token}&przycisk=submit')
    text=r.text
    soup=bs4.BeautifulSoup(text,'html.parser')
    span=soup.find_all('span')
    lista=[]
    for i in span:
        wynik=i.text
        if wynik=='':
            return False
        else:
            lista.append(wynik)
    return lista

def check_your_access():
    with open('token.txt', 'r') as file:
        token=file.read().strip()
        if token=="":
            return False
    r=requests.get(f'http://{paths.read_ip()}/url/?token={token}&przycisk=submit')
    text=r.text
    soup=bs4.BeautifulSoup(text,'html.parser')
    span=soup.find_all('span')
    lista=[]
    for i in span:
        wynik=i.text
        if wynik=='':
            return False
        else:
            lista.append(wynik)

    limit_accounts=int(lista[1])
    num_of_accounts=len(manager.get_enabled_profiles())
            
    if limit_accounts<num_of_accounts:
        print("Masz za Dużo kont")
        return False
    else:
        print("Masz dobry dostęp")
        autologin.login_via_selenium(manager.get_first_enabled_profile(),0)
        return True
