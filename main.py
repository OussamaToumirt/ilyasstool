from bs4 import BeautifulSoup
import requests
import urllib3
import json
from sendmsg import send_wa
from flask import Flask, jsonify

app = Flask(__name__)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
session = requests.Session()

@app.route('/api/data', methods=['GET'])
def get_html():
    response = session.get('https://drh.sante.gov.ma/Pages/MA_D_Admin.aspx', verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find_all('table', {'xmlns:__designer': 'http://schemas.microsoft.com/WebParts/v2/DataView/designer'})
    
    data = []
    for row in table:
        row_data = []
        for i in row.find_all('td'):
            try:
                search_for_div = i.find_all('div')
                for a in search_for_div:
                    print(a.text)
                    if 'Avec Choix​' in a.text:
                        print('HAS A NEW UPDATE -  - - - -- - - - - - ')
                        data.append('avecchoi')
                
                #print(search_for_div)
            except:
                search_for_div = None
            print(i.text)

    
    if 'avecchoi' in data:
        send_wa('update')
        print('HAS UPDATE -                --------')
    else:
        send_wa('check')
        print('NO UPDATE ----------------------------------------')
    
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


