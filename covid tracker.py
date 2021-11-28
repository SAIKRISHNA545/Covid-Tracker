from covid import Covid

covid = Covid()
print("1.Conformed cases 2.Active cases 3.Recover count")
x=int(input("enter your choice:"))
if x==1:
    confirmed = covid.get_total_confirmed_cases()
    print('Confirmed :', end =" ")
    print(confirmed)
elif x==2:
    active = covid.get_total_active_cases()
    print("Active:", end=" ")
    print(active)
elif x==3:
    recovered = covid.get_total_recovered()
    print('Recovered:', end =" ")
    print(recovered)
else:
    deaths = covid.get_total_deaths()
    print('Deaths:', end =" ")
    print(deaths)
