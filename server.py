# -*- encoding: utf-8 -*-

from flask import Flask, render_template,request, jsonify
import connexion

#app = Flask(__name__, template_folder="templates")
app = connexion.App(__name__,specification_dir='./')
app.add_api('swagger.yml')

@app.route('/')
def home():

    headers = request.headers
    auth = headers.get("X-Api-Key")

    if auth:
        return jsonify({"message:": "OK: Authorized"}), 200
    else:
        return jsonify({"message": "ERROR: Unauthorized"}), 401
    
    #return render_template('home.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)