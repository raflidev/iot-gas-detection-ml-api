from flask import Flask, request, send_file
from werkzeug.utils import secure_filename
import script as model
app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Hello, World!</p>"

@app.route('/predict', methods = ['GET', 'POST'])
def cek():
  if request.method == 'POST':
    # f = request.files['file']
    # f.save(secure_filename(f.filename))
    mq7 = request.form['mq7']
    mq135 = request.form['mq135']
    return model.predict(mq7, mq135)

if __name__ == "__name__":
  app.run(debug=True)