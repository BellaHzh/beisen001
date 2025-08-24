# This program scrapes source code from an HTML web page.

import urllib.request
import ssl

# This presents a security risk if the website is not a trusted source
ssl._create_default_https_context = ssl._create_unverified_context

# Mac users, it's preferable to update SSL certificates in order to securely access web pages.
# Applications > Python > 3.# > Install > Certificates.command

# Acess web page
page = urllib.request.urlopen('https://cs.nyu.edu/cs/faculty/clayton/')

# Read the contents of the page into computer memory
source_code = page.read()

# Convert bytes to Unicode string
source_code = source_code.decode('utf-8')

# Print out the source code of the web page
print(source_code)
