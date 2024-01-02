from flask import Flask, request, send_file
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import script as model
app = Flask(__name__) 
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@cross_origin
@app.route("/")
def home():
    return "<p>Hello, World!</p>"

@app.route('/predict', methods = ['GET', 'POST'])
def cek():
  if request.method == 'POST':
    # return "asd"
    # f = request.files['file']
    # f.save(secure_filename(f.filename))
    # mq7 = request.form['mq7']
    # mq135 = request.form['mq135']
    # json
    data = request.get_json()
    mq7 = data['mq7']
    mq135 = data['mq135']
    # return data
    return model.predict(mq7, mq135)

if __name__ == "__name__":
  app.run(debug=True)