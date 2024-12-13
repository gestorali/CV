# sections/profil_section.py

from reportlab.platypus import Paragraph

def get_nazwisko_text(styles):
    nazwa = """
    Michał Kotarski<br />
    Data Analyst
    """
    return Paragraph(nazwa, styles['PolishTitleShort'])

def get_skills_data():
    # Umiejętności z oceną w postaci gwiazdek
     return  [
        ("loyalty", 5),    # 5/5 gwiazdek
        ("analyses", 5),     # 4/5 gwiazdek
        ("adaptability", 4),    # 4/5 gwiazdek
        ("communication", 4),  # 4/5 gwiazdek
        ("budgeting", 4)   # 5/5 gwiazdek
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
        ("English", 4),    
        ("German", 2),   
        ("French", 1),  
    ]

def get_kontakt_text(styles):
    kontakt = """CONTACT"""
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
    edukacja = """EDUCATION"""
    data1 = """2004 – 2007"""
    edu1 = """Association of Chartered 
            Certified Accountants ACCA
            all exams passed."""
    data2 = """2003"""
    edu2 = """Warsaw University of Technology – 
            one-year postgraduate studies
            IT applications in business"""
    data3 = """1994 – 2000"""
    edu3 = """Warsaw School of Economics – 
            Master of Science in Finance and Banking,
            specialization in accounting"""
    
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
    hobby1 = """cycling"""
    hobby2 = """horse riding"""
    hobby3 = """non-fiction books"""

    content = []
    content.append(Paragraph(f'<u>{hobby}</u>', styles['PolishSmallTitle']))
    content.append(Paragraph(hobby1, styles['PolishSmallText']))
    content.append(Paragraph(hobby2, styles['PolishSmallText']))
    content.append(Paragraph(hobby3, styles['PolishSmallText']))
    return content