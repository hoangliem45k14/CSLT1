print("Price".ljust(10)+"Discount".ljust(13)+"Final Price")
for i in range(4,25,5):
    Dis=0.6*(i+0.95)
    D=str(round(Dis,2))
    New=i+0.95-Dis
    N=str(round(New,2))
    j=str(i+0.95)
    print(j.ljust(11)+D.ljust(13)+N)