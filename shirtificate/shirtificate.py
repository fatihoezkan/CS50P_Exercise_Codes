from fpdf import FPDF

# class PDF():
#     def __init__(self,name):
#         self._pdf = FPDF()
#         self._pdf.add_page()
#         self._pdf.set_font("halvetica","B",40)
#         self._pdf.cell(0,60,"CS50 Shirtificate", align="C")
#         self._pdf.image("shirtificate.png", w=self._pdf.epw)
#         self._pdf.set_font_size(28)
#         # self._pdf.set_color(255,255,255)
#         self._pdf.text(x=48,y=140,txt=f"{name} took CS50")


#     def save(self,name):
#         self._pdf.save(name)

# name = input("Name: ")
# pdf = PDF(name)
# pdf.save("shirtificate.pdf")

# # pdf = FPDF()
# # pdf = fpdf.FPDF(orientation="Portrait", format="A4")


from fpdf import FPDF

class PDF():
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("Helvetica", "B", 40)
        self._pdf.cell(0, 60, "CS50 Shirtificate", align="C", ln=True)  # `ln=True` moves to the next line
        self._pdf.image("shirtificate.png", x=10, y=80, w=self._pdf.epw)  # Adjust image placement
        self._pdf.set_font("Helvetica", size=28)
        self._pdf.set_text_color(255, 255, 255)  # Set white text color
        self._pdf.text(x=48, y=140, txt=f"{name} took CS50")

    def save(self, filename):
        self._pdf.output(filename)  # Use `output` instead of `save`

name = input("Name: ")
pdf = PDF(name)
pdf.save("shirtificate.pdf")
