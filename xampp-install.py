import urllib.request
import shutil
import zipfile
import fileinput
import subprocess

xamppurl = "http://downloads.sourceforge.net/project/xampp/XAMPP%20Windows/5.6.3/xampp-win32-5.6.3-0-VC11.zip?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fxampp%2Ffiles%2FXAMPP%2520Windows%2F5.6.3%2F&ts=1427859413&use_mirror=iweb"
composerurl = "https://getcomposer.org/download/1.0.0-alpha9/composer.phar"
file_name = "xampp.zip"
dest_dir = "c:\\"
phpini = "c:\\xampp\\php\\php.ini"


print ("Downloading XAMPP 5.6.3")

#with urllib.request.urlopen(xamppurl) as response, open(file_name, 'wb') as out_file:
#    shutil.copyfileobj(response, out_file)
	
print ("Download Done\n")
print ("Unzipping XAMPP")

#with zipfile.ZipFile(file_name, "r") as z:
#    z.extractall(dest_dir)
		
print ("Done Unzipping!\n")
print("Enabling OpenSSL")

#for line in fileinput.input(phpini, inplace=True):
#    print(line.replace(";extension=php_openssl.dll", "extension=php_openssl.dll"), end='')
	
print("OpenSSL Enabled\n")
print("Enabling Curl")

#for line in fileinput.input(phpini, inplace=True):
#    print(line.replace(";extension=php_curl.dll", "extension=php_curl.dll"), end='')
	
print("Curl Enabled\n")
print("Installing Composer")

with urllib.request.urlopen(composerurl) as response, open(file_name, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)
	
subprocess.call("move /y composer.phar c:\\xampp\\php")
open("composer.bat", "w")
file.write("@ECHO OFF\n php \"c:\\xampp\\php\\composer.phar\" %*")
file.close()

setpath = subprocess.Popen([r'C:\WINDOWS\system32\WindowsPowerShell\v1.0\powershell.exe',
                             '-ExecutionPolicy',
                             'Unrestricted',
                             './setpath.ps1'], cwd=os.getcwd())
result = setpath.wait()

print("Composer Installed\n")
print("Starting PayPal app install")

execfile("paypal.py")

