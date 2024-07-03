from flask import Flask
from flask import request
from flask import Response
import time
import requests
import sys
import random
 
TOKEN = "6517529659:AAH9psxjkXoInPzkIhwQssc-gjiaDhe4kZs"
app = Flask(__name__)
 
def parse_message(message):
    print("message-->",message)
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']
    print("chat_id-->", chat_id)
    print("txt-->", txt)

    return chat_id,txt
 
def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
   

    payload = {
                'chat_id': chat_id,
                'text': text
                }
   
    r = requests.post(url,json=payload)
    return r
 


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()
       
        chat_id,txt = parse_message(msg)
        if txt == "hi" or txt == "Hi":
            
            tel_send_message(chat_id,"Hello!!, how was ur day?")
            time.sleep(3)
        if txt != "hi" and txt != "Hi" and txt != "Yes" and txt != "No" and txt != "1" and txt != "2" and txt != "Bye" and txt != "/start" :
            tel_send_message(chat_id,"mm...ok shall we prepare for placements dear?(Yes/No)")
        if txt == "Yes":
            tel_send_message(chat_id,"which one shall we..aptitude?coding?(1/2)") 
        if txt == "1":
                tel_send_message(chat_id,"https://veltech908.examly.io/mycourses?type=mycourses") 
                tel_send_message(chat_id,"login to above website...have fun with learning") 
        if txt == "2":
                 tel_send_message(chat_id,"https://www.codechef.com/practice-old")
                 tel_send_message(chat_id,"try the problem with difficulty level given below...")
                 tel_send_message(chat_id,random.randrange(200,3000)) 
                    
            
        elif txt == "No":
            tel_send_message(chat_id,"no prob.. but never forget u have to get a good job..hmmm.. ")
            time.sleep(3)
            tel_send_message(chat_id,"ok ..relax in spotify..hope u have a quality time dear")  
            time.sleep(5) 
            tel_send_message(chat_id,"https://open.spotify.com/") 
            time.sleep(2)
            tel_send_message(chat_id,"my choice ...little drummer boy") 

        elif txt == "Bye":
           tel_send_message(chat_id,"love u dear..bye")   
        else:
            
        
         
            return Response('ok', status=200)
    else:
        return "<h1>Welcome!</h1>"
 
if __name__ == '__main__':
   app.run(debug=True)