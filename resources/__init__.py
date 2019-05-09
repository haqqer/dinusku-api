from flask import Flask, jsonify, request
from flask_restful import Resource
import requests 
from bs4 import BeautifulSoup
import json
from pprint import pprint
from flask_cors import CORS
import re
import os