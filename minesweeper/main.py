import numpy as np
from flask import Flask, request, render_template, jsonify, url_for
from minesweeper import Minesweeper

app = Flask(__name__)

GRID_SIZE = []
MS = []

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        nrow = int(request.form['nrow'])
        ncol = int(request.form['ncol'])
        per_mine = float(request.form['per_mine'])
        per_mine /= 100

        GRID_SIZE.clear()
        GRID_SIZE.append(nrow)
        GRID_SIZE.append(ncol)

        ms = Minesweeper(nrow, ncol, per_mine)
        ms.createMask()
        ms.createBoard()
        gridVals = ms.displayBoard()

        MS.clear()
        MS.append(ms)

        data = {0: GRID_SIZE, 1: gridVals, 2: False, 3: False}
        return render_template('index.html', data=data)
    elif request.method == 'GET':
        data = {0: None, 1: None, 2: False, 3: False}
        return render_template('index.html', data=data)


@app.route('/process_id', methods=['POST'])
def process_id():
    cell_id = request.json.get('id')
    ms = MS[0]
    x, y = cell_id.split("_")
    x = int(x)
    y = int(y)

    if ms.isOnBomb(x, y):
        ms.mask = np.where(ms.ans_board == -1, 1, ms.mask)
        gv = ms.displayBoard()
        udata = {0: GRID_SIZE, 1: gv, 2: False, 3: True}
        return jsonify({'status': 'success', 'data': udata})

    ms.updateMask(ms.ans_board, ms.mask, x, y)

    if ms.isWon():
        gv = ms.displayBoard()
        udata = {0: GRID_SIZE, 1: gv, 2: True, 3: False}
        return jsonify({'status': 'success', 'data': udata})

    gv = ms.displayBoard()
    udata = {0: GRID_SIZE, 1: gv, 2: False, 3: False}
    return jsonify({'status': 'success', 'data': udata})


if __name__ == '__main__':
    app.run(debug=True)
