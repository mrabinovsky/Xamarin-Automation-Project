These are simple scripts that assumes you have windows vista (or server equivalent) or newer (preferably 8.1 32bit as it is what it was tested on) fully patched with python 3.4 installed in the C directory. To run the scripts first copy them over to the desktop, or any other directory of your choosing for which you have read/write access.

*PART1 - Setting up windows firewall*
This is a very simple python script that simply runs windows firewall commands in the windows command line interface. What it does is set default rules to block all inbound and allow all outbound, delete all the predefined windows inbound rules, and add costum rules based on the rules predefined by the project.
Simply open Command prompt and type in firewall.py

*PART 2 - Installing the Application*
This script installs the requirements to run the PayPal web app and then the app itself. Just open up a command prompt and type in install-xampp.py to begin and the script should do the rest.

What the script does:
Downloads xampp, uncompressed it, changes some settings, gets dependencies for the web app and runs the second script paypal.py 
paypal.py gets the app, finishes setting up the dependencies, creates a DB, sets up the tables, and finally runs the app.

firewall-delete.py is just to undue the custom firewall rules for testing purposes (it does not restore the default windows rules though, for that I recommend exporting them first)
