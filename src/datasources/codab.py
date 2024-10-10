import os
from pathlib import Path

import geopandas as gpd
from dotenv import load_dotenv

load_dotenv()
AA_DATA_DIR = os.getenv("AA_DATA_DIR")
ADMS = []

def load_codab(admin_level: int = 0):
    if not admin_level == 0:
        raise ValueError("Only admin level 0 is supported")
    adm1_path = (
        Path(AA_DATA_DIR)
        / "public"
        / "raw"
        / "mdg"
        / "cod_ab"
        / "mdg_admbnda_adm0_BNGRC_OCHA_20181031.shp"
    )
    gdf = gpd.read_file(adm1_path)
    return gdf
