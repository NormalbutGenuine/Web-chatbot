from flask import Flask, request, jsonify, abort, render_template
from flask_cors import CORS
import give_answer
import sentiment_find
import random
import json

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():    
    # fm = request.form["msg"]       
    # output = give_answer.response(fm)

    return render_template('send.html')

@app.route('/answer', methods=['POST'])
def index2():
    x = request.form['letter']
    tok = sentiment_find.sequencing(x)
    num = sentiment_find.find_sentiment(tok)
    print(x)
    print(num)
    return render_template('test{}.html'.format(str(int(num)+1)))
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)