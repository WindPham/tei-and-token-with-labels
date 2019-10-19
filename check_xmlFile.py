
import numpy as np
import lxml
from lxml import etree as et
import os
from io import StringIO
from io import BytesIO

def solve(f):
    #f_new =open(name, "w", encoding="utf-8");
    s="";
    for i in f:
        for j in range(0, len(i)):
            if(i[j]=="&"):
                #f_new.write("&amp;");
                s+="&amp;";
                continue;
            #if(i[j]=='"'):
            #    s+="&quot;";
            #    continue;
            #if(i[j]=="'"):
            #    s+="&apos;";
            #    continue;
            #if(i[j]=="<"):
            #    s+="&lt;";
            #    continue;
            #if(i[j]==">"):
            #    s+="&gt;";
            #    continue;
            s+=i[j];
    return s;

def check_xml_file(path):
    list_of_names = os.listdir(os.path.expanduser(path));
    for name in list_of_names:
        perfect_path = path+"\\"+name;
        f = open(perfect_path, "r", encoding="utf-8");
        s = solve(f);
        f.close();
        f = open(perfect_path, "w", encoding="utf-8");
        f.write(s);
        f.close();
    return;

path_in = "F:\\Khóa Luận\\XML\\code\\_01\\docs_xml";

#check_xml_file(path_in);