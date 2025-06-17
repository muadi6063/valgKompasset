from flask import Flask,jsonify
import pandas as pd 

app = Flask(__name__)

df = pd.read_csv("data.csv")
