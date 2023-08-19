from flask import Flask, render_template,jsonify,request
from flask_cors import CORS
import requests,openai,os
from dotenv.main import load_dotenv
app = Flask(__name__)
CORS(app)

load_dotenv()
API = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def get_data():
    
    data = request.get_json()
    text=data.get('data')
    openai.api_key = API
    
    user_input = text
    try:
        completion = openai.ChatCompletion.create(
              model="gpt-3.5-turbo",  
              messages=[
                {"role": "user", "content": user_input}
              ]
            )
       
        model_reply = completion.choices[0].message.content
        # print(response,model_reply)
        return jsonify({"response":True,"message":model_reply})
    except Exception as e:
        # print(e)
        error_message = f'Error: {str(e)}'
        return jsonify({"message":error_message,"response":False})

    

if __name__ == '__main__':
    app.run()
