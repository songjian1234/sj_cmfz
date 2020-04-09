import datetime

d = datetime.datetime.now()


def day_get(d): # 通过for 循环得到天数，如果想得到两周的时间，只需要把8改成15就可以了。
    for i in range(1, 8):
        oneday = datetime.timedelta(days=i)
        day = d - oneday
        date_to = datetime.datetime(day.year, day.month, day.day)
        yield str(date_to)[:10]

qq = day_get(d)

list = []
for obj in qq:
    list.append(obj)
list_week_day = list[::-1]
print (list_week_day)
