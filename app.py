from flask import Flask, redirect, url_for, request
from flask import render_template
import tensorflow_hub as hub
from flask_sqlalchemy import SQLAlchemy
import random
import tensorflow as tf
loaded_model = tf.saved_model.load("trainedmodel")

# db = SQLAlchemy()

app = Flask(__name__)

# app.config['SECRET_KEY'] = random.randint(32)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
# db.init_app(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    form_data = request.form
    essay = form_data.get('essay')
    new_essay = [essay]

    # predicted_grade = model.predict([new_essay])
    # print(f"The predicted grade for the new essay is: {predicted_grade[0]}")
    outpit = loaded_model(new_essay)

    print(f"The predicted grade for the new essay is: {outpit[0]}")
    print(essay)
    return render_template("index.html", score=8)


if __name__=='__main__':
    app.run(debug=True)