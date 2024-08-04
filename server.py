from flask import Flask, jsonify, request
from web_scrapping import sanctions_list

app = Flask(__name__)

@app.route('/', methods=['GET'])
def OFAC_Search():
    try:
        search = request.args.get('search')
        entities =  sanctions_list(search)
        entities_dict = [entity.to_dict() for entity in entities]
        return jsonify(entities_dict)
    except:
        return jsonify(error="Search parameter is required.")

if __name__ == '__main__':
    app.run()