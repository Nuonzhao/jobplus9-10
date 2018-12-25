from flask import Blueprint, render_template
from flask import flash, redirect, url_for, request, current_app
from flask_login import login_user, logout_user, login_required
from jobplus.models import User, Company, Job
from jobplus.forms import LoginForm



company = Blueprint('company', __name__)

