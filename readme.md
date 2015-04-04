This is a simple script that assumes you have windows (preferably 8.1 32bit as it is what it was tested on) fully patched with python 3.4 installed in the C directory.
Just open up a command prompt and type in install-xampp.py to begin and the script should do the rest.

What the script does:
Downloads xampp, uncompressed it, changes some settings, gets dependencies for the web app and runs the second script paypal.py 
paypal.py gets the app, finishes setting up the dependencies, creates a DB, sets up the tables, and finally runs the app.