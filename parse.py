import xml.etree.ElementTree as ET
tree = ET.parse('Big_Bertha_3.ork')
root = tree.getroot()

for nosecone in root.iter('nosecone'):
    length = nosecone.find('length').text
    print "length: " + length