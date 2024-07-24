from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font(family="Times", style="B", size=12)
#ln is the next line if 0-> same line, 1-> next line
pdf.cell(w=0, h=12, txt="Hello World", border=1, ln=1, align="L")
pdf.cell(w=0, h=12, txt="Hiiii", border=1, ln=1, align="L")
data = pd.read_csv("topics.csv",sep=",")
for index,row in data.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(100,0,100)
    pdf.cell(w=0, h=12, txt=row["Topic"], ln=1, align="L")
    pdf.line(10, 22, 200, 22)
   
        
pdf.output("output.pdf")