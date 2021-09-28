from covid import Covid
A=Covid()
print(A.get_data())
for j in range(1,10000):
    act=A.get_total_active_cases()
    rec=A.get_total_recovered()
    death=A.get_total_deaths()
    con=A.get_total_confirmed_cases()
    print("1.GLOBAL COUNT")
    print("2.ACTIVE CASES")
    print("3.CONFIRMED CASES")
    print("4.RECORVED CASES")
    print("5.DECREAsED CASES")
    print("6.Get Covid Update By country Names")
    print("----------------------------------------------------")
    x=input("enter your choice:")
    if x=='1':
        print("ACTIVE CASES:",act,"\nCONFIRMED CASES:",con,"\nRECOVERED CASES:",rec,"\nDECREASED CASES:",death)
    elif x=='2':
        print("ACTIVE CASES:",act)
    elif x=='3':
        print("CONFIRMED CASES:",con)
    elif x=='4':
        print("RECORVED CASES:",rec)
    elif x=='5':
        print("DECREASED CASES:",death)
    elif x=='6':
        y=input("enter country name:")
        C=A.get_status_by_country_name(y)
        print(C)
    else:
        print("invalid input")
        break
        


