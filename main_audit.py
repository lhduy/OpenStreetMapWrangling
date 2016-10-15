#Ver 1.0 works for tag "node"

import xml.etree.cElementTree as ET
import pprint
import re
from collections import defaultdict
import datetime

#correct city name "Amsterdam":
def update_city(name):
    if name.endswith(" "):
        name = name[0:(len(name)-1)]
    if name == "Amsteram":
        name = "Amsterdam"
    return name

#correct gate type format
def update_gatetype(name):
    if name == "gate_type":
        return "gate:type"
    return name

#correct the telephone number:
def update_telephone(num):
    num = num.replace('+','').replace('-',"").replace(" ","")
    new_num = '0' + num[(len(num)-9):]
    new_num = new_num[:3] + '-' + new_num[3:7] + '-' + new_num[7:]
    return new_num

#correct the postal code
def update_postalcode(name):
    if " " in name:
        name = name.replace(" ","")
    return name

#verify tag name
def is_audit_type(elem,tag_name):
    return (elem.attrib['k'] == tag_name)

# Main function to classify the map problem
def audit(child_node):
    if is_audit_type(child_node,"addr:postcode"):
        child_node.attrib['v'] = update_postalcode(child_node.attrib['v'])
    if is_audit_type(child_node,"phone"):
        child_node.attrib['v'] = update_telephone(child_node.attrib['v'])
    if is_audit_type(child_node,"gate:type"):
        child_node.attrib['k'] = update_gatetype(child_node.attrib['k'])
    if is_audit_type(child_node,"addr:city"):
        child_node.attrib['v'] = update_city(child_node.attrib['v'])

    return child_node