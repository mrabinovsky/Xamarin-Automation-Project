import urllib.request
import shutil
import zipfile
import MySQLdb as db
import fileinput
import webbrowser

paypalurl = "https://github.com/paypal/rest-api-sample-app-php/archive/master.zip"
dburl = "https:\\localhost\\rest-api-sample-app-php\\install\\create_tables.php"
file_name = "paypal.zip"
dest_dir = "c:\\xampp\\htdocs"
sqlsettings = "c:\\xampp\\htdocs\\rest-api-sample-app-php\\app\\bootstrap.php"

print ("Downloading XAMPP 5.6.3")

#with urllib.request.urlopen(xamppurl) as response, open(file_name, 'wb') as out_file:
#    shutil.copyfileobj(response, out_file)
	
print ("Download Done\n")
print ("Unzipping XAMPP")

#with zipfile.ZipFile(file_name, "r") as z:
#    z.extractall(dest_dir)
		
print ("Done Unzipping!\n")
print ("Creating MySQL DB")

con = db.connect(username="root", passwd="")
cur = con.cursor()
cur.execute('CREATE DATABASE paypal_pizza_app;')

print ("Done creating MySQL DB!\n")
print ("Configuring MySQL")

#for line in fileinput.input(sqlsettings, inplace=True):
#    print(line.replace("'MYSQL_HOST', 'localhost:3306'", "'MYSQL_HOST', 'localhost'"), end='')
#	print(line.replace("'MYSQL_PASSWORD', 'root'", "'MYSQL_PASSWORD', ''"), end='')

print ("Done configuring MySQL\n")
print ("Opening create_tables.php to create tables")

webbrowser.open_new(dburl)

print ("Webpage opened\n")
print ("Starting App")

webbrowser.open_new("http://localhost/rest-api-sample-app-php")
