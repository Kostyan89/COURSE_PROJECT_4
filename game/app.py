from flask import Flask, render_template, request, redirect, url_for

from game.equipment import EquipmentData
from game.personages import personage_classes
from game.utils import load_equipment

app = Flask(__name__)
app.url_map.strict_slashes = False

EQUIPMENT: EquipmentData = load_equipment()


def render_choose_personage_template(*args, **kwargs) -> str:
    return render_template(
            'hero_choosing.html',
            classes=personage_classes.values(),
            equipment=EQUIPMENT,
            **kwargs,
        )


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/choose-hero', methods=['GET', 'POST'])
def choose_hero():
    if request.method == 'GET':
        return render_choose_personage_template(header='Выберите героя', next_button='Выбрать врага')
    ...
    return redirect(url_for('choose_enemy'))


@app.route('/choose-enemy', methods=['GET', 'POST'])
def choose_enemy():
    if request.method == 'GET':
        return render_choose_personage_template(header='Выберите врага', next_button='Начать сражение')
    ...
    return '<h2>Not Implemented</h2>'


