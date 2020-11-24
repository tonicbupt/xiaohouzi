import os
import contextlib
import tempfile
import shutil
from subprocess import check_call

from flask import Flask
from flask import url_for, redirect
from flask import request, render_template, send_from_directory
from werkzeug.utils import secure_filename

from xiaohouzi import fill

app = Flask(__name__)


@contextlib.contextmanager
def tempdir(prefix='xiaohouzi'):
    workdir = tempfile.mkdtemp(prefix=prefix)
    try:
        yield workdir
    finally:
        shutil.rmtree(workdir)


@app.route('/')
def index():
    return render_template('/index.html')


@app.route('/upload', methods=['POST'])
def upload():
    p = request.files['file']
    if not p.filename:
        return redirect(url_for('index'))

    filename = secure_filename(p.filename)
    name, ext = filename.rsplit('.', 1)
    if ext not in ('jpg', 'jpeg', 'png'):
        return redirect(url_for('index'))

    with tempdir() as d:
        filepath = os.path.join(d, filename)
        p.save(filepath)

        if ext == 'png':
            png_filepath = filepath
            filepath = os.path.join(d, '{}.jpg'.format(name))
            check_call(['sips', '-s', 'format', 'jpeg', png_filepath, '--out', filepath])
        name = fill(filepath, d)
        return send_from_directory(d, name, as_attachment=True, mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
