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

        start_ip = ipaddress.IPv4Address(start_ip)

        #最後のIP
        for i in range(1,5):
            end_ip += request.form[str(i) + "octet_end"]
            if i != 4:
                end_ip += "."
        
        end_ip = ipaddress.IPv4Address(end_ip)

        if start_ip <= end_ip:
            ip_range = ipaddress.summarize_address_range(start_ip,end_ip)
        else:
            return redirect(url_for("landing"))


        return render_template("index2.html",parameter=ip_range)


if __name__ == "__main__":
    app.run(port="8888")