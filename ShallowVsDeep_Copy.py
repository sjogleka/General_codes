import copy

if __name__ == '__main__':
    array1 = [1,2,2,5,6,7]
    ########################################### Assignment ###################################################
    print("###################### Assignment ##################")
    array2 = array1
    print("Before Change Array 1:-", array1)
    print("Before Change Array 2:-", array2)
    array2[1]=4
    print("Array 1 after change in array2:-",array1)
    print("Array 2 after change in array2:-", array2)
    array1[2]=3
    print("After change in array 1 Array 1:-", array1)
    print("After Change in array 1 Array 2:-", array2)
    ############################################## Deep Copy ##################################################
    print("###################### Deep copy ##################")
    array3 = copy.deepcopy(array1)
    array3[2]=10
    print("After Deep Copy",array1)
    print("After Deep Copy", array3)
    ################################################# Shallow Copy ##########################################
    print("###################### Shallow copy ##################")
    array4 = copy.copy(array1) ## Shallow copy using copy.
    print("Address of array 1:-",id(array1),"Address of array 4:-",id(array4)) ## Print address of array 1 and array4
    print("Before Change Array 1:-", array1)
    print("Before Change Array 2:-", array4)
    array1[0] = 500
    print("After Shallow Copy", array1)
    print("After Shallow Copy", array4)
    print("--------------------------------------")
    #################################### Special Case List of list ###############################
    ##### This is the actual difference between shallow copy and deep copy ########
    array5 = [[1,2,3],[4,5]]
    array6 = copy.copy(array5)
    print("Before Shallow Copy", array5)
    print("Before Shallow Copy", array6)
    array6[0][1] = 4
    print("After Shallow Copy Change", array5)
    print("After Shallow Copy Change", array6)
    print("ID of a[0]a[1]",id(array5[0]),id(array5[1]),"\nID of b[0]b[1]",id(array6[0]),id(array6[1]))
    print("Id A",id(array5),"Id of B",id(array6))
    print("--------------------------------------")
    array7 = copy.copy(array1)
    print("ID A :- ",id(array1),"ID B :- ",id(array7))

    #### Ref :- https://medium.com/@thawsitt/assignment-vs-shallow-copy-vs-deep-copy-in-python-f70c2f0ebd86 ####
