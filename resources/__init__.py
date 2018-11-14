from flask import Flask, jsonify, request
# from quart import Quart
import requests 
from bs4 import BeautifulSoup
import json
from pprint import pprint
from flask_cors import CORS
import re