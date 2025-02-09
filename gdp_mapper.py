import sys

# Read input line by line
for line in sys.stdin:
    line = line.strip()
    parts = line.split(",")

    # Extract columns (assuming CSV structure: year, rank, country, state, gdp, gdp_percent)
    if len(parts) >= 5:
        year = parts[0]
        gdp = parts[4]

        # Skip header row
        if year != "year":
            try:
                gdp_value = float(gdp)
                print(f"{year}\t{gdp_value}")
            except ValueError:
                pass  # Ignore invalid data
