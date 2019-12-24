<<<<<<< HEAD
<<<<<<< HEAD
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
posts = {
    0: {
        "post_id": 0,
        "title": "Hello world!",
        "content": "This is some better random text!"
    }
}


@app.route("/")
def home():
    return render_template("home.jinja2", posts=posts)


@app.route("/post/<int:post_id>")
def post(post_id):
    post = posts.get(post_id)
    if not post:
        return render_template("404.html", message=f"A post with id {post_id} does not exist")
    else:
        return render_template("post.html", post=post)


@app.route("/post/form")
def form():
    return render_template("create.html")


@app.route("/post/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        post_id = len(posts)
        posts[post_id] = {"post_id": post_id,
                          "title": title, "content": content}
        return redirect(url_for("post", post_id=post_id))
    return render_template("create.html")


if __name__ == "__main__":
    app.run(debug=True)
=======
from flask import Flask

>>>>>>> 423c596... Adding autopep8 and app.py
=======
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
posts = {
    0: {
        "post_id": 0,
        "title": "Hello world!",
        "content": "This is some better random text!"
    }
}


@app.route("/")
def home():
    return render_template("home.jinja2", posts=posts)


@app.route("/post/<int:post_id>")
def post(post_id):
    post = posts.get(post_id)
    if not post:
        return render_template("404.html", message=f"A post with id {post_id} does not exist")
    else:
        return render_template("post.html", post=post)


@app.route("/post/form")
def form():
    return render_template("create.html")


@app.route("/post/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        post_id = len(posts)
        posts[post_id] = {"post_id": post_id,
                          "title": title, "content": content}
        return redirect(url_for("post", post_id=post_id))
    return render_template("create.html")


if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> 246d1b2... Starting the web app with Flask and jinja2 templates
