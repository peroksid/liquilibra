from flask import (Blueprint, jsonify, request)

from datetime import datetime

bp = Blueprint('request_api', __name__, url_prefix='/request')

@bp.route('/', methods=('POST',))
def request_book():
    email = request.form['email']
    title = request.form['title']

    # TODO: check if user exists
    # create if missing
    # check if order exists
    # create if missing
    
    return jsonify(
      email=email,
      title=title,
      id=str(4242),  # TODO: real user ID
      # TODO: strftime to configured format
      # TODO: real datetiem from db
      timestamp=datetime.now().strftime('%m/%d/%Y, %H:%M:%S')  
    )
  