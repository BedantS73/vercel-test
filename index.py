import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the students data
with open("q-vercel-python.json", "r") as f:
    students_data = json.load(f)

@app.route("/", methods=["GET"])
def get_marks():
    # Get names from query parameters
    names = request.args.getlist("name")
    
    # Find marks for the provided names
    result = {name: next((student["marks"] for student in students_data if student["name"] == name), None) for name in names}
    
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)
