from flask import Flask, render_template
app = Flask(__name__)
JOBS = [
  {
    'id': 1,
    'title': 'Data Anatlyst',
    'location': 'chabahil,Nepal',
    'salary': 'Rs.100000'
  },
  {
    'id': 2,
    'title': 'Python Programmer',
    'location': 'Lagakhel,Nepal',
    'salary': 'Rs.120000'
  },
  {
    'id': 3,
    'title': 'Php Programmer',
    'location': 'Jawalakhel,Nepal',
    'salary': 'Rs.130000'
  },
]
@app.route("/")
def hello_world():
  return render_template("home.html",jobs=JOBS,company_name='Jovian')
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS) 
  
if __name__ == "__main__":
  app.run(host='0.0.0.0' , debug = True)
    
    
