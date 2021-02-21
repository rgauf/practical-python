# lib of URL functions.  Get page at URL
import urllib.request
u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14791&route=22')
# lib of XML functions.  Parse XML page result into an ElementTree object
from xml.etree.ElementTree import parse
doc = parse(u)
# search all levels in Tree for 'pt' tag, print TEXT of the tag
for pt in doc.findall('.//pt'):
    print(pt.text)
    
# here are some other Tree processing examples.  See doc page for ElementTree.
# root info
root = doc.getroot()
print('RootTag:', root.tag, 'Attrib:', root.attrib, 'Text:', root.text)
# info about first level down from root
print('Children of Root:')
for child in root:
    print(child.tag)
    
# info about 'pre' tags one level down
for e in doc.findall('./pre'):
    print('Childtag:', e.tag, 'Attrib:', e.attrib, 'Text:', e.text)
    
# info about those 'pt' tags we looked for earlier
for e in doc.findall('.//pt'):
    print('PT search found:', e.tag, 'Attrib:', e.attrib, 'Text:', e.text)
    
