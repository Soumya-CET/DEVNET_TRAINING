from flask import Flask
from flask import request
import requests
import json


app = Flask(__name__)


headers = {'Content-type':'application/json', 'Authorization':'Bearer ....................................................'}

@app.route('/reply', methods=['GET', 'POST'])
def reply():
    if request.method == 'POST':
        id = request.json["data"]["id"]
        #print(request.json)
        mess_rcv, sender_email = get_message(id)
        res = send_message(mess_rcv, sender_email)
        return res

def get_message(id):
    url = "https://webexapis.com/v1/messages/" + id
    payload = {}
    response = requests.request("GET", url,headers=headers, data = payload)
    message = json.loads(response.text)
    #print(message)
    return message["text"], message["personEmail"]

def send_message(message,email):
    url = "https://webexapis.com/v1/messages"
    reply = ""
    if ('devnet' in message.lower().split()):
        reply = "Devnet is Good"
    else:
        reply = "Please Learn DevNet"

    payload = '''{"toPersonEmail":"'''+email+'''","text":"'''+reply+'''"}'''
    #print(payload)
    response = requests.request("POST", url, headers = headers, data = payload)
    #print(response)
    return response.text



if __name__ == '__main__':
    app.run(host="0.0.0.0", port = "5500")