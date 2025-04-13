from flask import Flask, render_template, request
import os
app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/games")
def games():
    return render_template("games.html")
@app.route("/music", methods=["GET", "POST"])
def music():
    if request.method == "POST":
        file = request.files["musicFile"]
        if file:
            filename = file.filename # get the file name
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename) #save path
            file.save(filepath) #safe file
            return render_template("music.html", music_file=f"uploads/{filename}")
    return render_template("music.html", music_file=None)
@app.route("/videos")
def videos():
    return render_template("videos.html")
if __name__ == "__main__":
    app.run(debug=True)