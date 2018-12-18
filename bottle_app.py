
#####################################################################
### Assignment skeleton
### You can alter the below code to make your own dynamic website.
### The landing page for assignment 3 should be at /
#####################################################################

from bottle import route, run, default_app, debug, static_file
from htmlfiles.index import index
from htmlfiles.characters import characters
from htmlfiles.actors import actors
from htmlfiles.movies import movies
from htmlfiles.gallery import gallery
from htmlfiles.bibliography import bibliography

def server_static(path):
	return static_file(path, root='./htmlfiles')

def img_static(path):
	return static_file(path, root='./htmlfiles/z')

route('/', 'GET', index)
route('/index.html', 'GET', index)
route('/characters.html', 'GET', characters)
route('/actors.html', 'GET', actors)
route('/movies.html', 'GET', movies)
route('/gallery.html', 'GET', gallery)
route('/bibliography.html', 'GET', bibliography)
route('/<path>', 'GET', server_static)
route('/z/<path>', 'GET', img_static)

#####################################################################
### Don't alter the below code.
### It allows this website to be hosted on Heroku
### OR run on your computer.
#####################################################################

# This line makes bottle give nicer error messages
debug(True)
# This line is necessary for running on Heroku
app = default_app()
# The below code is necessary for running this bottle app standalone on your computer.
if __name__ == "__main__":
  run()

