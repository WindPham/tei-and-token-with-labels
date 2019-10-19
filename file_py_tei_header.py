import numpy as np
import lxml
from lxml import etree as et
import os
from io import StringIO
from io import BytesIO
import file_py_tei_header_fileDesc as fileDesc
import file_py_tei_header_profileDesc as profileDesc
import file_py_tei_header_revisionDesc as revisionDesc
import file_py_tei_header_encodingDesc as encodingDesc

def create_a_header(doc=None, id="", order=""):
    header = et.Element("teiHeader");
    header.append(fileDesc.create_an_element_for_a_fileDesc(doc=doc));
    header.append(encodingDesc.create_an_element_for_encodingDesc());
    header.append(profileDesc.create_an_element_for_a_profileDesc(doc = doc));
    header.append(revisionDesc.create_an_element_for_a_revisionDesc());
    return header;

def write_header(list_of_docs, path, init_number):
    count = 0;
    for doc in list_of_docs:
        count+=1;
        header = create_a_header(doc=doc, id=str(count), order=str(count));
        name = str(init_number + count)+".xml";
        f=open(path + "\\" + name, 'w', encoding="utf-8");
        f.write('<?xml version=\"1.0\" encoding=\"utf-8\"?>\n');
        f.write(et.tostring(header, encoding="unicode"));
    return 0;

def read_files(path):

    list_of_fileXML=[];

    list_of_filenames = os.listdir(os.path.expanduser(path));

    for filename in list_of_filenames:
        name = path + "\\" + filename;
        doc = et.parse(name);
        list_of_fileXML.append(doc);
    return list_of_fileXML;


#path_in = "F:\\Khóa Luận\\XML\\code\\_01\\docs_xml";
#path_out= "F:\\Khóa Luận\\XML\\code\\_01\\docs_demo";
#
#write_header(read_files(path_in), path_out, 1);
