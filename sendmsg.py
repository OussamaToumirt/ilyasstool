import requests



def send_wa(msg):

    if msg == 'check':
        data = {
        "chatId": "212679413409@c.us",
        "contentType": "string",
        "content": "RAH 9alebt Makayna Hta chi update",
        "options": {}
        }
    elif msg == 'update':
        data = {
        "chatId": "212679413409@c.us",
        "contentType": "string",
        "content": "RAH KAYBA UPDATE drh",
        "options": {}
        }
    re = requests.post('https://whatsapp-api-production-993a.up.railway.app/client/sendMessage/ABCD', data=data)
    if re.status_code == 200:
        print(re.text)
    else: 
        print('Server Whatsapp Down')
    
