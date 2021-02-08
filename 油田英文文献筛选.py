import pyocr
import importlib
import sys
import time
import codecs

importlib.reload(sys)
time1 = time.time()
# print("初始时间为：",time1)
 
import os.path
from pdfminer.pdfparser import  PDFParser,PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal,LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
 

#def shibie(results, field_name):
    

def pdf_txt():
    try:
        #text_path = r'D:\pdf_txt\test1\Marlim Sul-Brazil\da, C., et al., 2014, Insights from the Evaluation of Sand Control Performance in Offshore Brazilian Southeast, SPE168177.pdf'
        #field_name = 'Marlim Sul'
        
        '''解析PDF文本，并保存到TXT文件中'''
        fp = open(text_path,'rb')
        #用文件对象创建一个PDF文档分析器
        parser = PDFParser(fp)
        #创建一个PDF文档
        doc = PDFDocument()
        #连接分析器，与文档对象
        parser.set_document(doc)
        doc.set_parser(parser)
     
        #提供初始化密码，如果没有密码，就创建一个空的字符串
        doc.initialize()
     
        #检测文档是否提供txt转换，不提供就忽略
        if not doc.is_extractable:
            raise PDFTextExtractionNotAllowed
        else:
            #创建PDF，资源管理器，来共享资源
            rsrcmgr = PDFResourceManager()
            #创建一个PDF设备对象
            laparams = LAParams()
            device = PDFPageAggregator(rsrcmgr,laparams=laparams)
            #创建一个PDF解释其对象
            interpreter = PDFPageInterpreter(rsrcmgr,device)
     
            #循环遍历列表，每次处理一个page内容
            # doc.get_pages() 获取page列表
            #f = codecs.open(write_path,'w','utf-8')

            x_str = ''
            for page in doc.get_pages():
                interpreter.process_page(page)
                #接受该页面的LTPage对象
                layout = device.get_result()
                # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象
                # 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等
                # 想要获取文本就获得对象的text属性，
                
                for x in layout:
                    if(isinstance(x,LTTextBoxHorizontal)):
                        #with open(r'2.txt','a') as f:
                        #f.write(x.get_text())
                        results = x.get_text()
                        x_str += results

                        #f.write(results + '\n')
           
            refe = 0
            refe = x_str.find("References")
            if refe == -1:
                refe = x_str.find("Reference")

            if refe == -1:
                refe = x_str.find("REFERENCE")

            if refe == -1:
                refe = x_str.find("REFERENCES")


            field = 0
            field = x_str.find(field_name)
            if field == -1:
                field = x_str.find(field_name_upper)

            if field == -1:
                field = x_str.find(field_name_lower)

            if field == -1:
                field = x_str.find(field_name_upper0)

            if field == -1:
                field = x_str.find(field_name_lower0)


            print('field: ', field)
            print('refe: ', refe)
            
            if (int(field) > int(refe)) and (int(field) != -1) and (int(refe) != -1):
                print(text_path)
                false_pdf_name.write(text_path + '\n')

            elif int(field) == -1:
                print(text_path)
                false_pdf_name.write(text_path + '\n')

    except Exception as e:
        pass


if __name__ == '__main__':
    FileRoot = r'D:\pdf_txt\test1'
    false_pdf_name = codecs.open(r'C:\Users\jzzh\Desktop\false_pdf_name_0.txt','w','utf-8')
    for parent, dirnames, filenames in os.walk(FileRoot):
        for filename in filenames:
            field_name = str(parent.split("test1\\")[1].split("-")[0])
            field_name_upper0 = field_name[0].upper()
            field_name_lower0 = field_name[0].lower()
            field_name_upper = field_name.upper()
            field_name_lower = field_name.lower()
            print("field_name: ", field_name)
            text_path = os.path.join(parent, filename)
            #write_path = text_path.replace(".pdf", ".txt").replace("test1", "test")
            #print('write_path', write_path)
            pdf_txt()
            #read_txt()
            
    time2 = time.time()
    print("总共消耗时间为:",time2-time1)
