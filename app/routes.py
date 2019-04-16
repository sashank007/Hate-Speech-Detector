from app import app
from flask import g, render_template, jsonify,request
from app.models import Post
from app import db
import logging
import calendar
import time
toto_logger = logging.getLogger("toto")
toto_logger.setLevel(logging.DEBUG);
console_handler = logging.StreamHandler()
toto_logger.addHandler(console_handler)

@app.route('/')
@app.route('/home/' , methods=['GET','POST'])
def home():
    query_string = request.args.get("post")

    toto_logger.debug("current search request: " + query_string);
    model(query_string);
    addToQueue(query_string,'Sas')
    return 'hello universe'

def addToQueue(username,post):
    currentTime =calendar.timegm(time.strptime('Jul 9, 2009 @ 20:02:58 UTC', '%b %d, %Y @ %H:%M:%S UTC'))
    p=Post(username=username,time=currentTime,post=post)
    db.session.add(p)
    db.session.commit()
    # toto_logger.debug("value added to db : " , post)

def model(val):
    print "running model..."

