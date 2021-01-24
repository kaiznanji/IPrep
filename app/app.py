from flask import Flask, render_template, jsonify, request
from nlp_methods import get_similarity_score


app = Flask(__name__)

#Pages
@app.route('/contact')
def contact():
    return render_template("contact.html")
 

@app.route('/about') 
def about():
    return render_template("about.html")

 
@app.route('/room')
def room():
    return render_template("room.html")

@app.route('/results')
def results():
    return render_template("results.html")

# POST AND GET REQUESTS 
@app.route('/recievetext', methods=['GET','POST'])
def recieve_blob():
    if request.method == 'POST':
        print(request.get_json())
    return 'Call from get' 
  
# Main page   
@app.route('/')
def index():
    return render_template("main.html")

if __name__ == '__main__':
    app.run(debug=True)
