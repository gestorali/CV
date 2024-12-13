from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, PageBreak
from styles import get_styles

# Importy sekcji
from sections.tables_section_ENG import get_main_table

styles = get_styles()

# Konfiguracja dokumentu
margin = 20
pdf_path = "CV_Michal_ENG.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=A4, leftMargin=margin, rightMargin=margin, topMargin=margin, bottomMargin=margin)

# Szerokości kolumn
page_width = A4[0]
available_width = page_width - 2 * margin
col1_width = available_width * 0.25
col2_width = available_width * 0.75

# Generowanie zawartości
content = []
content.append(get_main_table(col1_width, col2_width, styles))  # Użycie main_table z short_table i long_table obok siebie
content.append(PageBreak())

# Tworzenie dokumentu
doc.build(content)
print(f"PDF zapisany jako {pdf_path}")
