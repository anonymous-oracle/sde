dates = ["2026-6-10", "2025-11-22", "2026-2-31"]

for date in dates:
    year, month, day = date.split("-")
    print(f"{int(day):02d}/{int(month):02d}/{int(year):02d}")
    if int(year) == 2025:
        print(f"found: {year}")
        break
else:
    print("no 2025")    
