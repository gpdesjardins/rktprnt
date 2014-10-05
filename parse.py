import xml.etree.ElementTree as ET
tree = ET.parse('estes_patriot.rkt')
root = tree.getroot()

for NoseCone in root.iter('NoseCone'):
    Len = NoseCone.find('Len').text
    print( "Length = " + Len + ";")
	
for FinSet in root.iter('FinSet'):
	Thickness = FinSet.find('Thickness').text
	print("Thickness = " + Thickness + ";")

