from struct import *
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
import MySQLdb

# create our little application :)
app = Flask(__name__)
app.debug = True
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def connect_db():
    return MySQLdb.connect(host="localhost",user="root",
                  		passwd="verygame123",db="coconutIsland",charset = "utf8")

@app.before_request
def before_request():
	g.db=connect_db()
	g.cur=g.db.cursor()

@app.teardown_request
def teardown_request(exception):
    g.db.close()

@app.route('/')
@app.route('/moregames/landscape')
def landscape():
    g.cur.execute('select icon, title, text, paidLink, price, freeLink from moreGames order by id')
    games = [dict(icon = row[0], title=row[1], text=row[2],
    		paidLink=row[3], price=row[4], freeLink=row[5]) for row in g.cur.fetchall()]
    return render_template('moreGames.html', games=games, cssfile=url_for('static', filename='moreGamesLandscape.css'), paidLable='BUY IN<br/>APP STORE', freeLable='TRY FOR FREE')
    
@app.route('/moregames/portrait')
def portait():
    g.cur.execute('select icon, title, text, paidLink, price, freeLink from moreGames order by id')
    games = [dict(icon = row[0], title=row[1], text=row[2],
    		paidLink=row[3], price=row[4], freeLink=row[5]) for row in g.cur.fetchall()]
    return render_template('moreGames.html', games=games, cssfile=url_for('static', filename='moreGamesPortrait.css'),  paidLable='', freeLable='FREE')

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
    #http_server = HTTPServer(WSGIContainer(app))
    #http_server.listen(8000)
    #IOLoop.instance().start()
