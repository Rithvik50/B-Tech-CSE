from flask import Flask, request,Response, render_template, url_for, redirect
from utils import db
import logging

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
app=Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    notes=db.get_note()
    return render_template("home.html",notes=notes)

@app.route("/add", methods=["GET", "POST"])
def add_note():
    if request.method=="POST":
        form_data=request.form
        db.insert(form_data["title"], form_data["content"])
        return redirect(url_for("home"))
    
    elif request.method=="GET":
        return render_template("add.html")

    else:
        return Response(status=404)

@app.route("/edit/<id>", methods=["GET", "POST"])
def edit_note(id):
    if request.method=="GET":
        
        note=db.get_note(int(id))[0]
        return render_template("edit.html",id=id,note_title=note["title"], note_content=note["content"])
    if request.method=="POST":
        note_title=request.form["title"]
        note_content=request.form["content"]
       
        try:       
            db.update(id, note_title, note_content)
            return redirect(url_for("home"))
        except:
            return Response("oops something went wrong", status=500)
        
@app.route("/delete/<id>", methods=["post"])
def delete_post(id):
    if request.method=="POST":
        try:
            db.delete(int(id))
            return redirect(url_for('home'))
        except:
            return Response("oops something went wrong", status=500)
            
            

if __name__=="__main__":
    db.setup_database()
    app.run(host="0.0.0.0", port=8080, debug=True)