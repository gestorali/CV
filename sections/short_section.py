# sections/profil_section.py

from reportlab.platypus import Paragraph

def get_nazwisko_text(styles):
    nazwa = """
    Michał Kotarski<br />
    Analityk Danych
    """
    return Paragraph(nazwa, styles['PolishTitleShort'])

def get_skills_data():
    # Umiejętności z oceną w postaci gwiazdek
     return  [
        ("lojalność", 5),    # 5/5 gwiazdek
        ("analiza", 5),     # 4/5 gwiazdek
        ("adaptacja", 4),    # 4/5 gwiazdek
        ("komunikacja", 4),  # 4/5 gwiazdek
        ("budżetowanie", 4)   # 5/5 gwiazdek
    ]

def get_coding_data():
    # Umiejętności z oceną w postaci gwiazdek
     return  [
        ("SQL", 4),    
        ("Power BI", 3),   
        ("GCP", 2),  
        ("Go", 1),    
        ("Python", 1)  
    ]

def get_languages_data():
    # Umiejętności z oceną w postaci gwiazdek
     return  [
        ("angielski", 4),    
        ("niemiecki", 2),   
        ("francuski", 1),  
    ]

def get_kontakt_text(styles):
    kontakt = """KONTAKT"""
    telefon = """+48 604 669 681"""
    mail = """mickotarski@gmail.com"""
    hyperlink_linkedIN = Paragraph(
    '<a href="https://linkedin.com/in/michalkotarski" color="blue">linkedin.com/in/michalkotarski</a>',
    styles['PolishXSText']
)
    content = []
    content.append(Paragraph(f'<u>{kontakt}</u>', styles['PolishSmallTitle']))
    content.append(Paragraph(telefon, styles['PolishSmallText']))
    content.append(Paragraph(mail, styles['PolishSmallText']))
    content.append(hyperlink_linkedIN)
    return content

def get_edukacja_text(styles):
    edukacja = """EDUKACJA"""
    data1 = """2004 – 2007"""
    edu1 = """Association of Chartered 
            Certified Accountants (ACCA) - 
            wszystkie egzaminy zdane."""
    data2 = """2003"""
    edu2 = """Politechnika Warszawska – 
            roczne studia podyplomowe z 
            zastosowania IT w biznesie"""
    data3 = """1994 – 2000"""
    edu3 = """Szkoła Główna Handlowa – 
            mgr finanse i bankowość,
            specjalizacja księgowość"""
    
    content = []
    content.append(Paragraph(f'<u>{edukacja}</u>', styles['PolishSmallTitle']))
    content.append(Paragraph(data1, styles['PolishSmallTitle']))
    content.append(Paragraph(edu1, styles['PolishSmallText']))
    content.append(Paragraph(data2, styles['PolishSmallTitle']))
    content.append(Paragraph(edu2, styles['PolishSmallText']))
    content.append(Paragraph(data3, styles['PolishSmallTitle']))
    content.append(Paragraph(edu3, styles['PolishSmallText']))
    return content

def get_hobby_text(styles):
    hobby = """HOBBY"""
    hobby1 = """Jazda na rowerze"""
    hobby2 = """Jazda konna"""
    hobby3 = """Literatura faktu"""

    content = []
    content.append(Paragraph(f'<u>{hobby}</u>', styles['PolishSmallTitle']))
    content.append(Paragraph(hobby1, styles['PolishSmallText']))
    content.append(Paragraph(hobby2, styles['PolishSmallText']))
    content.append(Paragraph(hobby3, styles['PolishSmallText']))
    return content