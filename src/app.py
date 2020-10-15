"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


@app.route('/members', methods=['GET'])
def handle_hello():
    # this is how you can use the Family datastructure by calling its methods
    try:
        members = jackson_family.get_all_members()
        return jsonify(members), 200
    except:
        return jsonify('internal server error'), 500


@app.route('/member/<int:id>', methods=['GET'])
def get_one_member(id):
    try:
        id_member = int(id)
        member = jackson_family.get_member(id_member)        
        if(member == 404):
            return jsonify('Member not found'), 404
        else:
            new_obj = {
                "name":member["first_name"],
                "id":member["id"],
                "age":member["age"],
                "lucky_number":member["lucky_number"]
            }
            return jsonify(new_obj), 200

    except ValueError as err:
        print('VALUE ERROr', err)
        return jsonify('internal server error'), 500

    except:
        print('one error')
        return jsonify('internal server error'), 500
    

@app.route('/member', methods=["POST"])
def cretate_member():
    try:
        age = request.json["age"]
        firstname = request.json["first_name"]
        lucky_numbers = request.json["lucky_numbers"]
        member = {
            "age":age,
            "firstname": firstname,
            "lucky_numbers":lucky_numbers
        }
        create = jackson_family.add_member(member)
        if(create == 200):
            return jsonify('todo bien'), 200

    except ValueError as err:
        print('VALUES ERROR', err)
        return jsonify('Internal server error'), 500

    except Exception as err:
        print('IOS ERROR', err)
        return jsonify('Bad request'), 400

    except:
        print('Except')
        return jsonify('Internal server error'), 500


@app.route('/member/<int:id>', methods=["DELETE"])
def delete_member(id):
    try:
        id_member = int(id)
        member = jackson_family.delete_member(id_member)        
        if(member == 404):
            return jsonify('Member not found'), 404
        else:
            return jsonify(member), 200

    except ValueError as err:
        print('VALUE ERROr', err)
        return jsonify('internal server error'), 500

    except:
        print('one error')
        return jsonify('internal server error'), 500

    

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
