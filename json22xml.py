import sys
import json

from types import *
from xml.etree.ElementTree import TreeBuilder, tostring

def parserbuilder(data, tag_name, builder, indent="\n     "):
    t = type(data)
    if t == NoneType:
        builder.start(tag_name, {})
        builder.end(tag_name)
    elif t in (StringType, UnicodeType, IntType, FloatType, BooleanType, LongType):
        builder.data(indent)
        builder.start(tag_name, {})
        builder.data(unicode(data))
        builder.end(tag_name)
    elif t in (ListType, TupleType):
        #indent = indent + "    ";        
        for value in data:
        	if(str(tag_name)!="stacktrace" and str(tag_name)!="exception" and str(tag_name)!="message"):
        		parserbuilder(value, tag_name, builder, indent)
            
        builder.data(indent)
    elif t == DictionaryType:
        builder.data(indent)
        builder.start(tag_name, {})
        indent = indent + "    ";
        for key, value in data.items():
            parserbuilder(value, key, builder, indent)
        indent = indent[0:len(indent)-4]
        builder.data(indent)
        builder.end(tag_name)
    return builder

    
#filename = "./championships/week02/qae.json"


filename = sys.argv[1]
filexml = sys.argv[2]
i=0;
jsonfile = open(filename);
json_data = json.loads(jsonfile.read())
jsonfile.close()
xmlfile = open(filexml, "w")

xmlfile.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
xmlfile.write(open("dtd.xml").read())
xmlfile.write("\n<alldata>\n    ")
for data in json_data:
    builder = parserbuilder(data, "data", TreeBuilder())
    doc = builder.close()
    xml = tostring(doc, encoding='utf-8') + "\n"
    xml.replace("data", str(i))
    xmlfile.write("     " + xml)
    i+=1;
xmlfile.write("</alldata>")
xmlfile.close();
