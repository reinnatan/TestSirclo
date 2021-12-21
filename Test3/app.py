from datetime import datetime

from flask import Flask, render_template, request
from sqlalchemy import desc, delete
from werkzeug.utils import redirect
from model.berat_badan import *


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///beratbadan.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()


@app.route('/')
def index():
    list_berat_badan = BeratBadanModel.query.order_by(desc(BeratBadanModel.tanggal)).all()
    avg_max = 0
    avg_min = 0
    avg_diff = 0
    for berat_badan in list_berat_badan:
        avg_max += berat_badan.max
        avg_min += berat_badan.min
        avg_diff += berat_badan.perbedaan

    try:
        avg_max = avg_max/len(list_berat_badan)
        avg_min = avg_min/len(list_berat_badan)
        avg_diff = avg_diff/len(list_berat_badan)
    except Exception:
        pass

    all_div = {
        "avg_max": avg_max,
        "avg_min": avg_min,
        "avg_diff":avg_diff,
    }

    return render_template('list-bb.html', list_berat_badan=list_berat_badan, avg_diff= all_div)


@app.route('/view-create')
def view_create_bb():
    return render_template('create-bb.html')


@app.route('/update/<int:id>', methods=['GET'])
def update_view_bb(id):
    berat_badan_selected = BeratBadanModel.query.filter_by(id=id).first()
    if berat_badan_selected:
        return render_template('update-bb.html', berat_badan_selected=berat_badan_selected)
    return f"Berat Badan dengan id ={id} tidak exist"


@app.route('/create-bb', methods=['POST'])
def create_berat_badan():
    tanggal = request.form['tanggal']
    date_db = datetime.strptime(tanggal, "%Y-%m-%d")
    try:
        max = int(request.form['max'])
        min = int(request.form['min'])
    except Exception:
        return render_template('create-bb.html', error="value min max must be integer")

    if min > max:
        return render_template('create-bb.html', error = "min must less than max")

    berat_badan_selected = BeratBadanModel.query.filter_by(tanggal=tanggal).first()
    if berat_badan_selected:
        return render_template('create-bb.html', error="Data dengan tanggal" + tanggal + " sudah ada")

    perbedaan = max - min
    berat_badan = BeratBadanModel(tanggal=date_db, max=max, min=min, perbedaan=perbedaan)
    db.session.add(berat_badan)
    db.session.commit()
    return redirect('/')


@app.route('/action-update-bb/<int:id>',  methods=['POST'])
def action_update_berat_badan(id):
    tanggal = request.form['tanggal']
    date_db = datetime.strptime(tanggal, "%Y-%m-%d")
    try:
        max = int(request.form['max'])
        min = int(request.form['min'])
    except Exception:
        return render_template('create-bb.html', error="min max must integer")

    if min > max:
        return render_template('create-bb.html', error = "min must less than max")

    list_delete = []
    list_bb = BeratBadanModel.query.filter_by(tanggal=tanggal).all()
    for sel_bb in list_bb:
        list_delete.append(sel_bb.id)

    if len(list_delete)>0:
        sql1 = delete(BeratBadanModel).where(BeratBadanModel.id.in_(list_delete))
        db.session.execute(sql1)
        db.session.commit()

        berat_badan_selected = BeratBadanModel.query.filter_by(id=id).first()
        if berat_badan_selected:
            db.session.delete(berat_badan_selected)
            db.session.commit()

        perbedaan = max - min
        berat_badan = BeratBadanModel(tanggal=date_db, max=max, min=min, perbedaan=perbedaan)
        db.session.add(berat_badan)
        db.session.commit()

    return redirect('/')

@app.route('/delete/<int:id>')
def delete_berat_badan(id):
    berat_badan_selected = BeratBadanModel.query.filter_by(id=id).first()
    if berat_badan_selected is None:
        return f"Berat Badan dengan id ={id} tidak exist"

    db.session.delete(berat_badan_selected)
    db.session.commit()
    return redirect('/')


@app.route('/detail/<tanggal>')
def detail_berat_badan(tanggal):
    berat_badan_selected = BeratBadanModel.query.filter_by(tanggal=tanggal).first()
    if berat_badan_selected is None:
        return f"Berat Badan dengan id ={id} tidak exist"
    return render_template('detail.html', berat_badan_selected=berat_badan_selected)



if __name__ == '__main__':
    app.run(debug=True)
