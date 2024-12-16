from datetime import datetime
from src import constants

def speed2numcat(speed: float) -> int:
    """Convert wind speed in knots to numerical cyclone category using
    South-West Indian Ocean cyclone scale.

    Numerical categories are:
    - 0: TDist (Tropical Disturbance)
    - 1: TD (Tropical Depression)
    - 2: MTS (Moderate Tropical Storm)
    - 3: STS (Severe Tropical Storm)
    - 4: TC (Tropical Cyclone)
    - 5: ITC (Intense Tropical Cyclone)
    - 6: VITC (Very Intense Tropical Cyclone)


    Parameters
    ----------
    speed: float
        wind speed in knots

    Returns
    -------
    int
        numerical cyclone category

    """
    if speed < 0:
        raise ValueError("Wind speed must be positive")
    elif speed < 28:
        return 0
    elif speed < 34:
        return 1
    elif speed < 48:
        return 2
    elif speed < 64:
        return 3
    elif speed < 90:
        return 4
    elif speed < 116:
        return 5
    else:
        return 6
    
# Define storm categories in order of intensity
category_order = {
    "Tropical Disturbance": 1,
    "Tropical Depression": 2,
    "Tropical Storm": 3,
    "Severe Tropical Storm": 4,
    "Tropical Cyclone": 5,
    "Intense Tropical Cyclone": 6,
    "Very Intense Tropical Cyclone": 7,
}

def categorize_cyclone(wind_speed):
    if wind_speed > 115:
        return "Very Intense Tropical Cyclone"
    elif wind_speed >= 90:
        return "Intense Tropical Cyclone"
    elif wind_speed >= 64:
        return "Tropical Cyclone"
    elif wind_speed >= 48:
        return "Severe Tropical Storm"
    elif wind_speed >= 34:
        return "Moderate Tropical Storm"
    elif wind_speed >= 28:
        return "Tropical Depression"
    else:
        return "Tropical Disturbance"
    
def calculate_storm_return_period(
    df, wind_speed_kmh_min, wind_speed_kmh_max, start_year
):
    # Convert the given speed from km/h to knots
    min_speed_knots = wind_speed_kmh_min * constants.kmh_to_knots
    max_speed_knots = wind_speed_kmh_max * constants.kmh_to_knots

    # Extract the year from the 'ISO_TIME' column
    df["year"] = df["ISO_TIME"].apply(
        lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S").year
    )

    # Filter the DataFrame for records from the start year and with wind speed above the threshold
    df_filtered = df[
        (df["year"] >= start_year)
        & (df["REU_WIND"] >= min_speed_knots)
        & (df["REU_WIND"] <= max_speed_knots)
    ]

    # Count unique storms
    unique_storms = df_filtered["NAME"].nunique()
    unique_seasons = df_filtered["Season"].nunique()

    # Calculate the total number of years in the filtered DataFrame
    yr_len = 2024 - start_year + 1

    # Calculate the combined return period
    combined_return_period = yr_len / unique_seasons

    print(
        f"The combined return period of storms over {wind_speed_kmh_min}km/h is 1-in-{round(combined_return_period, 1)} years."
    )

def classify_scenario(deplacees_sum):
    if 1000 <= deplacees_sum <= 10000:
        return "Scenario 1"
    elif 10000 < deplacees_sum <= 25000:
        return "Scenario 2"
    elif deplacees_sum > 25000:
        return "Scenario 3"
    else:
        return "No Scenario"

