from flask import Flask, request
import random 

app = Flask(__name__)

# animal generator route here
@app.route('/get_animal')
def get_animal():
    return random.choice(['cow', 'horse', 'pig'])

@app.route('/get_noise', method=['POST'])
def get_noise(animal):
    noises = {
        'cow' : 'moo'
        'horse' : 'neigh'
        'pig' : 'oink'
    }
    return noises[request.data.decode('utf-8')]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)