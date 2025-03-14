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


print('''                                                                                 	
        XXXXX                                                                   
       XXXXXXX                                                                  
     XXXXXXXXXXX                                                                
  XXXX  X   X  XXXX                                                             
     X XXX XXX X                                                                
     X  X   X  X                                                                
      X       X     
        XXXXX
''')
username = input("seu_nome_de_usuario: ")

# Verifica o nome de usuário em cada site
for site_name, site_url in sites.items():
    print(f"Verificando {site_name}...")
    check_username(username, site_url)
