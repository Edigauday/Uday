import xmltodict
import json

my_xml =input("Enter the file Name: ")
with open(my_xml) as xml_file:
    my_dict=xmltodict.parse(xml_file.read())
xml_file.close()
json_data=json.dumps(my_dict)
print(json_data)
