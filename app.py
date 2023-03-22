from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    message = request.form['message']
    # Process the message using your GPT model, and return a response
    response = "This is a generic response to your message: " + message
    return {'response': response}

if __name__ == '__main__':
    app.run(debug=True)
