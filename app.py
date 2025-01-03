
from chatbot import chatbot
from flask import Flask, render_template, request, flash, redirect,jsonify
import pymysql

app = Flask(__name__,static_url_path='/static')
app.secret_key = 'SUHASBM1234567890'


# Database Connectivity
def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='Suhasdhanunie26#',
        database='register'
)


@app.route("/")
def home():
    return render_template("src/main.html")
@app.route("/main")
def main():
    return render_template("src/main.html")

@app.route('/index')
def chatss():
    return render_template('src/index.html')



@app.route("/suggestion", methods=['POST'])
def suggestion():
    email = request.form.get('email')
    suggestion_message = request.form.get('message')
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO `suggestion` (email, message) VALUES (%s, %s)", (email, suggestion_message))
    conn.commit()
    cur.close()
    conn.close()

    flash('Your suggestion has been successfully sent!')
    return redirect('/index')



@app.route("/get",methods=['GET'])
def get_bot_response():
    user_message=request.args.get('msg')
    response=chatbot.get_response(user_message)
    return jsonify(str(response))

if __name__ == "__main__":
    app.run()
