import os
from pathlib import Path

import geopandas as gpd
from dotenv import load_dotenv

load_dotenv()
AA_DATA_DIR = os.getenv("AA_DATA_DIR")
ADMS = []

def load_codab(admin_level: int = 0):
    if not admin_level in [0, 1, 2]:
        raise ValueError("Only admin level 0, 1 and 2 is supported")
    adm_path = (
        Path(AA_DATA_DIR)
        / "public"
        / "raw"
        / "mdg"
        / "cod_ab"
        / f"mdg_admbnda_adm{admin_level}_BNGRC_OCHA_20181031.shp"
    )
    gdf = gpd.read_file(adm_path)
    return gdf
