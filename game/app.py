from flask import Flask, render_template, request

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/choose-hero', methods=['GET', 'POST'])
def choose_hero():
    if request.method == 'GET':
        render_template('hero_choosing.html', header='Выберите героя')
    if request.method == 'POST':


