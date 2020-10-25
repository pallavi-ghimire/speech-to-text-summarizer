import os
from flask import Flask, render_template, request, redirect, url_for
from google_speech import google_speech
from final import final
app = Flask(__name__)

app.config["IMAGE_UPLOADS"] = "resources/"


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        file = request.files['featured']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], file))

    return render_template("index.html")


@app.route('/upload', methods=['GET', 'POST'])
def upload(gist=None, content=None):
    global summary
    cont = ""
    all = ""
    if request.method == "POST":
        perc = request.form['percentage']
        if request.files:
            image = request.files["file"]
            print(image)
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
            name_of_file = image.filename
            print(type(name_of_file))

            summary = google_speech(name_of_file, perc)
            # print(summary[0])
            return redirect(url_for('upload'))
    separator = ', '
    for s in summary.summarized:
        all = all + " " + s
    for u in summary.unsummarized:
        cont = cont + u
    return render_template('result.html', gist=all, content=cont)


if __name__ == "__main__":
    app.run()


