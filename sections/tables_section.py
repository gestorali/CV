# sections/tables_section.py

from reportlab.platypus import Table, TableStyle, Paragraph, Image
from reportlab.lib import colors
from sections.profil_section import get_profile_text, get_experience1_text, get_experience2_text, get_experience3_text, get_experience4_text, get_experience5_text, get_experience6_text, get_experience7_text, get_experience8_text, get_experience9_text
from sections.short_section import get_nazwisko_text, get_skills_data, get_coding_data,get_languages_data, get_kontakt_text, get_edukacja_text, get_hobby_text

def create_rating_section(title, data, styles, col1_width):
    # Nagłówek sekcji
    section_data = [[Paragraph(f'<u>{title}</u>', styles['PolishSmallTitle'])]]

    # Generowanie wierszy dla ocen
    for name, rating in data:
        stars_full = '<font color="orange">★</font>' * rating
        stars_empty = '<font color="orange">☆</font>' * (5 - rating)
        stars = f"{stars_full}{stars_empty}"
        section_data.append([
            Paragraph(name, styles['PolishSmallText']),
            Paragraph(stars, styles['PolishTitle'])
        ])

    # Tworzenie tabeli
    section_table = Table(section_data, colWidths=[col1_width * 0.55, col1_width * 0.35])
    section_table.setStyle(TableStyle([
        ('SPAN', (0, 0), (-1, 0)),  # Scalanie komórek nagłówka
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0)
    ]))

    return section_table

def get_short_table(col1_width, styles):
    short_table_data = [
        [Image("/mnt/c/Users/micko/OneDrive/Dokumenty/CV/zdjecie/STK_0615-PL Dyplom-45x65 mm.jpg", width=115, height=165)],
        [get_nazwisko_text(styles)],
        [create_rating_section("UMIEJĘTNOŚCI", get_skills_data(), styles, col1_width)],
        [create_rating_section("PROGRAMOWANIE", get_coding_data(), styles, col1_width)],
        [create_rating_section("JĘZYKI", get_languages_data(), styles, col1_width)],
        [get_kontakt_text(styles)],
        [get_edukacja_text(styles)],
        [get_hobby_text(styles)]
    ]
    short_table = Table(short_table_data, colWidths=[col1_width], rowHeights=None)
    short_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.Color(0.85, 0.85, 0.85)),
        #('BACKGROUND', (0, 1), (0, 1), colors.whitesmoke),
        #('BOX', (0, 0), (-1, -1), 1, colors.black),
        #('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('ALIGN', (0, 0), (0, 0), 'CENTER'),
        ('VALIGN', (0, 0), (0, 0), 'TOP')
    ]))
    return short_table

def get_long_table(col2_width, styles):
    long_table_data = [
        [Paragraph("PROFIL", styles['PolishTitle'])],
        [get_profile_text(styles)],
        [Paragraph("DOŚWIADCZENIE", styles['PolishTitle'])],
        [get_experience1_text(styles)], 
        [get_experience2_text(styles)],
        [get_experience3_text(styles)], 
        [get_experience4_text(styles)],
        [get_experience5_text(styles)],
        [get_experience6_text(styles)],
        [get_experience7_text(styles)], 
        [get_experience8_text(styles)],
        [get_experience9_text(styles)]
    ]
    long_table = Table(long_table_data, colWidths=[col2_width], rowHeights=None)
    long_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),         # Tło dla PROFIL   
        ('BACKGROUND', (0, 1), (-1, 1), colors.whitesmoke),        # Tło dla profilu
        ('BACKGROUND', (0, 2), (-1, 2), colors.lightblue),         # Tło dla DOŚWIDCZENIE
        #('BOX', (0, 0), (-1, -1), 1, colors.black),
        #('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        #('LINEBELOW', (0, 0), (0, 0), 0, colors.transparent)
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
