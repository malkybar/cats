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
    
@app.route('/static-example/img')
def static_example_img():
    start = '<img src="'
    url = url_for("static", filename="vmask.jpg")
    end = '">'
    return start+url+end, 200
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port= "8080", debug=True)