import json
import openai
from flask import Flask, request
import requests
openai.api_key =  API

def get_param(cfgfile):
    global API
    global Remcount
    with open(cfgfile,encoding="utf-8") as j:
            cfginfo=json.load(j)
            j.close()
    API = cfginfo.get("API")
    Remcount = cfginfo.get("Remcount")

def available(): #Check the balance
    url = 'https://api.openai.com/dashboard/billing/credit_grants'
    headers = {
        "Authorization": "Bearer " + openai.api_key,
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    content = response.text
    content = json.loads(content)
    return(content)


def chat(text1):
# Use the GPT-3.5 model
    chat_log.append({"role": "user", "content": text1})
    if len(chat_log)==Remcount:
        chat_log.pop(0)
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_log
        )
    # Return the generated text
    return(completion['choices'][0]['message']['content'])

app = Flask(__name__)
@app.route('/api', methods=['GET'])
def api():
    text = request.args.get('text')
    if text:
        if text =="QWEQWEQWEQWE":
            return available()
        else:
            return chat(text)
    else:
        return "Please enter the text!"

if __name__ == '__main__':
    chat_log = []
    get_param('test.cfg')
    app.run(host='0.0.0.0',port=5000,debug=True) #Start the server