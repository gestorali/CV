# sections/profil_section.py

from reportlab.platypus import Paragraph

def get_profile_text(styles):
    profile_text = """
    Po dwudziestu latach pracy w różnych działach finansowych zmieniłem profil działalności na obszar IT. Jako konsultant współpracowałem z działami finansowymi klientów i tworzyłem dla nich raporty w Power BI. Dane, przechowywane w chmurze – Google Cloud Platform lub Azure Databricks – przygotowywałem głównie w SQL, a czasami w Power Query. Obecnie pracuję jako analityk danych w banku, gdzie korzystam z Oracle SQL, tworząc raporty na potrzeby klientów wewnętrznych.<br />
    Długoletnie doświadczenie w działach takich jak księgowość, audyt wewnętrzny i kontroling jest niezwykle przydatne w mojej nowej roli, ponieważ pomaga mi sprawnie określić potrzeby użytkownika biznesowego, zrozumieć temat raportów oraz efektywnie się komunikować.<br />
    Przygotowując się do przebranżowienia, samodzielnie nauczyłem się programowania w SQL. Obecnie rozwijam się w językach Python oraz Go. Moje dotychczasowe życie zawodowe nauczyło mnie pracy w dużej organizacji, odpowiedniego zarządzania czasem, pilnowania terminów oraz wzmocniło zdolności analityczne. Umiejętność pracy w zespole przejawia się w zarządzaniu różnej wielkości strukturami – od jednego do dziewięciu pracowników – klarownej komunikacji, przekazywaniu wiedzy oraz dzieleniu się spostrzeżeniami mającymi wpływ na usprawnienie działalności. Praktyczne umiejętności finansowe poparłem wiedzą zdobywaną w trakcie studiów ACCA. Jestem otwarty na naukę nowych języków programowania.
    """
    return Paragraph(profile_text, styles['PolishBodyText'])

def get_experience1_text(styles):
    experience1_text = """
    Moje doświadczenie w banku obejmuje tworzenie raportów, analizowanie danych oraz wsparcie zespołów finansowych...
    """
    return Paragraph(experience1_text, styles['PolishBodyText'])

def get_experience2_text(styles):
    experience2_text = """
    Moje doświadczenie w doradztwie finansowym to wsparcie klientów w zakresie optymalizacji kosztów i zarządzania ryzykiem...
    """
    return Paragraph(experience2_text, styles['PolishBodyText'])
