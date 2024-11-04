from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

# Ustawienia marginesów
margin = 20  # Margines 20 punktów z każdej strony
page_width = A4[0]  # Szerokość strony A4 (595 punktów)
available_width = page_width - 2 * margin  # Szerokość dostępna dla tabeli

# Ustawienia szerokości kolumn
col1_width = available_width * 0.2  # 30% dostępnej szerokości dla pierwszej kolumny (short_table)
col2_width = available_width * 0.8  # 70% dostępnej szerokości dla drugiej kolumny (long_table)


# Ścieżka do pliku PDF
pdf_path = "CV_Michal.pdf"

# Rejestracja czcionki DejaVu Sans, która obsługuje polskie znaki
pdfmetrics.registerFont(TTFont('DejaVuSans', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))

# Konfiguracja dokumentu
doc = SimpleDocTemplate(pdf_path, pagesize=A4, leftMargin=margin, rightMargin=margin, topMargin=margin, bottomMargin=margin)
styles = getSampleStyleSheet()

# Tworzenie stylu dla tekstu z czcionką DejaVu Sans
styles.add(ParagraphStyle(name='PolishBodyText', fontName='DejaVuSans', fontSize=10, leading=12, alignment=4))  # Justified
styles.add(ParagraphStyle(name='PolishTitle', fontName='DejaVuSans', fontSize=16, leading=20, spaceAfter=12))

content = []

# Dane do tabeli short_table z jedną kolumną
short_table_data = [
    [Image("/mnt/c/Users/micko/OneDrive/Dokumenty/CV/zdjecie/STK_0615-PL Dyplom-45x65 mm.jpg", width=100, height=145)],
    [Paragraph("Sekcja 1 - Po lewej z obrazem", styles['PolishBodyText'])],
    [Paragraph("Sekcja 3 - Na dole", styles['PolishBodyText'])]
]

# Ustawienia szerokości kolumn i wysokości wierszy
short_table = Table(short_table_data, colWidths=[col1_width], rowHeights=[150, 40, 40])
short_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (0, 0), colors.lightgrey),       # Tło dla pierwszego wiersza
    ('BACKGROUND', (0, 1), (0, 1), colors.whitesmoke),      # Tło dla drugiego wiersza
    ('BOX', (0, 0), (-1, -1), 1, colors.black),             # Obramowanie wokół tabeli
    ('GRID', (0, 0), (-1, -1), 0.5, colors.black),          # Siatka między komórkami
    ('ALIGN', (0, 0), (0, 0), 'LEFT'),                       # Wyrównanie obrazu do lewej
    ('VALIGN', (0, 0), (0, 0), 'TOP'),                       # Wyrównanie obrazu do góry
]))

# Tabela long_table
long_table_data = [
    [Paragraph("Sekcja 2 - Po prawej", styles['PolishBodyText'])],
    [Paragraph("Dodatkowa sekcja 1", styles['PolishBodyText'])],
    [Paragraph("Dodatkowa sekcja 2", styles['PolishBodyText'])]
]
long_table = Table(long_table_data, colWidths=[col2_width], rowHeights=[80, 50, 30])
long_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),
    ('BACKGROUND', (0, 1), (-1, 1), colors.whitesmoke),
    ('BOX', (0, 0), (-1, -1), 1, colors.black),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
    ('VALIGN', (0, 0), (-1, -1), 'TOP')
]))

# Tabela nadrzędna, która zawiera short_table i long_table
main_table_data = [
    [short_table, long_table]
]
main_table = Table(main_table_data, colWidths=[col1_width, col2_width])  # Ustawienie szerokości tabel
main_table.setStyle(TableStyle([
    ('VALIGN', (0, 0), (-1, -1), 'TOP')
]))

content.append(main_table)
content.append(PageBreak())  # Dodanie przejścia do następnej strony

# Dodanie kolejnych elementów na drugiej stronie
# Dodanie hiperłącza i zakończenia
hyperlink = Paragraph(
    '<a href="https://www.example.com" color="blue">Kliknij tutaj, aby przejść do strony (example.com)</a>', 
    styles['PolishBodyText']
)
content.append(hyperlink)
content.append(Spacer(1, 12))

closing_note = Paragraph("To jest przykładowy PDF z równoległymi tabelami, obrazem i linkiem.", styles['PolishBodyText'])
content.append(closing_note)

# Tworzenie dokumentu
doc.build(content)
print(f"PDF zapisany jako {pdf_path}")
