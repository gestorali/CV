# sections/tables_section.py

from reportlab.platypus import Table, TableStyle, Paragraph, Image
from reportlab.lib import colors
from sections.profil_section import get_profile_text, get_experience1_text, get_experience2_text
from sections.short_section import get_nazwisko_text, get_skills_data

def create_skills_table(styles, col1_width):
    # Pobranie danych o umiejętnościach
    skills = get_skills_data()
    
    # Generowanie tabeli z umiejętnościami i gwiazdkami
    skills_data = []

    # Dodanie nagłówka z podkreśleniem, który zajmuje całe dwie kolumny
    skills_data.append([
        Paragraph('<u>UMIEJĘTNOŚCI</u>', styles['PolishSmallTitle'])
    ])

    for skill, rating in skills:
        # Pełne gwiazdki
        stars_full = '<font color="orange">★</font>' * rating
        # Puste gwiazdki
        stars_empty = '<font color="orange">☆</font>' * (5 - rating)
        # Łączenie pełnych i pustych gwiazdek
        stars = f"{stars_full}{stars_empty}"
        skills_data.append([Paragraph(skill, styles['PolishSmallText']), Paragraph(stars, styles['PolishSmallText'])])

    # Tworzenie tabeli
    skills_table = Table(skills_data, colWidths=[col1_width * 0.55, col1_width * 0.35])
    skills_table.setStyle(TableStyle([
        ('SPAN', (0, 0), (-1, 0)),  # Scal pierwszą komórkę z ostatnią w wierszu 0 dla nagłówka
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),               # Wyśrodkowanie nagłówka
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),   # Brak lewego marginesu w komórkach
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),  # Brak prawego marginesu w komórkach
        ('TOPPADDING', (0, 0), (-1, -1), 0),    # Minimalny odstęp od góry
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0)  # Minimalny odstęp od dołu
    ]))

    return skills_table

def get_short_table(col1_width, styles):
    short_table_data = [
        [Image("/mnt/c/Users/micko/OneDrive/Dokumenty/CV/zdjecie/STK_0615-PL Dyplom-45x65 mm.jpg", width=100, height=145)],
        [get_nazwisko_text(styles)],
        [create_skills_table(styles, col1_width)],  # Użycie funkcji generującej tabelę umiejętności
        [create_skills_table(styles, col1_width)]  # Użycie funkcji generującej tabelę umiejętności
    ]
    short_table = Table(short_table_data, colWidths=[col1_width], rowHeights=None)
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
