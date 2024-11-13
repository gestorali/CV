# sections/profil_section.py

from reportlab.platypus import Paragraph

def get_nazwisko_text(styles):
    profile_text = """
    Michał Kotarski<br />
    Analityk Danych
    """
    return Paragraph(profile_text, styles['PolishTitle'])
