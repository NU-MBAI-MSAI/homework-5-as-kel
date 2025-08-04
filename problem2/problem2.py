def date_format(my_date):
    year = my_date[-4:]
    day = my_date[3:5]
    month = my_date[0:2]
    return year + "-" + month + "-" + day