import os
KNOTS2MS = 0.514444
kmh_to_knots = 0.5399568 # Conversion factor from km/h to knots
THRESHOLD_SPEED_OPT1 = 118
THRESHOLD_SPEED_OPT2 = 166
buffer = 100 #in km
mdg_epsg = 29702 # for buffer conversion
minute_to_10_minute_conversion_factor = 0.88 # converting 1-minute wind speeds to 10-minute
ADMS = [
    "Diana",
    "Sava",
    "Sofia",
    "Boeny",
    "Analanjirofo",
    "Ambatosoa",
    "Alaotra Mangoro",
    "Atsinanana",
    "Vatovavy Fitovinany",
    "Atsimo Atsinanana",
]
AA_DATA_DIR = os.getenv("AA_DATA_DIR")
AA_DATA_DIR_NEW = os.getenv("AA_DATA_DIR_NEW")