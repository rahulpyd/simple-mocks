import json
import os
from flask import Flask, Response, request

app = Flask(__name__, static_url_path='', static_folder='public')
# app.add_url_rule('/', 'root', lambda: app.send_static_file('index.html'))

@app.route('/api/users', methods=['GET', 'POST'])
def mydata_handler():
    with open('users.json', 'r') as file:
       users = json.loads(file.read())

    if request.method == 'POST':
        data.append(request.form.to_dict())

        with open('users.json', 'w') as file:
            file.write(json.dumps(users, indent=4, separators=(',', ': ')))

    return Response(json.dumps(users), mimetype='application/json', 
                                        headers={'Cache-Control': 'no-cache'})

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT",3000)))
