from flask import Flask, redirect, url_for, abort, render_template, request
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

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route("/goodbye/")
def goodbye():
        return "Goodbye cruel world :("
    
@app.route("/maxwell/")
def maxwell():
    start = '<img src="'
    url = url_for("static", filename="upload.png")
    end = '">'
    return  start+url+end, 200

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

@app.route("/account/", methods = ['GET', 'POST'])
def account():
    if request.method == 'POST':
        print(request.form)
        name = request.form['name']
        return "Hello %s" % name
    else:
        page = '''
        <html><body>
            <form action="" method="post" name="form">
                <label for="name">Name:</label>
                <input type="text" name="name" id="name"/>
                <input type="submit" name="submit" id="submit"/>
            </form>
            </body><html>'''
            
        return page

@app.route("/upload/", methods = ['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['datafile']
        f.save('static/uploads/upload.png')
        return "File Uploaded"
    else:
        page = '''
        <html>
        <body>
        <form action="" method="post" name="form" enctype="multipart/form-data">
        <input type="file" name="datafile"/>
        <input type="submit" name="submit" id="submit"/>
        </form>
        </body>
        </html>'''
            
        return page, 200

app.route("/display/")
def display():
    return '<img src="'+url_for('static', filename='uploads/file.png')+'"/>'
    
@app.route("/add/<int:first>/<int:second>")
def add(first, second):
    return str(first+second)

@app.route('/users/')
def users():
    names = ['maxwell', 'kenobi', 'beluga', 'neil', 'grevious']
    return render_template('loops.html', names=names)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port= "8080", debug=True)