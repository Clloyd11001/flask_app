from flask import Flask, render_template, request
import psutil

app = Flask(__name__)

new_session = True


@app.route('/', methods=['GET', 'POST'])
def index():
    global new_session
    loaded_text = ""

    if request.method == 'POST':
        textbox = request.form['textbox']
        # This creates the file before writing ("i tested by viewing inside docker container")
        with open('/tmp/test.txt', 'w') as file:
            file.write(textbox)
        print('Value saved to a file')

    elif request.method == 'GET':
        try:
            with open('/tmp/test.txt', 'r') as file:
                loaded_text = file.read()
        except FileNotFoundError:
            print("Could not find file to read from")

        if new_session:
            loaded_text = ""
            new_session = False

    return render_template('index.html', loaded_text=loaded_text)


if __name__ == "__main__":
    app.run(debug=True)
