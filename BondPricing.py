print('This is a Financial Calculator by Vlad Vassilyev(my second program)\nFunction available are as follows\n\nbondprice(Yield_to_Maturity,Coupon_Payment,Years_to_Maturity,Coupons_per_Year)-to calculate the flat and full price of a bond')
print('\npv(Future_Value,Payments,Years_to_Maturity,Periods_per_Year,Required_ROR)- for calculating a present value of an investment')
file1=open("Results.txt","w")
file1.close
def bondprice(Yield_to_Maturity,Coupon_Payment,Years_to_Maturity,Coupons_per_Year):
    r=Yield_to_Maturity            
    c=Coupon_Payment
    n=Years_to_Maturity
    py=Coupons_per_Year
    try:
        float(r+c+n+py)
    except:
        print('Please input numeric values')
    try:
        rn=n*py
        pv=[]
        r=r/100
        i=1
        pv.append((100+c)/(1+r/py)**rn)
        while i<rn:
            pv.append(c/(1+r/py)**i)
            i=i+1
        print('Flat price of the bond is $',sum(pv))
        if sum(pv)>100:
            print('Bond is trading at a premium')
        elif sum(pv)==100:
            print('Bond is trading at par')
        elif sum(pv)<100:
            print('Bond is trading at a discount')        
        print('Value of each payment is',pv)
        print('Lets find out the full price of your bond')
        try:
            T=int(input('What is the the year length method(360/365)'))
            if T==360:
                print('Since, it is probably a corporate bond, you should count each month as 30 day')
            elif T==365:
                print('Since, it is probably a government bond, you should count the actual number of days in each month')
            else:
                print('I would double check your input if I was you')
        except:
            print('Please try again')
        if T==360:
            t=int(input('How many months have passed since last payment?'))
            h=int(input('and how many days?'))
            t=t*30+h
        elif T==365:
            try:
                t=int(input('How many days exactly have passed since the last coupon?'))
            except:
                print('Please try again')
        else:
            try:
                t=int(input('How many days exactly have passed since the last coupon?'))                    
            except:
                print('Please try again')
        T=T/py
        AI=t/T*c
        print('The accrued interest of your bond is $',AI)
        print('Full price of the bond is $',sum(pv)+AI)
        q=input('Would you want for me to save those results in a txt file (y/n)')
        if q=='n':
            print('ok cool, proceed')
        elif q=='y':
            lines=[]
            print('The file name is Results\nand it is found in the folder you keep this program')
            with open("Results.txt","a") as file1:
                lines.append('Bond Price Function Results\n')
                lines.append(str('Yield to Maturity: '+str(Yield_to_Maturity)+'%\n'))
                lines.append(str('Coupon Payment: $'+str(Coupon_Payment)+' per pay period\n'))
                lines.append(str('Number Years to Maturity:'+str(Years_to_Maturity)+'\n'))
                lines.append(str('Number of Coupons per Year: '+str(Coupons_per_Year)+'\n'))
                lines.append(str('Year day count: '+str(T*py)+'\n'))
                lines.append(str('Day count since last Coupon: '+str(t)+'\n'))                  
                lines.append(str('Flat price of the bond is $'+str(sum(pv))+'\n'))
                lines.append(str('Full price of the bond is $'+str(sum(pv)+AI)+'\n'))
                lines.append(str('The accrued interest of your bond is $'+str(AI)+'\n'))
                lines.append(str('Value of each payment respectively is'+str(pv)+'\n'))
                lines.append('\n')
                for line in lines:
                    file1.writelines(line)
                    file1.close
    except:
            print('An error has occurred\nPlease use numeric values when applicable')        
def pv(Future_Value,Payments,Years_to_Maturity,Periods_per_Year,Required_ROR):
    c=Payments
    n=Years_to_Maturity
    py=Periods_per_Year
    r=Required_ROR
    fv=Future_Value
    try:
        float(c+n+py+r+fv)
    except:
        print('Please use numeric values')
    try:
        pv=[]
        rn=n*py
        r=r/100
        i=1
        pv.append((fv+c)/(1+r/py)**rn)
        while i<rn:
            pv.append(c/(1+r/py)**i)
            i=i+1
        print('Present Value of the investment is $',sum(pv))
        print('Present Value of all your payments is',pv)
        q=input('Would you want for me to save those results in a txt file (y/n)')
        if q=='n':
            print('ok cool, proceed')
        elif q=='y':
            lines=[]
            print('The file name is Results\nand it is found in the folder you keep this program')
            with open("Results.txt","a") as file1:
                lines.append('Present Value Function Results\n')
                lines.append(str('Number Years to Maturity of the investment:'+str(Years_to_Maturity)+'\n'))
                lines.append(str('Number of investment growth intervals per year per Year: '+str(Periods_per_Year)+'\n'))
                lines.append(str('Required Rate of Return of the Investment: '+str(Required_ROR)+'%\n'))
                lines.append(str('Future Value of the investment: $'+str(Future_Value)+'\n'))
                lines.append(str('Present Value of the investment is $'+str(sum(pv))+'\n'))
                lines.append(str('Present Value of all your payments is'+str(pv)+'\n'))
                lines.append('\n')
                for line in lines:
                    file1.writelines(line)
                    file1.close
    except:
        print('An error has occurred\n')        