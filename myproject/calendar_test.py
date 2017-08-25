import calendar

months=[]
days=[]

for i in range(1,13):
  months.append(calendar.month_name[i])

  for j in range(1,7):
        days.append(calendar.day_name[j])

print(months,days)
