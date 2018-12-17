import calendar

# Working...
def get_month():

    m = [] #Creating a list to store each month

    for month in range(1, 13):
        m.append(calendar.month_name[month].lower())

    return m


def get_year():

    year = []
    base_year = 2016

    while base_year < 2019:
        base_year += 1
        year.append(base_year)

    return year


def get_url():

    url = []

    for i in get_year():

        for m in get_month():
            url.append('NBA_' + str(i) + '_games-' + str(m) + '.html')

    return url


print(get_url())







