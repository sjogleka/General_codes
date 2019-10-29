def iterate(emp1,temp,designation_emp):
    #print(designation_emp.get(emp1))
    if(designation_emp.get(emp1)!="Boss"):
        temp.append(designation_emp.get(emp1))
        iterate(designation_emp.get(emp1),temp,designation_emp)
    return temp




if __name__ == '__main__':
    temp = []
    temp2=[]
    set_emp = set(["Gaurav","Sakshat","Pratik","Sumedh","Anup","Pawan","Srishti"])
    designation_emp = {"Gaurav":"Sumedh","Sakshat":"Sumedh","Pratik":"Sumedh","Sumedh":"Anup","Anup":"Srishti","Pawan":"Srishti","Srishti":"Boss"}
    #print(designation_emp.get("Srishti"))
    a = iterate("Gaurav",temp,designation_emp)
    b = iterate("Sumedh",temp2,designation_emp)
    s = set()
    a.reverse()
    b.reverse()
    print("a = ", a)
    print("b = ", b)
    LCM = "none"
    if len(a)<len(b):
        for i in range(len(a)):
            if a[i]!=b[i]:
                LCM = a[i-1]
        if LCM == "none":
            LCM = b[len(a)-1]
    else:
        for i in range(len(b)):
            if b[i]!=a[i]:
                LCM = b[i-1]
        if LCM == "none":
            LCM = a[len(b)-1]

    print(LCM)


    '''
    if len(a)>len(b):
        for i in range(len(a)):
            s.add(a[i])
    else:
        for i in range(len(b)):
            s.add(b[i])
    print("s - ",s)
    if len(a)>len(b):
        print("In if",len(a))
        for i in range(len(a)-1,-1,-1):
            #print(i)
            if a[i] not in s:
                print(a[i])
                LCM = a[i+1]
                print(LCM)
                break
            else:
                print("In else")
        print("Out of for")
    else:
        for i in range(len(b)-1,-1,-1):
            if b[i] not in s:
                LCM = b[i + 1]
                break
    #print(LCM)
    
    '''