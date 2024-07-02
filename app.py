from flask import Flask, render_template
import json
import random


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    random_quote = get_random_quote()
    return render_template('home.html', random_quote=random_quote)


def get_random_quote():
    quotes = load_quotes()
    random_key = random.choice(list(quotes['all_quotes'].keys()))
    return quotes['all_quotes'][random_key]
    

def load_quotes():
    with open("quotes.json", "r", encoding="utf-8") as json_file:
        quotes = json.load(json_file)
    return quotes
        
if __name__ == "__main__":
    app.run()
    
