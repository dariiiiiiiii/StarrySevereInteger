from flask import Flask , render_template ,jsonify
app = Flask(__name__)
somthing = [
  {"name":"Ali","age":12},
  {"id":2,"name":"Bli","age":13},
  {"id":3,"name":"Cli","age":14},
  {"id":4,"name":"Dli","age":15},
]
@app.route("/")
def hello_world():
  return render_template('home2.html',somthing=somthing)
print(__name__)
@app.route("/somthing")
def list_somthing():
  return jsonify(somthing)
if __name__ =="__main__":
  app.run(host="0.0.0.0" , debug=True)
@app.route("/somthing")
def list_somthing():
  return jsonify(somthing)