#!/usr/bin/env python
import ipaddress
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/", methods=["GET"])
def landing():
    #ランディングページの処理
    if request.method == "GET":
        return render_template("index.html")

@app.route("/result",methods=["POST"])
def showing():
    #パラメータなどを受け取って，予測部分に渡す
    if request.method == "POST":
        parameter = {}

        start_ip = ""
        end_ip = ""

        #最初のIP
        for i in range(1,5):

            start_ip += request.form[str(i) + "octet_start"]

            if i != 4:
                start_ip += "."

        try:
            start_ip = ipaddress.IPv4Address(start_ip)
        except:
            return redirect(url_for("relanding"))



        #最後のIP
        for i in range(1,5):
            end_ip += request.form[str(i) + "octet_end"]
                
            if i != 4:
                end_ip += "."
        
        try:
            end_ip = ipaddress.IPv4Address(end_ip)
        except:
            return redirect(url_for("relanding"))


        
        if start_ip <= end_ip:
            ip_range = ipaddress.summarize_address_range(start_ip,end_ip)
        else:
            return redirect(url_for("relanding"))



        return render_template("index2.html",parameter=ip_range)


@app.route("/retry", methods=["GET"])
def relanding():
    #ランディングページの処理
    if request.method == "GET":
        return render_template("index3.html")



if __name__ == "__main__":
    app.run(port="8888",debug=False)