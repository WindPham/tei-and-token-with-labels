import numpy as np
import lxml
from lxml import etree as et
import os

import file_py_tei_header as header
import file_py_tei_text as text

class tei(object):
    def __init__(self, path_xml_in,path_txt_in, path_out_xml_teiFormat):
        self.path_xml_in=path_xml_in;
        self.path_txt_in=path_txt_in;
        self.path_out_xml=path_out_xml_teiFormat;
        return;
    def create_tei(self, init_number=0):
        list_of_xmls_in = header.read_files(self.path_xml_in);
        list_of_txts_in = text.read_files(self.path_txt_in);
        for i in range(0, len(list_of_xmls_in)):
            teiHeader = header.create_a_header(doc=list_of_xmls_in[i], id=str(i), order=str(i));
            teiText = text.create_a_text(doc=list_of_txts_in[i], id=str(i), order=str(i));
            TEI =et.Element("tei");
            TEI.attrib["id"]="00000000";
            TEI.append(teiHeader);
            TEI.append(teiText);
            name = self.path_out_xml+"\\"+str(init_number+i)+".xml";
            f = open(name, "w", encoding="utf-8");
            f.write('<?xml version=\"1.0\" encoding=\"utf-8\"?>\n');
            f.write(et.tostring(TEI, encoding="unicode"));
            f.close();
        return 1;




        


