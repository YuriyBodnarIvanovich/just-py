from flask import Blueprint

contact_form_bp = Blueprint('contact_form_bp_in', __name__, template_folder="templates/contact_form")

from . import view