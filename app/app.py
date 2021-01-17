from flask import Flask, render_template, jsonify, request
from nlp_methods import get_similarity_score


app = Flask(__name__)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template("contact.html")



@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template("about.html")




@app.route('/room', methods=['GET', 'POST'])
def room():
    return render_template("room.html")




# Main page
@app.route('/')
def index():
    return render_template("main.html")

if __name__ == '__main__':
    app.run(debug=True)
