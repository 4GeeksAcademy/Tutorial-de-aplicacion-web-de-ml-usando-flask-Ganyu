from flask import render_template, request
from app import app
import math

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None

    if request.method == 'POST':
        expr = request.form.get('expression')
        try:
            allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
            result = eval(expr, {"__builtins__": None}, allowed_names)
        except Exception as e:
            error = str(e)

    return render_template('index.html', result=result, error=error)
