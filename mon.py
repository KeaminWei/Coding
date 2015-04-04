mon = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "sep",
    "oct",
    "nov",
    "dec",
]
endings = ['st', 'nd', 'rd'] + 17 * ['th'] + \
    ['st', 'nd', 'rd'] + 7 * ['th'] + ['st']
year = raw_input('year:')
month = raw_input('month:')
day = raw_input('day:')
month_num = int(month)
day_num = int(day)
month_name = mon[month_num - 1]
ordinal = day + endings[day_num - 1]
print month_name + ' ' + ordinal + ' ' + year
