import urllib.request
import shutil
import zipfile
import fileinput
import subprocess

xamppurl = "http://downloads.sourceforge.net/project/xampp/XAMPP%20Windows/5.6.3/xampp-win32-5.6.3-0-VC11.zip?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fxampp%2Ffiles%2FXAMPP%2520Windows%2F5.6.3%2F&ts=1427859413&use_mirror=iweb"
composerurl = "http://getcomposer.org/download/1.0.0-alpha9/composer.phar"
pymysqlurl= "https://github.com/PyMySQL/mysqlclient-python/archive/master.zip"
file_name_xampp = "xampp.zip"
file_name_py = "pymysql.zip"
dest_dir = "c:\\"
phpini = "c:\\xampp\\php\\php.ini"


print ("Downloading XAMPP 5.6.3")

with urllib.request.urlopen(xamppurl) as response, open(file_name_xampp, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)
	
print ("Download Done\n")
print ("Unzipping XAMPP")

with zipfile.ZipFile(file_name_xampp, "r") as z:
    z.extractall(dest_dir)
		
print ("Done Unzipping!\n")
print("Enabling OpenSSL")

for line in fileinput.input(phpini, inplace=True):
    print(line.replace(";extension=php_openssl.dll", "extension=php_openssl.dll"), end='')
	
print("OpenSSL Enabled\n")
print("Enabling Curl")

for line in fileinput.input(phpini, inplace=True):
   print(line.replace(";extension=php_curl.dll", "extension=php_curl.dll"), end='')
	
print("Curl Enabled\n")
print("Installing Composer")

with urllib.request.urlopen(composerurl) as response, open("composer.phar", 'wb') as out_file:
    shutil.copyfileobj(response, out_file)
	
subprocess.call("move /y composer.phar c:\\xampp\\php", shell=True)
with open("composer.bat", "w") as f:
    f.write("@ECHO OFF\n c:\\xampp\\php\\php.exe \"c:\\xampp\\php\\composer.phar\" %*")
f.close

print("Composer Installed\n")
print("Installing PyMySQL")

subprocess.call("pip install mysqlclient")
                
print("PyMySQL Installed\n")
print("Starting XAMPP")

subprocess.call("c:\\xampp\\xampp_start.exe")

print("Starting PayPal app install")

exec(open("paypal.py").read())

