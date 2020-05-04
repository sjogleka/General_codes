#####################################################################################
############################## Final Class ##########################################
#####################################################################################

class Final(type):

    def __new__(self, name, base, ns):
        #print(name,base,ns)
        for b in base:
            if isinstance(b,Final):
                raise TypeError("Can not instantiate final")

        return type.__new__(self,name,base,ns)

class myClass(metaclass=Final):
    pass

class myclass2(metaclass=Final):
    pass

######## Remove below comments to learn about final class ##########
#class myclass3(myClass):
#    pass

#####################################################################################
############################## Multiple Inheritance #################################
#####################################################################################

# Ref - https://www.i-programmer.info/programming/python/12217-programmers-python-mutliple-inheritance.html?start=2
# Ref - https://en.wikipedia.org/wiki/C3_linearization


'''
class A:
    def __init__(self):
        print("A :- parent class")

    def method1(self):
        print("In mthod1 of A")

#Class B inherits A
class B(A):
    def __init__(self):
        print("B: - Derived class")

    def method1(self):
        print("In mthod1 of B")

#Class C inherits A
class C(A):
    def __init__(self):
        print("C: - Derived class")

    def method1(self):
        print("In mthod1 of C")

#Class D inherits B->A
class D(B):
    def __init__(self):
        print("D: - Derived class")

#Class E inherits D,C - D->B->C->A->object
class E(D,C):
    def __init__(self):
        print("E: - Derived class")
        print(E.mro())

#Class F inherits C,D - C->D->B->A->object
class F(C,D):
    def __init__(self):
        print("F: - Derived class")
        print(F.mro())
'''

#Overriding __repr__ method from type in metaclass cutomTemp

class customTemp(type):
    def __repr__(self):
        return self.__name__


class O(metaclass=customTemp):pass

class A(O): pass

class B(O): pass

class C(O): pass

class D(O): pass

class E(O): pass

class K1(A, B, C): pass

#class K2(D, B, E): pass

class K2(E, D, B): pass
'''Think -  IMP 
In case of Z(K1,K2,K3) after done with K1 and K2 we have A in the next seq but not an ideal candidate 
as it appears at the tail of K3. Next is E - ideal candidate and can be visited. Hence E will be visited
before K3

'''
class K3(D, A): pass

class Z(K1, K2, K3): pass

if __name__ == '__main__':
    print("---------------- Implementation of Final ------------------")
    print(Final.__dict__)
    print(myClass.__dict__)

    print("--------------- Multiple Inheritance -------------------")
    '''
    Here MRO plays important role. 
    C3 linearization properties:- 
    It produces mro such that - 
    - has no base classes before their child classes
    - each class is only included once
    - the local left to right order used in the class declaration is preserved. If A is to the left of B in a class declaration then it will be earlier in the mro.
    - The mro is monotonic in that subclassing an existing class does not change the order of classes in the existing mro.
    
    In the explained example MRO of Z will be calculated as follows:-
    1. First K1,K2,K3 will be visited as there are no prereq needs to be consider before visitin them
    2. Now as K1 comes first and is derived from  A, B, C in order.
        - To visit A we must visit D first as K3(D,A)
    3. Hence D will be visited first then A and remaining classes in the way they appears in Z.
    
    e = E()
    e.method1()
    f = F()
    f.method1()
    '''
    print("K1 MRO :- ")
    print(K1.mro())
    print("K2 MRO :- ")
    print(K2.mro())
    print("K3 MRO :- ")
    print(K3.mro())
    print("Z MRO :- ")
    print(Z.mro())


