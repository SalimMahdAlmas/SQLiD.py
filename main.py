# - *- coding: utf- 8 - *-
# | CODED BY LittlEvil

from flask import Flask, redirect, url_for, request,render_template
import urllib2
flask_app = Flask(__name__)


def main():
    if flask_app is None:
        print "Sorry flask app is null something went wrong in the environment"
        exit()
    else:
    	flask_app.run(debug = True)
def check(url):
    content_1 = urllib2.urlopen(url).read()
    if not url.__contains__("="):
        return False
    else:
        content_2 = urllib2.urlopen(url + "%27").read()
        if not content_1 == content_2:
            return True
        else:
            return False

@flask_app.route('/SQLiD',methods=['POST', 'GET'])
def index():
	user = None
	if request.method=='POST':
		user=request.form['my_url']
	
	else:
		user=request.args.get('my_url')
	if user is None:
		return "Only for client side"
		
	try:    
		urllib2.urlopen(user)
	except:
		return render_template("error.html",url=user)

	return render_template("check.html", vulu=check(user),url=user)

if __name__ == "__main__":
    main()
