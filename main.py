from flask import Flask, render_template, request, jsonify
import maritalk
from dotenv import load_dotenv
import os
import markdown2

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variable
api_key = os.getenv("API_KEY")
model = os.getenv("MODEL")

model = maritalk.MariTalk(
    key=api_key,
    model=model  # No momento, suportamos os modelos sabia-3, sabia-2-medium e sabia-2-small
)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/question', methods=['POST'])
def pergunta():
    data = request.get_json()  # Recebe os dados JSON da requisição POST
    response = model.generate(data['pergunta'])
    answer = response["answer"]
    html = markdown2.markdown(answer) 
    # return answer
    return jsonify({'resposta': html}), 200

if __name__ == '__main__':
    app.run(debug=True)