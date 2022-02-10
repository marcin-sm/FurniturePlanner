#bash-> export FLASK_APP=app_web.py
#bash-> export FLASK_ENV=development
#bash-> python -m flask run --host=0.0.0.0   

from flask import Flask
from flask import render_template
from markupsafe import escape
from FurniturePlanner import *
app = Flask(__name__)



@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    Prod = Production ('TODAY')
    Proj = Project ('KUCHNIA')
    Proj.Add(Corpus(post_id,450,510,'down','shelfs',False,False))
    Prod.Add(Proj)
    info = Prod.OperationsProgress (prt = False)
    #return f'Post {post_id}'
    return str(info)

#@app.route('/code/<int:code>')
#def scan(code=None):
#    return render_template('print.html', code=str(code))

@app.route('/')
def home():
    return render_template('print.html')

if __name__ == "__main__":
    app.run()