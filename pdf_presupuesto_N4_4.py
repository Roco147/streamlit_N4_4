from fpdf import FPDF
from mi_negocio_N4_4 import *

LOGO = "logo.png"

def renglon(pdf, texto, valor):
    pdf.cell(120, 9, texto)
    pdf.cell(0, 9, valor, align="R", new_x="LMARGIN", new_y="NEXT")

def armar_pdf(numero, fecha, cliente, prod1, cant1, prec1, prod2, cant2, prec2, prod3, cant3, prec3, subtotal, descuento, iva, total):
    pdf = FPDF()
    pdf.add_page()

    try:
        pdf.image(LOGO, x=10, y=10, w=28)
    except:
        pass

    pdf.set_font("Helvetica", "B", 20)
    pdf.cell(0, 12, NOMBRE_NEGOCIO, align="R", new_x="LMARGIN", new_y="NEXT")

    pdf.set_font("Helvetica", "", 11)
    pdf.cell(0, 7, f"Presupuesto N° {numero}", align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.cell(0, 7, f"Fecha: {fecha}", align="R", new_x="LMARGIN", new_y="NEXT")
    pdf.ln(15)

    pdf.set_font("Helvetica", "", 12)
    renglon(pdf, "Cliente", cliente)
    
    if cant1 > 0:
        renglon(pdf, f"{cant1} x {prod1}", f"${prec1 * cant1:.2f}")
    if cant2 > 0:
        renglon(pdf, f"{cant2} x {prod2}", f"${prec2 * cant2:.2f}")
    if cant3 > 0:
        renglon(pdf, f"{cant3} x {prod3}", f"${prec3 * cant3:.2f}")
    
    pdf.ln(5)

    renglon(pdf, "Subtotal", f"${subtotal:.2f}")
    renglon(pdf, "Descuento", f"-${descuento:.2f}")
    renglon(pdf, "IVA 21%", f"${iva:.2f}")

    pdf.set_font("Helvetica", "B", 14)
    pdf.set_text_color(0, 210, 211)
    renglon(pdf, "TOTAL", f"${total:.2f}")
    pdf.set_text_color(0, 0, 0)

    pdf.ln(10)
    pdf.set_font("Helvetica", "I", 9)
    pdf.cell(0, 6, "Presupuesto válido por 7 días.")

    return bytes(pdf.output())