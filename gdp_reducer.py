import sys

current_year = None
total_gdp = 0
count = 0

# Read input from Mapper
for line in sys.stdin:
    line = line.strip()
    year, gdp = line.split("\t")

    try:
        gdp_value = float(gdp)
    except ValueError:
        continue  # Ignore invalid data

    # Aggregating values
    if current_year == year:
        total_gdp += gdp_value
        count += 1
    else:
        if current_year:
            # Print average GDP for previous year
            print(f"{current_year}\t{total_gdp / count}")

        current_year = year
        total_gdp = gdp_value
        count = 1

# Print last year’s result
if current_year:
    print(f"{current_year}\t{total_gdp / count}")