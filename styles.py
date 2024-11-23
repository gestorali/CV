from reportlab.lib.styles import ParagraphStyle,getSampleStyleSheet
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

# Konfiguracja czcionek
pdfmetrics.registerFont(TTFont('DejaVuSans', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuSans-Bold', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))

def get_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name='PolishBodyText', fontName='DejaVuSans', fontSize=9, leading=11, alignment=4))
    styles.add(ParagraphStyle(name='PolishBodyTextBold', fontName='DejaVuSans-Bold', fontSize=9, leading=11, alignment=4))
    styles.add(ParagraphStyle(name='PolishTitle', fontName='DejaVuSans-Bold', fontSize=10, leading=12, spaceBefore=3, spaceAfter=3))
    styles.add(ParagraphStyle(name='PolishSmallTitle', fontName='DejaVuSans-Bold', fontSize=8, leading=10, alignment=1, underline=True))  # alignment=1 to CENTER
    styles.add(ParagraphStyle(name='PolishSmallText', fontName='DejaVuSans', fontSize=8, leading=10))
    styles.add(ParagraphStyle(name='BulletStyle', fontName='DejaVuSans',fontSize=9, leading=11))
    return styles
