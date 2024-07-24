from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

#ln is the next line if 0-> same line, 1-> next line
data = pd.read_csv("topics.csv",sep=",")
for index,row in data.iterrows():
    
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=12)
    pdf.set_text_color(100,0,100)
    pdf.cell(w=0, h=12, txt=row["Topic"], ln=1, align="L")
    pdf.line(10, 22, 200, 22)
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(190,190,190)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
  
    for p in range(int(row["Pages"])-1):
        pdf.add_page()
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(190,190,190)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

        
pdf.output("output.pdf")
