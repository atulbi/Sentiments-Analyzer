from flask import Flask, redirect, render_template, request, url_for

import os
import sys
from analyzer import Analyzer
from termcolor import colored
import helpers
from analyzer import Analyzer

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():

    # validate screen_name
    screen_name = request.args.get("screen_name", "")
    if not screen_name:
        return redirect(url_for("index"))
    screen_name = screen_name.lstrip("@")
    screen_name = screen_name.lower()
    tweet_list = helpers.get_user_timeline(screen_name,100)
    
    if len(tweet_list) == 0:
        return redirect(url_for("index"))
    # absolute paths to lists
    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")
    
    analyzer = Analyzer(positives, negatives)
    
    #print(len(tweet_list))
    for line in tweet_list:
        analyzer.analyze(line)
    
    a = float(analyzer.pos)
    b = float(analyzer.neg)
    c = float(analyzer.neu)
    
    sumi = a+b+c
    #print(analyzer.pos , analyzer.neg ,analyzer.neu)
    
    positive, negative, neutral = (a/sumi)*100.0, (b/sumi)*100.0, (c/sumi)*100.0
    
    # generate chart
    chart = helpers.chart(positive, negative, neutral)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)
