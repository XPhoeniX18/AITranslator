import os
from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = 'key'

def translate_text(text, language):
   
    prompt = f"Translate the following text to {language}: {text}"
    
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-16k",
        prompt=prompt,
        max_tokens=100  
    )
    
    return response.choices[0].text.strip()

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ''
    if request.method == 'POST':
        text = request.form['text']
        language = request.form['language']
        translated_text = translate_text(text, language)
    return render_template('index.html', translated_text=translated_text)

if __name__ == "__main__":
    app.run(debug=True)