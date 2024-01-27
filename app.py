from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    loaded_text = ""

    if request.method == 'POST':
        textbox = request.form['textbox']
        with open('tmp/test.txt', 'w') as file:
            file.write(textbox)
        print('Value saved to a file')

    elif request.method == 'GET':
        try:
            with open('tmp/test.txt', 'r') as file:
                loaded_text = file.read()
        except FileNotFoundError:
            print("Could not find file to read from")

    # textbox.mytext.data = ""
    return render_template('index.html', loaded_text=loaded_text)


if __name__ == "__main__":
    app.run(debug=True)
