from flask import Flask, render_template, request
import random

app = Flask(__name__)

def generate_sequences(quantity):
    sequences = []
    for _ in range(quantity):
        sequence = random.sample(range(1, 61), 6)
        sequences.append(sequence)
    return sequences

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_value = int(request.form['input_value'])
        sequences = generate_sequences(input_value)
        return render_template('index.html', sequences=sequences, input_value=input_value)
    return render_template('index.html', sequences=None, input_value=None)

if __name__ == '__main__':
    app.run(debug=True)
