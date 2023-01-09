import flask
import datetime


app=flask.Flask(__name__)
nowSensor=0

def loginAuth():
    if flask.request.cookies.get('userID')==None:
        return False
    return True

@app.route('/',methods=['GET','POST'])
def main():
    if flask.request.method=='GET':
        if flask.request.cookies.get('userID'):
            return flask.redirect('/logout')
        return flask.render_template('index.html')
    userID=flask.request.form.get('UserID')
    resp=flask.make_response(flask.redirect('/recent'))
    resp.set_cookie(key='userID',value=userID,max_age=datetime.timedelta(days=7))
    return resp

@app.route('/recent')
def recent():
    if loginAuth():
        return flask.render_template('recent.html',userID=flask.request.cookies.get('userID'))
    else:
        return flask.redirect('/')

@app.route('/history')
def history():
    if loginAuth():
        return flask.render_template('history.html',userID=flask.request.cookies.get('userID'))
    return flask.redirect('/')

@app.route('/logout')
def logout():
    resp=flask.make_response(flask.redirect('/'))
    try:
        resp.delete_cookie('userID')
    except:
        pass
    return resp

@app.errorhandler(404)
def errorPage(e):
    return flask.render_template('404.html'),404


if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)