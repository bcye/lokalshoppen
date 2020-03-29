from api.models import Category

KATEGORIEN_CHOICES = [
    ("LEB", "Lebensmittel"),
    ("BAE", "Bäckerei"),
    ("FLE", "Fleischerei"),
    ("GET", "Getränke"),
    ("DRO", "Drogerie"),
    ("ELE", "Elektronik"),
    ("HWO", "Haushalt & Wohnen"),
    ("WEB", "Werkeln & Basteln"),
    ("SPO", "Sport"),
    ("UNT", "Unterhaltung"),
    ("MOD", "Mode"),
    ("APO", "Apotheke"),
    ("KIO", "Zeitungen & Kiosk"),
    ("BUe", "Bücher"),
    ("TIE", "Tierbedarf"),
    ("BLU", "Blumenladen"),
    ("OUT", "Outdoor"),
    ("SON", "Sonstiges"),
    ("RAU", "Raucherbedarf"),
    ("SPI", "Spielwaren"),
    ("SCH", "Schuhe"),
]

def import_old_cats():
    for slug, name in KATEGORIEN_CHOICES:
        Category.objects.get_or_create(slug=slug, name=name)


