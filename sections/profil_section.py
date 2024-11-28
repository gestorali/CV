# sections/profil_section.py

from reportlab.platypus import Paragraph, Spacer,ListFlowable, ListItem, Flowable

def get_profile_text(styles):
    paragraphs = [
    "Analityk danych z ponad 20-letnim doświadczeniem w finansach oraz 3-letnim w IT. Specjalizuję się w tworzeniu raportów i analiz danych przy wykorzystaniu Power BI oraz zapytań SQL do baz danych. Mam doświadczenie w pracy z danymi przechowywanymi na platformach takich jak Google Cloud Platform i Azure Databricks. Łączę dogłębną wiedzę finansową z umiejętnościami analitycznymi i technologicznymi, by dostarczać efektywne rozwiązania wspierające cele biznesowe.", 
    "Prywatnie rozwijam swoje umiejętności w Pythonie, szczególnie w zakresie analizy danych z wykorzystaniem bibliotek takich jak Pandas i NumPy, a także w obszarze uczenia maszynowego (machine learning). Eksperymentuję z modelami uczenia nadzorowanego i niesuperwizyjnego, wykorzystując narzędzia takie jak scikit-learn i TensorFlow. Jestem otwarty na naukę nowych technologii i ich praktyczne zastosowanie."
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
        "Tworzenie raportów w Oracle SQL dla klientów wewnętrznych oraz na potrzeby nadzoru bankowego.",
        "Optymalizacja procesów przetwarzania danych."
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
        "Przygotowywanie raportów finansowych w Power BI.",
        "Przetwarzanie danych w SQL oraz Power Query, integracja z Google Cloud Platform i Azure Databricks.",
        "Tworzenie prostych DAG-ów w Airflow do automatyzacji procesów danych w GCP."
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
        "Odpowiedzialność za budżetowanie przychodów, kosztów oraz kontrolę realizacji wydatków inwestycyjnych.",
        "Przeprowadzanie analiz ROI dla projektów inwestycyjnych."
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
        "Przeprowadzanie audytów procesów biznesowych.",
        "Aktualizacja procedur wewnętrznych oraz wdrożenie nowych standardów kontroli."
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
        "Zarządzanie 9-osobowym zespołem księgowym, raportowanie związane ze środkami trwałymi.",
        "Wdrożenie procesu inwentaryzacji środków trwałych po kilkuletniej przerwie."
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
        "Tworzenie opisów procesów wewnętrznych oraz wdrażanie procedur księgowych."
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
        "Współpraca z doradcami podatkowymi w celu optymalizacji podatkowej i wdrożenia nowych procedur.",
        "Szacowanie podatku odroczonego oraz składanie deklaracji podatkowych."
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
        "Raportowanie finansowe, wdrażanie standardów IFRS.",
        "Testowanie utraty wartości aktywów oraz analiza umów najmu pod kątem IFRS 16.",
        "zarządzanie 2- osobowym zespołem."
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
        "Budżetowanie kosztów, analiza NPV, raportowanie finansowe."
        
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