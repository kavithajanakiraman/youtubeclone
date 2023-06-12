from flask import Flask,render_template,url_for,redirect,request
import sqlite3 as sql
from pytube import extract

app=Flask(__name__)

@app.route('/')
def home():
    conn=sql.connect("videos.db")
    conn.row_factory=sql.Row
    cur=conn.cursor()
    cur.execute("SELECT * FROM video")
    dic=cur.fetchall()
    return render_template("home.html",data=dic)

@app.route('/video/<var>')
def video(var):
    return render_template("videoplayer.html",VAR=var)

@app.route('/form', methods=["POST","GET"])
def form():
    if request.method=="POST":
        videourl=request.form.get("video")
        videoid=extract.video_id(videourl)
        thumb=request.form.get("thumb")
        name=request.form.get("name")
        des=request.form.get("des")
        conn=sql.connect("videos.db")
        cur=conn.cursor()
        cur.execute('insert into video(videourl,thumbnail,title,description)values(?,?,?,?)',(videoid,thumb,name,des))
        conn.commit()
        return redirect(url_for("home"))
    return render_template("upload.html")



if __name__=="__main__":
    app.run(debug=True)



    


