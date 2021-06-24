def dayofyear():
    import datetime
    year = input('please input year')
    month = input('please input month')
    day = input('please input day')
    date1 = datetime.date(year=int(year), month=int(month), day=int(day))
    date2 = datetime.date(year=int(year), month=1, day=1)
    res = (date1 - date2).days + 1
    print(res)
    return res
if __name__ == '__main__':
    dayofyear()