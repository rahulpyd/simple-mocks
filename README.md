# simple-mocks

## Setup 
    $ pip install virtualenv
    $ mkdir mock_server ; cd mock_server
    $ virtualenv env 
    $ source env/bin/activate
    $ git clone https://github.com/rahulpyd/simple-mocks.git
    $ cd simple-mocks
    $ pip install -r requirements.txt
    $ python server.py

    localhost:3000/api/users

## Adding end-points
Add end-points on the same lines as the example in `server.py`

Have your data in `.json` file. Here it is `users.json` .

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


