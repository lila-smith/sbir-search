NUM_RESULTS = 200

print("Welcome to SBIR URL generator. Simply hit enter for any category you don't want to filter by.")
city = input("Which city? ")
zip = input("Which zip code? ")
state = input("Which state? ")
award_years = input("Which years for awards? (Enter comma separated list) ").split(",")
print(award_years)
years_str = ""
for year in award_years:
    years_str += f"&year%5B%5D={year}"
    print(years_str)

print("Web Link:")
print(f"    https://www.sbir.gov/sbirsearch/firm/all?firm=&duns=&city={city}&zip={zip}&state={state}{years_str}&page=1&per_page={NUM_RESULTS}")
print("XLSX Download:")
print(f"    https://www.sbir.gov/sbirsearch/firm/all?firm=&duns=&city={city}&zip={zip}&state={state}{years_str}&page=1&print=xls&per_page={NUM_RESULTS}")