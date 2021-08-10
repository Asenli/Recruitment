from flask import Blueprint
import os

dir_name = os.path.split(os.path.split(os.path.abspath(__file__))[0][1])
api = Blueprint(dir_name, __name__)

from . import user, role