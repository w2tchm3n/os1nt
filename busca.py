import os
os.system("pip install requests")
import requests


def check_username(username, site_url):
   
    url = site_url.format(username=username)
    
    try:
        
        response = requests.get(url)
        
       
        if response.status_code == 200:
            print(f"[+] {username} encontrado em: {url}")
        elif response.status_code == 404:
            print(f"[-] {username} não encontrado em: {url}")
        else:
            print(f"[?] {username} status desconhecido em {url}: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"[!] Erro ao acessar {url}: {e}")


sites = {
    "GitHub": "https://github.com/{username}",
    "Twitter": "https://twitter.com/{username}",
    "Instagram": "https://instagram.com/{username}",
    "Reddit": "https://reddit.com/user/{username}",
    "Youtube":"https://www.youtube.com/@{username}",
}


print('''\33[32m
 .OOOOOOOOOOOOOOO @@         D i c k  T r a c y        @@ OOOOOOOOOOOOOOOO.
  OOOOOOOOOOOOOOOO @@                                    @@ OOOOOOOOOOOOOOOO
  OOOOOOOOOO'''''' @@                                    @@ ```````OOOOOOOOO
  OOOOO'' aaa@@@@@@@@@@@@@@@@@@@@"""                   """""""""@@aaaa `OOOO
  OOOOO,""""@@@@@@@@@@@@@@""""                                     a@"" OOOA
  OOOOOOOOOoooooo,                                            |OOoooooOOOOOS
  OOOOOOOOOOOOOOOOo,                                          |OOOOOOOOOOOOC
  OOOOOOOOOOOOOOOOOO        ferramenta para buscar nomes     ,|OOOOOOOOOOOOI
  OOOOOOOOOOOOOOOOOO @           em redes sociais            |OOOOOOOOOOOOOI
  OOOOOOOOOOOOOOOOO'@                                        OOOOOOOOOOOOOOb
  OOOOOOOOOOOOOOO'a'                                        |OOOOOOOOOOOOOy
  OOOOOOOOOOOOOO''                                           aa`OOOOOOOOOOOP
  OOOOOOOOOOOOOOb,..                                          `@aa``OOOOOOOh
  OOOOOOOOOOOOOOOOOOo                                           `@@@aa OOOOo
  OOOOOOOOOOOOOOOOOOO|                       .                     @@@ OOOOe
  OOOOOOOOOOOOOOOOOOO@                               aaaaaaa       @@',OOOOn
  OOOOOOOOOOOOOOOOOOO@                        aaa@@@@@@@@""        @@ OOOOOi
  OOOOOOOOOO~~ aaaaaa"a                 aaa@@@@@@@@@@""            @@ OOOOOx
  OOOOOO aaaa@"""""""" ""            @@@@@@@@@@@@""               @@@|`OOOO'
  OOOOOOOo`@@a                  aa@@  @@@@@@@""         a@        @@@@ OOOO9
  OOOOOOO'  `@@a               @@a@@   @@""           a@@   a     |@@@ OOOO3
  `OOOO'       `@    aa@@       aaa"""          @a        a@     a@@@',OOOO 
ascii art feita por {Roy Sussman}   \33[32m''')

username = input("seu_nome_de_usuario: ")
# Verifica o nome de usuário em cada site
for site_name, site_url in sites.items():
    print(f"Verificando {site_name}...")
    check_username(username, site_url)
