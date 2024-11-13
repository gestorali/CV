# sections/tables_section.py

from reportlab.platypus import Table, TableStyle, Paragraph, Image
from reportlab.lib import colors
from sections.profil_section import get_profile_text, get_experience1_text, get_experience2_text
from sections.short_section import get_nazwisko_text

def get_short_table(col1_width, styles):
    short_table_data = [
        [Image("/mnt/c/Users/micko/OneDrive/Dokumenty/CV/zdjecie/STK_0615-PL Dyplom-45x65 mm.jpg", width=100, height=145)],
        [get_nazwisko_text(styles)],
        [Paragraph("Sekcja 3 - Na dole", styles['PolishBodyText'])]
    ]
    short_table = Table(short_table_data, colWidths=[col1_width], rowHeights=[150, 40, 40])
    short_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), colors.lightgrey),
        ('BACKGROUND', (0, 1), (0, 1), colors.whitesmoke),
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('ALIGN', (0, 0), (0, 0), 'LEFT'),
        ('VALIGN', (0, 0), (0, 0), 'TOP')
    ]))
    return short_table

def get_long_table(col2_width, styles):
    long_table_data = [
        [Paragraph("PROFIL", styles['PolishTitle'])],
        [get_profile_text(styles)],
        [Paragraph("DOŚWIADCZENIE", styles['PolishTitle'])],
        [get_experience1_text(styles)], 
        [get_experience2_text(styles)]  
    ]
    long_table = Table(long_table_data, colWidths=[col2_width], rowHeights=None)
    long_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),         # Tło dla PROFIL   
        ('BACKGROUND', (0, 1), (-1, 1), colors.whitesmoke),        # Tło dla profilu
        ('BACKGROUND', (0, 2), (-1, 2), colors.lightblue),         # Tło dla DOŚWIDCZENIE
        ('BOX', (0, 0), (-1, -1), 1, colors.black),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LINEBELOW', (0, 0), (0, 0), 0, colors.transparent)
    ]))
    return long_table

# Nowa funkcja tworząca main_table z short_table i long_table obok siebie
def get_main_table(col1_width, col2_width, styles):
    short_table = get_short_table(col1_width, styles)
    long_table = get_long_table(col2_width, styles)
    
    # main_table z short_table i long_table obok siebie
    main_table_data = [
        [short_table, long_table]
    ]
    main_table = Table(main_table_data, colWidths=[col1_width, col2_width])
    main_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP')
    ]))
    return main_table
