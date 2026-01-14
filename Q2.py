import pandas as pd
import glob
import os

# defining month groups for Australian seasons
SEASONS = {
    "Summer": ["December", "January", "February"],
    "Autumn": ["March", "April", "May"],
    "Winter": ["June", "July", "August"],
    "Spring": ["September", "October", "November"],
}
# defining month columns
MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

# loading and combining all files
all_files = glob.glob(
    os.path.join(
        "/Users/sumitmanandhar/Desktop/SYD06 - ASSIGNMENT1/Assignment 2/temperatures",
        "*.csv",
    )
)
df_list = []
for f in all_files:
    temp_df = pd.read_csv(f)
    df_list.append(temp_df)
df = pd.concat(df_list, ignore_index=True)

# Convert month columns to numeric
for month in MONTHS:
    df[month] = pd.to_numeric(df[month])

# 1). SEASON AVERAGES

# We calculate the mean of all values in the columns for each season by stacking the values for the months in that season
season_results = {}
for season, month_s in SEASONS.items():
    season_results[season] = df[month_s].stack().mean()

# writing the results to file and printing for verification
with open("average_temp.txt", "w") as f:
    for season in ["Summer", "Autumn", "Winter", "Spring"]:
        f.write(f"{season}: {season_results[season]}°C\n")
        print(f"{season}: {season_results[season]}°C\n")


# 2). LARGEST TEMPERATURE RANGE

# Get max and min for each station across all months
# axis=1 means we calculate row-wise
df["row_max"] = df[MONTHS].max(axis=1)
df["row_min"] = df[MONTHS].min(axis=1)

# grouping by station name to find the max and min temperature ever recorded for each station
station_groups = df.groupby("STATION_NAME")
temp_max = station_groups["row_max"].max()
temp_min = station_groups["row_min"].min()

# calculating the temperature range for each station
range_temp = temp_max - temp_min

# finding the maximum range value and the stations that have this range
max_range = range_temp.max()
max_range_stations = range_temp[range_temp == max_range].index

# writing the results to file and printing for verification
with open("largest_temp_range_station.txt", "w") as f:
    for station in max_range_stations:
        f.write(
            f"Station ::{station}:--- Range:{max_range}°C "
            f"(Max: {temp_max[station]}°C, Min: {temp_min[station]}°C)\n"
        )
        print(
            f"Station ::{station}:--- Range:{max_range}°C "
            f"(Max: {temp_max[station]}°C, Min: {temp_min[station]}°C)\n"
        )


# 3). STATION TEMPERATURE STABILITY

# we melt the data so all temperatures for a station are in one series
# melt : Unpivot a DataFrame from wide to long format, optionally leaving identifiers set
melted = df.melt(id_vars=["STATION_NAME"], value_vars=MONTHS)
# calculating standard deviation for each grouped station across all its recorded months
deviation = melted.groupby("STATION_NAME")["value"].std()

# finding the minimum and maximum standard deviation values
min_deviation = deviation.min()
max_deviation = deviation.max()

# writing the results to file and printing for verification
with open("temperature_stability_stations.txt", "w") as f:
    for station in deviation[deviation == min_deviation].index:
        f.write(f"Most Stable: Station {station}: StdDev {min_deviation}°C\n")
        print(f"Most Stable: Station {station}: StdDev {min_deviation}°C\n")
    for station in deviation[deviation == max_deviation].index:
        f.write(f"Most Variable: Station {station}: StdDev {max_deviation}°C\n")
        print(f"Most Variable: Station {station}: StdDev {max_deviation}°C\n")
