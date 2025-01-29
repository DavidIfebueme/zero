from flask import Flask, Response
import json
from flask_cors import CORS
from datetime import datetime
import pytz

app = Flask(__name__)
CORS(app)

@app.route('/')
def get_info():
    current_datetime = datetime.now(pytz.UTC).strftime("%Y-%m-%dT%H:%M:%SZ")
    response = {
        "email": "davidifebueme@gmail.com", 
        "current_datetime": current_datetime,
        "github_url": "https://github.com/DavidIfebueme/zero"  
    }

    return Response(json.dumps(response, indent=2), content_type='application/json') 

if __name__ == '__main__':
    app.run(debug=True)
