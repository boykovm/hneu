from flask import Flask, render_template

app = Flask(__name__,
            template_folder='./templates'
            )


@app.route('/qwe')
def qwe():
    return 'we'
    # return render_template('qwe.html')

@app.route('/')
def hello_world():  # put application's code here
    # return 'Hello World!'

if __name__ == '__main__':
    app.run()
