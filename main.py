import flask

app=flask.Flask(__name__)
nowSensor=0

@app.route('/')
def main():
    global nowSensor
    return flask.render_template('index.html',sensor=nowSensor)

@app.route('/login')
def login():
    return flask.render_template('login.html')

@app.errorhandler(404)
def errorPage(e):
    return flask.render_template('404.html'),404

@app.route('/sensor')
def sensor():
    global nowSensor
    try:
        data=flask.request.args
        if data['data']:
            nowSensor=data['data']
        return flask.redirect('/')
    except:
        return flask.redirect('/')

    

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)