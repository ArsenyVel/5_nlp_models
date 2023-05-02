from flask import Flask, request, render_template,  jsonify

from predict import predict

app = Flask(__name__)


@app.route("/")
def hello():
    return '''
        <!DOCTYPE html>
        <html>
        <style>
              h1 {text-align: center;}
              p {text-align: center;}
              div {text-align: center;}
           </style>
        <body>
        <h1>5 NLP Models</h1>
        <p> if you want to test any of 5 available models click</p>
        <a href="/test_nlp_models"><p style="text-align:center">Test NLP models</p></a>
        </body></html>
        '''


@app.route('/test_nlp_models', methods=["GET", "POST"])
def test_nlp_models():
    # If a form is submitted
    if request.method == "POST":
        # getting input text
        text = str(request.form['text'])
        # getting task name
        print(text)
        task = str(request.form['task'])
        print(task)
        output = predict(text, task)

        return render_template('template_1.html',output=output)

    return render_template('template_1.html')


if __name__ == '__main__':
    app.run(host ="0.0.0.0",port=8002)
