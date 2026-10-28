from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

# Classmates' favorite acronyms (Task 2)
acronyms = [
    ("Daniel", "LOL", "Laughing Out Loud"),
    ("Ethan", "GGWP", "Good Game Well Played"),
    ("Paulo", "AFK", "Away From Keyboard"),
]

# My favorite acronym (Task 3)
my_acronym = "AFK (Away From Keyboard)"


@app.route('/')
def index():
    # Task 2 — generate the HTML directly from the view function
    paragraphs = ''.join(
        f'<p>{name}: {abbr} ({meaning})</p>'
        for name, abbr, meaning in acronyms
    )
    return f'<h1>Favorite Acronyms</h1>{paragraphs}'


@app.route('/rishabh')
def rishabh():
    # Task 3 & 4 — render a Jinja template with Bootstrap styling
    return render_template('template.html', acronym=my_acronym)


if __name__ == '__main__':
    app.run(debug=True)
