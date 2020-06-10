import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except Exception as erro:
    print(f'\033[1:31:40mSite não encontrado ou não ha conexão com INTERNET.  ERRO:{erro.__class__} \033[1:31:40')
else:
    print('\033[1:31:40mSite ONLINE e com acesso.\033[m')
    print(site.read())

