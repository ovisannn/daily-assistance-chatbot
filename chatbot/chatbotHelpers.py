from datetime import datetime, date
import string


def GetHours():
    return datetime.today()

def GetDay():
    return datetime.now().strftime("%A")

def GetNoesaAge():
    built = date(2022, 8, 1)
    now = date.today()
    delta = now - built
    totalDays =delta.days
    months = int(totalDays/30)%12
    years = int(totalDays/365)
    days = totalDays%30
    
    if months ==0 and years == 0:
        return('%s hari'%(days))
    elif years == 0:
        return('%s hari %s bulan'%(days, months))
    else:
        return('%s hari %s bulan dan %s tahun'%(days, months, years))


# if __name__ == '__main__':
#     # now = datetime.now()
#     # print(now.strftime("%A"))
#     print(GetNoesaAge())
#     # print(37)