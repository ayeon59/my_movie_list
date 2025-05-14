from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient 

app = Flask(__name__)
client = MongoClient('localhost',27017)
db=client.mymovie