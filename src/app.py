from flask import Flask, jsonify, request
from .datastructures import FamilyStructure  

app = Flask(__name__)
app.url_map.strict_slashes = False

# Instancia de la familia Jackson
jackson_family = FamilyStructure("Jackson")

@app.route('/members', methods=['GET'])
def get_all_members():
    try:
        members = jackson_family.get_all_members()
        return jsonify(members), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    try:
        member = jackson_family.get_member(member_id)
        if member:
            return jsonify(member), 200
        else:
            return jsonify({"error": "Miembro no encontrado"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/members', methods=['POST'])
def add_member():
    try:
        member_data = request.get_json()
        if "first_name" not in member_data or "age" not in member_data or "lucky_numbers" not in member_data:
            return jsonify({"error": "Faltan campos requeridos"}), 400

        jackson_family.add_member(member_data)
        return jsonify(member_data), 200 
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    try:
        member = jackson_family.get_member(member_id)
        if not member:
            return jsonify({"error": "Miembro no encontrado"}), 404

        jackson_family.delete_member(member_id)
        return jsonify({"done": True}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
