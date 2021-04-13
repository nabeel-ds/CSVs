from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
    {
        "Name": u"Sadana",
        "Contact": u"9940048341",
        "Type": u"Family",
        "ID": 1
    },
    {
        "Name": u"Renuka",
        "Contact": u"9940140430",
        "Type": u"Business",
        "ID": 2
    },
]

@app.route("/add-contact" , methods = ["POST"])

def add_contact():
    if not request.json:
         return jsonify({
            "status":"error",
            "message": "Please provide the contact details!"
        },400)

    contact = {
        "Name": request.json["Name"],
        "Contact": request.json.get("Contact" , ""),
        "Type": request.json["Type"],
        "ID": contacts[-1]["ID"] + 1
    }

    contacts.append(contact)

    return jsonify({
        "status": "Success",
        "message": "Contact added succesfully!"
    })

@app.route("/get-contacts")
def get_contacts():
    return jsonify({
        "data": contacts
    })

if (__name__ == "__main__"):
    app.run(debug=True)
