from flask import Flask, redirect, url_for, abort
app = Flask(__name__)

@app.route("/private")
def private():
    #test for user logged in failed
    #so redirect to login url
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return "Now we should get a username and password"

@app.route("/")
def root():
    return "The default, 'root' route"

@app.route("/hello/")
def hello():
    return "Hello Napier!!! :D"

@app.route("/goodbye/")
def goodbye():
        return "Goodbye cruel world :("
    
@app.route("/maxwell/")
def maxwell():
    return "Maxwell the chonky cat"

@app.errorhandler(404)
def page_not_found(error):
    return "Couldn't find the page you requested.", 404

@app.route('/force404')
def force404():
    abort(404)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)