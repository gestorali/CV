# sections/profil_section.py

from reportlab.platypus import Paragraph, Spacer,ListFlowable, ListItem, Flowable

def get_profile_text(styles):
    paragraphs = [
    "Doświadczony analityk danych z ponad 20-letnim doświadczeniem w sektorze finansowym (księgowość, audyt wewnętrzny, controlling) oraz 3-letnim stażem we wdrażaniu rozwiązań analitycznych w IT. Specjalizuję się w analizie danych, posługując się zaawansowanym SQL (Oracle, BigQuery, Spark) oraz narzędziami Business Intelligence (Power BI).", 
    "Moje kluczowe kompetencje obejmują: zbieranie i analizę wymagań biznesowych, projektowanie i tworzenie efektywnych raportów, zarządzanie projektami oraz zespołami (do 9 osób).",
    "Bogate doświadczenie w sektorze finansowym umożliwia mi szybkie zrozumienie potrzeb biznesowych i efektywną komunikację z interesariuszami. Obecnie rozwijam swoje umiejętności w języku Golang i zastosowaniach Pythona w Machine Learning. Posiadam certyfikat ACCA, który potwierdza moje kompetencje w obszarze finansów. Jestem osobą zaangażowaną, skuteczną i skupioną na osiąganiu celów."
    ]
    # Tworzenie listy akapitów z minimalnym odstępem
    content = []
    for para in paragraphs:
        content.append(Paragraph(para, styles['PolishBodyText']))
        content.append(Spacer(1, 6))  # Dodanie minimalnego odstępu między akapitami

    return content

class InlineText(Flowable):
    def __init__(self, left_text, left_style, right_text, right_style):
        super().__init__()
        self.left_text = Paragraph(left_text, left_style)
        self.right_text = Paragraph(right_text, right_style)

    def wrap(self, available_width, available_height):
        # Oblicza szerokość i wysokość elementu
        self.width = available_width * 0.8
        self.height = max(
            self.left_text.wrap(available_width, available_height)[1],
            self.right_text.wrap(available_width, available_height)[1],
        )
        return self.width, self.height

    def draw(self):
        # Rysowanie lewej i prawej części tekstu
        canvas = self.canv
        left_width, left_height = self.left_text.wrap(self.width, self.height)
        self.left_text.drawOn(canvas, 0, 0)

        right_width, right_height = self.right_text.wrap(self.width - left_width, self.height)
        self.right_text.drawOn(canvas, left_width, 0)

def get_experience1_text(styles):

    company = """Bank Polskiej Spółdzielczości S.A."""


    # Użycie InlineText dla dwóch fragmentów tekstu
    inline_text = InlineText(
        left_text="Analityk danych", 
        left_style=styles['PolishBodyTextBold'],
        right_text="4/2024 – obecnie",
        right_style=styles['PolishBodyText']
    )

    content = []
    content.append(Paragraph(company, styles['PolishBodyText']))
    content.append(inline_text)

    # Punkty do listy
    bullet_points = [
        "Tworzenie i optymalizacja raportów finansowych z wykorzystaniem SQL (Oracle).",
        "Przegląd i aktualizacja procedur."
    ]

    # Tworzenie listy punktowanej
    bullet_list = ListFlowable(
        [
            ListItem(Paragraph(point, styles['BulletStyle']), bulletText="•")
            for point in bullet_points
        ],
        bulletFontName='DejaVuSans',  # Czcionka dla symboli
        bulletFontSize=9,            # Rozmiar symboli
        bulletType='bullet'          # Typ listy: punktowana
    )
    content.append(bullet_list)  # Dodanie listy punktowanej do zawartości

    return content

def get_experience2_text(styles):

    company = """Cogit Sp. z o.o."""


    # Użycie InlineText dla dwóch fragmentów tekstu
    inline_text = InlineText(
        left_text="Konsultant", 
        left_style=styles['PolishBodyTextBold'],
        right_text="3/2022 – 3/2024",
        right_style=styles['PolishBodyText']
    )

    content = []
    content.append(Paragraph(company, styles['PolishBodyText']))
    content.append(inline_text)

    # Punkty do listy
    bullet_points = [
        "Budowa i wizualizacja raportów finansowych w Power BI.",
        "Przetwarzanie dużych zbiorów danych za pomocą Spark SQL i BigQuery.",
        "Integracja danych w środowiskach Google Cloud Platform.",
        "Automatyzacja procesów ETL przy użyciu Apache Airflow."
    ]

    # Tworzenie listy punktowanej
    bullet_list = ListFlowable(
        [
            ListItem(Paragraph(point, styles['BulletStyle']), bulletText="•")
            for point in bullet_points
        ],
        bulletFontName='DejaVuSans',  # Czcionka dla symboli
        bulletFontSize=9,            # Rozmiar symboli
        bulletType='bullet'          # Typ listy: punktowana
    )
    content.append(bullet_list)  # Dodanie listy punktowanej do zawartości

    return content

def get_experience3_text(styles):

    company = """Carrefour Polska Sp. z o.o."""


    # Użycie InlineText dla dwóch fragmentów tekstu
    inline_text = InlineText(
        left_text="Kontroler galerii handlowych i inwestycji", 
        left_style=styles['PolishBodyTextBold'],
        right_text="7/2017 – 5/2021",
        right_style=styles['PolishBodyText']
    )

    content = []
    content.append(Paragraph(company, styles['PolishBodyText']))
    content.append(inline_text)

    # Punkty do listy
    bullet_points = [
        "Budżetowanie przychodów i kosztów galerii handlowych oraz nadzór nad wydatkami inwestycyjnymi.",
        "Analiza rentowności projektów inwestycyjnych (ROI).",
        "Zarządzanie pracą zespołu (1 osoba)."
    ]

    # Tworzenie listy punktowanej
    bullet_list = ListFlowable(
        [
            ListItem(Paragraph(point, styles['BulletStyle']), bulletText="•")
            for point in bullet_points
        ],
        bulletFontName='DejaVuSans',  # Czcionka dla symboli
        bulletFontSize=9,            # Rozmiar symboli
        bulletType='bullet'          # Typ listy: punktowana
    )
    content.append(bullet_list)  # Dodanie listy punktowanej do zawartości

    return content

def get_experience4_text(styles):

    company = """Carrefour Polska Sp. z o.o."""


    # Użycie InlineText dla dwóch fragmentów tekstu
    inline_text = InlineText(
        left_text="Menedżer kontroli wewnętrznej", 
        left_style=styles['PolishBodyTextBold'],
        right_text="1/2015 – 6/2017",
        right_style=styles['PolishBodyText']
    )

    content = []
    #content.append(Paragraph(company, styles['PolishBodyText']))
    content.append(inline_text)

    # Punkty do listy
    bullet_points = [
        "Audyt procesów biznesowych i identyfikacja obszarów do poprawy.",
        "Opracowywanie i wdrażanie nowych procedur oraz standardów kontroli."
    ]

    # Tworzenie listy punktowanej
    bullet_list = ListFlowable(
        [
            ListItem(Paragraph(point, styles['BulletStyle']), bulletText="•")
            for point in bullet_points
        ],
        bulletFontName='DejaVuSans',  # Czcionka dla symboli
        bulletFontSize=9,            # Rozmiar symboli
        bulletType='bullet'          # Typ listy: punktowana
    )
    content.append(bullet_list)  # Dodanie listy punktowanej do zawartości

    return content

def get_experience5_text(styles):

    company = """Carrefour Polska Sp. z o.o."""


    # Użycie InlineText dla dwóch fragmentów tekstu
    inline_text = InlineText(
        left_text="Menedżer ds. środków trwałych", 
        left_style=styles['PolishBodyTextBold'],
        right_text="4/2012 – 12/2014",
        right_style=styles['PolishBodyText']
    )

    content = []
    #content.append(Paragraph(company, styles['PolishBodyText']))
    content.append(inline_text)

    # Punkty do listy
    bullet_points = [
        "Zarządzanie 9-osobowym zespołem księgowym.",
        "Organizacja i wdrożenie procesu inwentaryzacji środków trwałych."
    ]

    # Tworzenie listy punktowanej
    bullet_list = ListFlowable(
        [
            ListItem(Paragraph(point, styles['BulletStyle']), bulletText="•")
            for point in bullet_points
        ],
        bulletFontName='DejaVuSans',  # Czcionka dla symboli
        bulletFontSize=9,            # Rozmiar symboli
        bulletType='bullet'          # Typ listy: punktowana
    )
    content.append(bullet_list)  # Dodanie listy punktowanej do zawartości

    return content

def get_experience6_text(styles):

    company = """Carrefour Polska Sp. z o.o."""


    # Użycie InlineText dla dwóch fragmentów tekstu
    inline_text = InlineText(
        left_text="Kontroler procesów finansowych", 
        left_style=styles['PolishBodyTextBold'],
        right_text="1/2011 – 3/2012",
        right_style=styles['PolishBodyText']
    )

    content = []
    #content.append(Paragraph(company, styles['PolishBodyText']))
    content.append(inline_text)

    # Punkty do listy
    bullet_points = [
        "Opracowanie polityki rachunkowości.",
        "Przygotowanie dokumentacji procesów biznesowych i wdrażanie procedur księgowych."
    ]

    # Tworzenie listy punktowanej
    bullet_list = ListFlowable(
        [
            ListItem(Paragraph(point, styles['BulletStyle']), bulletText="•")
            for point in bullet_points
        ],
        bulletFontName='DejaVuSans',  # Czcionka dla symboli
        bulletFontSize=9,            # Rozmiar symboli
        bulletType='bullet'          # Typ listy: punktowana
    )
    content.append(bullet_list)  # Dodanie listy punktowanej do zawartości

    return content

def get_experience7_text(styles):

    company = """Carrefour Polska Sp. z o.o."""


    # Użycie InlineText dla dwóch fragmentów tekstu
    inline_text = InlineText(
        left_text="Menedżer w dziale podatków", 
        left_style=styles['PolishBodyTextBold'],
        right_text="1/2009 – 12/2010",
        right_style=styles['PolishBodyText']
    )

    content = []
    #content.append(Paragraph(company, styles['PolishBodyText']))
    content.append(inline_text)

    # Punkty do listy
    bullet_points = [
        "Współpraca z doradcą podatkowym nad procesem liczenia podatku CIT.",
        "Szacowanie podatku odroczonego."
    ]

    # Tworzenie listy punktowanej
    bullet_list = ListFlowable(
        [
            ListItem(Paragraph(point, styles['BulletStyle']), bulletText="•")
            for point in bullet_points
        ],
        bulletFontName='DejaVuSans',  # Czcionka dla symboli
        bulletFontSize=9,            # Rozmiar symboli
        bulletType='bullet'          # Typ listy: punktowana
    )
    content.append(bullet_list)  # Dodanie listy punktowanej do zawartości

    return content

def get_experience8_text(styles):

    company = """Carrefour Polska Sp. z o.o."""


    # Użycie InlineText dla dwóch fragmentów tekstu
    inline_text = InlineText(
        left_text="Menedżer konsolidacji", 
        left_style=styles['PolishBodyTextBold'],
        right_text="1/2001 – 12/2008",
        right_style=styles['PolishBodyText']
    )

    content = []
    #content.append(Paragraph(company, styles['PolishBodyText']))
    content.append(inline_text)

    # Punkty do listy
    bullet_points = [
        "Przygotowywanie sprawozdawczości finansowej zgodnej ze standardami MSSF.",
        "Testowanie utraty wartości aktywów i analiza umów najmu zgodnie z MSR 16.",
        "Zarządzanie 2-osobowym zespołem."
    ]

    # Tworzenie listy punktowanej
    bullet_list = ListFlowable(
        [
            ListItem(Paragraph(point, styles['BulletStyle']), bulletText="•")
            for point in bullet_points
        ],
        bulletFontName='DejaVuSans',  # Czcionka dla symboli
        bulletFontSize=9,            # Rozmiar symboli
        bulletType='bullet'          # Typ listy: punktowana
    )
    content.append(bullet_list)  # Dodanie listy punktowanej do zawartości

    return content

def get_experience9_text(styles):

    company = """Globi Sp. z o.o."""


    # Użycie InlineText dla dwóch fragmentów tekstu
    inline_text = InlineText(
        left_text="Kontroler finansowy", 
        left_style=styles['PolishBodyTextBold'],
        right_text="12/1999 – 12/2000",
        right_style=styles['PolishBodyText']
    )

    content = []
    content.append(Paragraph(company, styles['PolishBodyText']))
    content.append(inline_text)

    # Punkty do listy
    bullet_points = [
        "Budżetowanie kosztów, analiza NPV oraz przygotowywanie raportów finansowych."
    ]

    # Tworzenie listy punktowanej
    bullet_list = ListFlowable(
        [
            ListItem(Paragraph(point, styles['BulletStyle']), bulletText="•")
            for point in bullet_points
        ],
        bulletFontName='DejaVuSans',  # Czcionka dla symboli
        bulletFontSize=9,            # Rozmiar symboli
        bulletType='bullet'          # Typ listy: punktowana
    )
    content.append(bullet_list)  # Dodanie listy punktowanej do zawartości

    return content