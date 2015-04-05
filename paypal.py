import urllib.request
import shutil
import zipfile
import _mysql
import subprocess
import re
import webbrowser

paypalurl = "https://github.com/paypal/rest-api-sample-app-php/archive/master.zip"
dburl = "https:\\localhost\\rest-api-sample-app-php-master\\install\\create_tables.php"
file_name = "paypal.zip"
dest_dir_pp = "c:\\xampp\\htdocs"
sqlsettings = "C:\\xampp\\htdocs\\rest-api-sample-app-php-master\\app\\bootstrap.php"

print ("Downloading PayPal App")

#with urllib.request.urlopen(paypalurl) as response, open(file_name, 'wb') as out_file:
#    shutil.copyfileobj(response, out_file)
	
print ("Download Done\n")
print ("Unzipping PayPal")

with zipfile.ZipFile(file_name, "r") as z:
    z.extractall(dest_dir_pp)
		
print ("Done Unzipping!\n")
print ("Updating composer")

subprocess.call("move /y composer.bat c:\\xampp\\htdocs\\rest-api-sample-app-php-master", shell=True)
subprocess.call("move /y c:\\xampp\\htdocs\\rest-api-sample-app-php-master\\composer.json %homepath%\\desktop", shell=True)
subprocess.call("c:\\xampp\\htdocs\\rest-api-sample-app-php-master\\composer.bat update")
subprocess.call("move /y vendor c:\\xampp\\htdocs\\rest-api-sample-app-php-master", shell=True)
subprocess.call("move /y composer.lock c:\\xampp\\htdocs\\rest-api-sample-app-php-master", shell=True)
subprocess.call("move /y composer.json c:\\xampp\\htdocs\\rest-api-sample-app-php-master", shell=True)


print ("Creating MySQL DB")

#db = _mysql.connect(host="localhost",user="root",passwd="")
#db.query('CREATE DATABASE paypal_pizza_app;')

print ("Done creating MySQL DB!\n")
print ("Configuring MySQL")

def replace( filePath, text, subs, flags=0 ):
    with open( filePath, "r+" ) as file:
        fileContents = file.read()
        textPattern = re.compile( re.escape( text ), flags )
        fileContents = textPattern.sub( subs, fileContents )
        file.seek( 0 )
        file.truncate()
        file.write( fileContents )

replace (sqlsettings, "'MYSQL_HOST', 'localhost:3306'", "'MYSQL_HOST', 'localhost'")
replace (sqlsettings, "'MYSQL_PASSWORD', 'root'", "'MYSQL_PASSWORD', ''")

print ("Done configuring MySQL\n")
print ("Opening create_tables.php to create tables")

webbrowser.open_new(dburl)

print ("Webpage opened\n")
print ("Starting App")

webbrowser.open_new("http://localhost/rest-api-sample-app-php-master")

