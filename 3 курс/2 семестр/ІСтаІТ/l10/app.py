from flask import Flask, render_template

app = Flask(
    __name__,
)


skills = [
    {
        'name': 'JavaScript',
        'knowledge_level': 3
    },
    {
        'name': 'CSS',
        'knowledge_level': 3
    },
]

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/ne-home')
def ne_home():
    return render_template('ne-home.html', skills=skills)


if __name__ == '__main__':
    app.run()

