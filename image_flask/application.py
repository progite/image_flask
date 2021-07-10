import codecs
from flask import Flask, render_template,request
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='GET':
        return render_template("upload.html")
    else:
        # image_file = request.files["fileToUpload"]
        # image_file.save("static/"+secure_filename(image_file.filename))
        # image_file.close()
        # return render_template("display.html", name=image_file.filename)
        # try_img='try_img.html'
        file = codecs.open("try_img.html", "r", "utf-8")
        # print(file.read())
        return render_template("display.html", name=file.)