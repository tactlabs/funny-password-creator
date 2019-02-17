from flask import Flask, render_template
import os
import sys
from flask import request
from random import randint

import adj_reader as adr
import digit_util as du
import name_reader as nr

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    
    name  = request.form.get('name')    
    if(len(name) == 0):
        name = None 
    name_details = get_password(name)

    result = {
        'apiresult' : 0,    
        'apimessage' : 'OK',    

        'name' : name,
        'password' : name_details        
    }
    
    return render_template('index.html', result=result)


def get_password(username = None):

    adjective = adr.get_random_adj()
    digit = du.random_4()

    if(username is None):
        username = nr.get_random_name()

    password = adjective + str(username) + str(digit)

    #print(adjective)

    return password

if __name__ == "__main__":
    app.run(port=5648)
