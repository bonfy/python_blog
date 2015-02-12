# coding : utf-8
__author__ = 'ChenKai'
#################
#### imports ####
#################

from flask import render_template, Blueprint, request, flash, redirect, url_for
from flask.ext.login import login_required, current_user

from project import db
from project.models import Post, User



################
#### config ####
################

user_blueprint = Blueprint(
    'back', __name__,
    template_folder='templates'
)