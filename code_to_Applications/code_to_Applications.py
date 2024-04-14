
# -*- coding: cp1251 -*-
from docx import Document
from encodings import utf_8
import docx
from docx.shared import Pt
import os
from docx.shared import Mm
from docx.enum.style import WD_STYLE_TYPE




listfiles = sorted(os.listdir('file/'))


doc = docx.Document()
style3 = doc.styles['Header']
style3.font.name = 'Times New Roman'
style3.font.size = Pt(14)
style3.font.bold = True


style1 = doc.styles['Normal']
style1.font.name = 'Times New Roman'
style1.font.size = Pt(14)


style2 = doc.styles.add_style('Codee', WD_STYLE_TYPE.PARAGRAPH)
style2.font.name = 'Courier New'
style2.font.size = Pt(14)





count = 1;
for file in listfiles:

    par1 = doc.add_paragraph('ПРИЛОЖЕНИЕ ' + str(count))
    par1.style = doc.styles['Header']
    p_fmt = par1.paragraph_format
    p_fmt.first_line_indent = Mm(12.5)
    p_fmt.line_spacing = 1.5
    p_fmt.space_after = Pt(10)

    par2 = doc.add_paragraph(file)
    p_fmt3 = par2.paragraph_format
    p_fmt3.first_line_indent = Mm(12.5)
    p_fmt3.line_spacing = 1.5
    par2.style = doc.styles['Normal']

    
    

    try:  
        f = open('file/' + file,'r', encoding='utf-8')
        print(f)
        for st in f:
            if len(st) > 5:
                st = st.replace('\n','')
                cod1 = doc.add_paragraph(st)

                cod1.style = doc.styles['Codee']
                p_fmt1 = cod1.paragraph_format
                p_fmt3.left_indent = Mm(0)
                p_fmt3.first_line_indent = Mm(12.5)
                p_fmt1.line_spacing = 1
                p_fmt1.space_before = Pt(0)
                p_fmt1.space_after = Pt(0)


        f.close()
    
        
    except:
        print(file + ' : NaN File')

    doc.add_page_break()
    count += 1




doc.save('app.docx')

