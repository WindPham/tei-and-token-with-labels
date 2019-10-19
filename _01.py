
import numpy as np
import lxml
from lxml import etree as et
import os
from io import StringIO
from io import BytesIO

def solve(f,name):
    #f_new =open(name, "w", encoding="utf-8");
    s="";
    for i in f:
        for j in range(0, len(i)):
            if(i[j]=="&"):
                #f_new.write("&amp;");
                s+="&amp;";
            else:
                #f_new.write(i[j]);
                s+=i[j];
    return s;
                


#path_in = "F:\\Khóa Luận\\XML\\code\\_01\\docs_xml";
#
#l = os.listdir(os.path.expanduser(path_in));
#
#
#f = open(path_in +"\\"+ "101.xml", "r", encoding="utf-8");
#solve(f, path_in +"\\"+ "101_1.xml");



