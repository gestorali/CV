# sections/profil_section.py

from reportlab.platypus import Paragraph, Spacer,ListFlowable, ListItem, Flowable

def get_profile_text(styles):
    paragraphs = [
    "Experienced Data Analyst with over 20 years of expertise in the financial sector (accounting, internal audit, controlling) and 3 years of experience implementing analytical solutions in IT. I specialize in data analysis, leveraging advanced SQL (Oracle, BigQuery, Spark) and Business Intelligence tools like Power BI.", 
    "My key competencies include: gathering and analyzing business requirements, designing and creating efficient reports, managing projects and leading teams (up to 9 people).",
    "Extensive experience in the financial sector enables me to quickly understand business needs and communicate effectively with stakeholders. Currently, I am expanding my skills in Golang and Python applications for Machine Learning. I hold an ACCA certificate, which confirms my expertise in finance. I am a dedicated, results-oriented professional with strong analytical skills and the ability to work both independently and within a team."
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
        left_text="Data Analyst", 
        left_style=styles['PolishBodyTextBold'],
        right_text="4/2024 – present",
        right_style=styles['PolishBodyText']
    )

    content = []
    content.append(Paragraph(company, styles['PolishBodyText']))
    content.append(inline_text)

    # Punkty do listy
    bullet_points = [
        "Developing and optimizing financial reports using SQL (Oracle).",
        "Reviewing and updating  procedures."
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
        left_text="Data Consultant", 
        left_style=styles['PolishBodyTextBold'],
        right_text="3/2022 – 3/2024",
        right_style=styles['PolishBodyText']
    )

    content = []
    content.append(Paragraph(company, styles['PolishBodyText']))
    content.append(inline_text)

    # Punkty do listy
    bullet_points = [
        "Building and visualizing financial reports in Power BI.",
        "Processing large datasets using Spark SQL and BigQuery.",
        "Data integration in Google Cloud Platform and Azure Databricks.",
        "Automating ETL processes with Apache Airflow."
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
        left_text="Controller of Shopping Malls and Investments", 
        left_style=styles['PolishBodyTextBold'],
        right_text="7/2017 – 5/2021",
        right_style=styles['PolishBodyText']
    )

    content = []
    content.append(Paragraph(company, styles['PolishBodyText']))
    content.append(inline_text)

    # Punkty do listy
    bullet_points = [
        "Budgeting revenues and costs for shopping malls and overseeing investment expenses.",
        "Conducting ROI analyses for investment projects.",
        "Managing a team (1 person)."
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
        left_text="Internal Control Manager", 
        left_style=styles['PolishBodyTextBold'],
        right_text="1/2015 – 6/2017",
        right_style=styles['PolishBodyText']
    )

    content = []
    #content.append(Paragraph(company, styles['PolishBodyText']))
    content.append(inline_text)

    # Punkty do listy
    bullet_points = [
        "Auditing business processes and identifying areas for improvement.",
        "Developing and implementing new procedures and control standards."
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
        left_text="Fixed Assets Manager", 
        left_style=styles['PolishBodyTextBold'],
        right_text="4/2012 – 12/2014",
        right_style=styles['PolishBodyText']
    )

    content = []
    #content.append(Paragraph(company, styles['PolishBodyText']))
    content.append(inline_text)

    # Punkty do listy
    bullet_points = [
        "Managing a 9-person accounting team responsible for fixed asset records.",
        "Organizing and implementing the fixed asset inventory process."
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
        left_text="Financial Processes Controller", 
        left_style=styles['PolishBodyTextBold'],
        right_text="1/2011 – 3/2012",
        right_style=styles['PolishBodyText']
    )

    content = []
    #content.append(Paragraph(company, styles['PolishBodyText']))
    content.append(inline_text)

    # Punkty do listy
    bullet_points = [
        "Developing an accounting policy.",
        "Preparing business process documentation and implementing accounting procedures."
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
        left_text="Tax Department Manager", 
        left_style=styles['PolishBodyTextBold'],
        right_text="1/2009 – 12/2010",
        right_style=styles['PolishBodyText']
    )

    content = []
    #content.append(Paragraph(company, styles['PolishBodyText']))
    content.append(inline_text)

    # Punkty do listy
    bullet_points = [
        "Collaborating with a tax advisor to develop a new CIT calculation process.",
        "Estimating deferred tax.",
        "Managing a team (1 person)."
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
        left_text="Consolidation Manager", 
        left_style=styles['PolishBodyTextBold'],
        right_text="1/2001 – 12/2008",
        right_style=styles['PolishBodyText']
    )

    content = []
    #content.append(Paragraph(company, styles['PolishBodyText']))
    content.append(inline_text)

    # Punkty do listy
    bullet_points = [
        "Preparing financial reporting in compliance with IFRS standards",
        "Conducting asset impairment testing and lease agreement analysis under IAS 16.",
        "Managing a 2-person team."
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
        left_text="Financial Controller", 
        left_style=styles['PolishBodyTextBold'],
        right_text="12/1999 – 12/2000",
        right_style=styles['PolishBodyText']
    )

    content = []
    content.append(Paragraph(company, styles['PolishBodyText']))
    content.append(inline_text)

    # Punkty do listy
    bullet_points = [
        "Budgeting costs, analyzing NPV, and preparing financial reports."
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