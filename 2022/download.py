from aocd import get_data
import datetime

DAY = datetime.date.today().day
YEAR = 2022
FILENAME = f"Day{DAY}/{DAY}.txt"

data = get_data(day=DAY, year=YEAR)

with open(FILENAME, "w", encoding="utf8") as f:
	f.write(data)
