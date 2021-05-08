import json
from operator import itemgetter
from flask import jsonify

data = [
    {
        "id": 1,
        "name": "Evans Forson",
        "email": "ataforson@gmail.com"
    },
    {
        "id": 2,
        "name": "Georg Udosen",
        "email": "datameshprojects@gmail.com"
    },
    {
        "id": 3,
        "name": "Fon Nkwenti",
        "email": "fonnkwenti85@gmail.com"
    },
    {
        "id": 4,
        "name": "Franklin Tallah",
                "email": "ftallah@gmail.com"
    },
    {
        "id": 5,
        "name": "Gabriel Sallah",
        "email": "gabriel.sallah@gmail.com"
    },
    {
        "id": 6,
        "name": "Seyram Komla Sapaty",
        "email": "komlasapaty@gmail.com"
    },
    {
        "id": 7,
        "name": "Nbanjika",
        "email": "nbanjika@gmail.com"
    }
]


def get_all(self):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    return jsonify(data)


def get_names(self):
    persons = json.loads(json.dumps(data))    
    v = {p for p in [person['name'] for person in persons]}
    final = {"Name": list(v)}
    if final:
        return jsonify(final)    
    else:
        return "No records!"
      


def get_name(request):
      if request.args and 'id' in request.args:
            person_id = request.args.get('id')
            if int(person_id) > 1 or int(person_id) < len(data):
                p = [i for i in sorted(data, key=itemgetter('id')) if i["id"] == int(person_id)]
                if p:
                    return jsonify(p)
                else:
                    return 'No such record found!'
            else:
                return "No such record found!"
      else:
            return "Please pass an id query string value!"
