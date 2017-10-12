import pip

def install(package):
    pip.main(['install', package])

print "Installing any dependencies"
install ('idna')
install ('BeautifulSoup4')

print "Example to use the script ( python domain-check.py 'best domain' )"
