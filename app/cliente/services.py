import requests 
URL = 'http://localhost:8089'
def get_cliente():
    
    r = requests.get(URL+'/cliente')
    clientes = r.json()
    lista = {'clientes':clientes,'req':r}
    #print(r.text)
    #print(r.headers)
    return lista