from flask import Flask, render_template, jsonify, request
from nlp_methods import get_similarity_score


app = Flask(__name__)

#Pages
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template("contact.html")
 

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template("about.html")


@app.route('/room', methods=['GET', 'POST'])
def room():
    return render_template("room.html")

<<<<<<< HEAD
=======

>>>>>>> 009829f61e8f451673f2be2ac8a2f7b2e68d1b7c
@app.route('/results', methods=['GET', 'POST'])
def results():
    return render_template("results.html")

<<<<<<< HEAD
# POST AND GET REQUESTS
@app.route('/recieveblob', methods=['GET','POST'])
def recieve_blob():
    if request.method == 'POST':
        data = request.get_json()
        print("YO")
        return "Success"
    return 'Call from get' 
  
=======



>>>>>>> 009829f61e8f451673f2be2ac8a2f7b2e68d1b7c
# Main page
@app.route('/')
def index():
    return render_template("main.html")

if __name__ == '__main__':
    app.run()
