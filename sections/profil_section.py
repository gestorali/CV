# sections/profil_section.py

from reportlab.platypus import Paragraph, Spacer,ListFlowable, ListItem, Flowable

def get_profile_text(styles):
    paragraphs = [
    "Po dwudziestu latach pracy w różnych działach finansowych zmieniłem profil działalności na obszar IT. Jako konsultant współpracowałem z działami finansowymi klientów i tworzyłem dla nich raporty w Power BI. Dane, przechowywane w chmurze – Google Cloud Platform lub Azure Databricks – przygotowywałem głównie w SQL, a czasami w Power Query. Obecnie pracuję jako analityk danych w banku, gdzie korzystam z Oracle SQL, tworząc raporty na potrzeby klientów wewnętrznych.",
    "Długoletnie doświadczenie w działach takich jak księgowość, audyt wewnętrzny i kontroling jest niezwykle przydatne w mojej nowej roli, ponieważ pomaga mi sprawnie określić potrzeby użytkownika biznesowego, zrozumieć temat raportów oraz efektywnie się komunikować.",
    "Przygotowując się do przebranżowienia, samodzielnie nauczyłem się programowania w SQL. Obecnie rozwijam się w językach Python oraz Go. Moje dotychczasowe życie zawodowe nauczyło mnie pracy w dużej organizacji, odpowiedniego zarządzania czasem, pilnowania terminów oraz wzmocniło zdolności analityczne. Umiejętność pracy w zespole przejawia się w zarządzaniu różnej wielkości strukturami – od jednego do dziewięciu pracowników – klarownej komunikacji, przekazywaniu wiedzy oraz dzieleniu się spostrzeżeniami mającymi wpływ na usprawnienie działalności. Praktyczne umiejętności finansowe poparłem wiedzą zdobywaną w trakcie studiów ACCA. Jestem otwarty na naukę nowych języków programowania."
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

    # Użycie InlineText dla dwóch fragmentów tekstu
    inline_text = InlineText(
        left_text="Analityk danych", 
        left_style=styles['PolishBodyTextBold'],
        right_text="od 4/2024 – obecnie",
        right_style=styles['PolishBodyText']
    )

    content = []
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
    experience2_text = """
    Moje doświadczenie w doradztwie finansowym to wsparcie klientów w zakresie optymalizacji kosztów i zarządzania ryzykiem...
    """
    return Paragraph(experience2_text, styles['PolishBodyText'])
