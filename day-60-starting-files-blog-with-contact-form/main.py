import smtplib

from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

load_dotenv("./vars/.env")

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
OWN_EMAIL = os.getenv("MY_EMAIL")
OWN_PASSWORD = os.getenv("MY_EMAIL_PASSWORD")

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        number = request.form["phone"]
        message = request.form["message"]

        email_message = f"Subject:Client's Message\n\nName : {name}\neMail : {email}\nTelephone Number : {number}\nMessage : \n{message}\n"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=OWN_EMAIL, password=OWN_PASSWORD)
            connection.sendmail(from_addr=OWN_EMAIL, to_addrs="alvinwen3@gmail.com",
                                msg=email_message)

        return render_template("contact.html", msg_sent = True)
    return render_template("contact.html", msg_sent= False)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
