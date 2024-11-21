from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

# Importy sekcji
from sections.tables_section import get_main_table

# Konfiguracja dokumentu
margin = 20
pdf_path = "CV_Michal.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=A4, leftMargin=margin, rightMargin=margin, topMargin=margin, bottomMargin=margin)
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='PolishBodyText', fontName='DejaVuSans', fontSize=9, leading=11, alignment=4))
styles.add(ParagraphStyle(name='PolishBodyTextBold', fontName='DejaVuSans-Bold', fontSize=9, leading=11, alignment=4))
styles.add(ParagraphStyle(name='PolishTitle', fontName='DejaVuSans-Bold', fontSize=10, leading=12, spaceBefore=3, spaceAfter=3))
styles.add(ParagraphStyle(name='PolishSmallTitle', fontName='DejaVuSans-Bold', fontSize=8, leading=10, alignment=1, underline=True))  # alignment=1 to CENTER
styles.add(ParagraphStyle(name='PolishSmallText', fontName='DejaVuSans', fontSize=8, leading=10))
styles.add(ParagraphStyle(name='BulletStyle', fontName='DejaVuSans',fontSize=9, leading=11))

# Konfiguracja czcionek
pdfmetrics.registerFont(TTFont('DejaVuSans', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuSans-Bold', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))

# Szerokości kolumn
page_width = A4[0]
available_width = page_width - 2 * margin
col1_width = available_width * 0.2
col2_width = available_width * 0.8

# Generowanie zawartości
content = []
content.append(get_main_table(col1_width, col2_width, styles))  # Użycie main_table z short_table i long_table obok siebie
content.append(PageBreak())

# Tworzenie dokumentu
doc.build(content)
print(f"PDF zapisany jako {pdf_path}")
