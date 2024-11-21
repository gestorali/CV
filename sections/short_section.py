# sections/profil_section.py

from reportlab.platypus import Paragraph

def get_nazwisko_text(styles):
    profile_text = """
    Michał Kotarski<br />
    Analityk Danych
    """
    return Paragraph(profile_text, styles['PolishTitle'])

def get_skills_data():
    # Umiejętności z oceną w postaci gwiazdek
     return  [
        ("Język angielski", 4),    # 4/5 gwiazdek
        ("SQL", 5),                # 5/5 gwiazdek
        ("Python", 3),             # 3/5 gwiazdek
        ("Power BI", 4),           # 4/5 gwiazdek
        ("Komunikacja", 5)         # 5/5 gwiazdek
    ]