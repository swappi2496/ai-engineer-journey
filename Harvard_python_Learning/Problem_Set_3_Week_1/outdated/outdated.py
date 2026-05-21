months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December",
]

while True:
    try:
        date = input("Date: ").strip()

        if "/" in date:
            month, day, year = date.split("/")
            month, day, year = int(month), int(day), int(year)

        elif "," in date:
            month_name, rest = date.split(" ", 1)
            day, year = rest.split(",")
            day, year = int(day), int(year)
            if month_name not in months:
                continue
            month = months.index(month_name) + 1

        else:
            continue

        if 1 <= month <=12 and 1 <= day <= 31:
            print(f"{year}-{month:02d}-{day:02d}")
            break
    except (ValueError, IndexError):
        continue
