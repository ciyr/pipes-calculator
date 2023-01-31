# flask app
from flask import Flask
from flask import render_template
from flask import request

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='/static')



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST', 'GET'])
def calculate():
    if request.method == 'POST':
        with open('static/list.csv', 'r') as f:
            data = f.readlines()
            f.close()
        pe = request.form.get('pe')
        pn = request.form.get('pn')
        od = request.form.get('od')
        length = request.form.get('length')
        price = "0"
        for i in data:
            i = i.split(',')
            i[-1] = i[-1].strip()
            if i[0] == pe and i[1] == pn and i[2] == od:
                price = str(float(length)*float(i[4])*float(i[5]))
    return render_template('price.html', pe = pe, pn = pn, od = od, length = length, name = price)
    # get the data from the request
    

