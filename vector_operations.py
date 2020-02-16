# =================================================================================
# Operations of vectors
# INFORMATION 
# numpy tutorial
# https://facundoq.github.io/courses/images/res/03_numpy.html
# doc - numpy
# https://zenodo.org/record/3599567
# vectors
# https://mathinsight.org/n_dimensional_vector_examples
# magnitude of vectors
# https://www.omnicalculator.com/math/vector-magnitude
# https://math.stackexchange.com/questions/2601108/vector-magnitude-in-dimensions-4
# =================================================================================
# import math and numpy to run
import math
import numpy as np

def options():
    n = validation_METHOD(welcome())
   
    while n != 0:
        n = validation_METHOD(welcome())
        
        if n == 1:
            # add vectors
            print("="*60)
            print("THIS IS THE OPTION 1 - ADD VECTORS")
            add_vector()
        elif n == 2:
            # subtract vector
            print("="*60)
            print("THIS IS THE OPTION 2 - SUBSTRACT VECTORS")
            subtract_vector()
         
        elif n == 3:
            print("="*60)
            print("-"*40)
            print("SELECT SUB OPTIONS: 3.1, 3.2, 3.3, 3.4, 3.5")
            print("-"*40)
            # multiply vector
        elif n == 3.1:
            print("="*60)
            print("THIS IS THE OPTION 3.1 - PRODUCT WITH A SCALAR")
            # PRODUCT WITH A SCALAR
            product_with_scalar()
        elif n == 3.2:
            print("="*60)
            print("THIS IS THE OPTION 3.2 - SCALAR PRODUCT OF TWO VECTORS")
            # PRODUCT OF TWO VECTORS
            scalar_product_two_vectors()
            
        elif n == 3.3:
            print("="*60)
            print("THIS IS THE OPTION 3.3 - VECTOR PRODUCT OF TWO VECTORS")
            # PRODUCT OF TWO VECTORS
            vector_product_two_vectors()
        elif n == 3.4:
            print("="*60)
            print("THIS IS THE OPTION 3.4 - TRIPLE SCALAR PRODUCT")
            # TRIPLE SCALAR PRODUCT
            triple_scalar_product()
        elif n == 3.5:
            print("="*60)
            print("THIS IS THE OPTION 3.5 - TRIPE VECTOR PRODUCT")
            # TRIPE VECTOR PRODUCT
            triple_vector_product()
        elif n == 0:
            print("="*60)
            print("Bye")
        else:
            print("="*60)
            print("-"*40)
            print("This is not in the option")
            print("The options are 1, 2, 3.1, 3.2, 3.3, 3.4, 3.5 and 0")
            print("Try again")
            print("-"*40)
            continue
    print("finish")
    
def welcome():
    return """
====================================================
              OPERATIONS OF VECTORS
====================================================

    1- ADD VECTORS
    2- SUBTRACT TWO VECTORS
    3- MULTIPLY VECTORS
       3.1- PRODUCT WITH A SCALAR
       3.2- SCALAR PRODUCT OF TWO VECTORS
       3.3- VECTOR PRODUCT OF TWO VECTORS
       3.4- TRIPLE SCALAR PRODUCT
       3.5- TRIPLE VECTOR PRODUCT
    0- EXIT
    
    Note: \"Access option 3.<option> to products\"
    OPTION: 
    """
def add_vector():
    
    m = int(validation_METHOD("How many vectors do you need to add: "))
    element = int(validation_METHOD("How many elements does have the vector: "))
    # ---------------------------
    matrix = make_matrix(m, element)
    #-----------------
    # print(matrix)
    print("-"*70)
    add_rows(matrix)  
    print("-"*70)
            
    

def subtract_vector():
    # just for two vectors
    print("Just for two vectors")
    element = int(validation_METHOD("How many elements does have the vector: "))
    # --------------
    matrix = make_matrix(2, element)
    # -------------
    print("-"*70)
    subtract(matrix)
    print("-"*70)
    

def product_with_scalar():
    
    scalar_num = validation_METHOD("Value of escalar: ")
    element = int(validation_METHOD("How many elements does have the vector: "))
    magnitude_sum = 0
    # -----------
    vector = make_matrix(1, element)
    # ------------
    result_vector = vector[0, :]*scalar_num
    for k in result_vector:
        magnitude_sum += k**2
    magnitude = math.sqrt(magnitude_sum)
    print("-"*70)
    print("The result R = {} x {} = {}".format(scalar_num, vector[0, :], result_vector))
    print("The magnitude |R| = {}".format(round(magnitude, 3)))
    print("-"*70)
    
def scalar_product_two_vectors():
    # just for two vectors
    print("Just for two vectors")
    element = int(validation_METHOD("How many elements does have the vector: "))
    # ----------------
    matrix = make_matrix(2, element)
    # ----------------
    
    add_product=0
    for i in range(len(matrix[0, :])):
        add_product += matrix[0, i]*matrix[1, i]
    print("-"*70)
    print("The scalar product V_1.V_2 = {}".format(add_product))
    # angle between two vectors
    angle_product_scalar(matrix)
    print("-"*70)


def vector_product_two_vectors():
    print("Just for two vectors with 3 element\nFirst V_1 then V_2\nV_1 X V_2:")
    # -----------------
    m = make_matrix(2, 3)
    # -----------------
    print(m)
    x = m[0, 1]*m[1, 2] - m[0, 2]*m[1, 1]
    y = (-1)*(m[0, 0]*m[1, 2] - m[0, 2]*m[1, 0])
    z = m[0, 0]*m[1, 1] - m[0, 1]*m[1, 0]
    magnitude = math.sqrt(x**2 + y**2 + z**2)
    vector = [round(x, 3), round(y, 3), round(z, 3)]
    print("-"*70)
    print("The result of V_1 X V_2 = {}".format(vector))
    print("The magnitude ||V_1 X v_2|| = {}".format(round(magnitude, 3)))
    angle_product_scalar(m)
    print("-"*70)


def triple_scalar_product():
    print("Just for 3 vectors with 3 element")
    print("calculate v_1 . (V_2 X V_3)")
    m = make_matrix(3, 3)
    print(m)
    a = m[0, 0]*(m[1, 1]*m[2, 2] - m[1, 2]*m[2, 1])
    b = m[0, 1]*(m[1, 0]*m[2, 2] - m[1, 2]*m[2, 0])
    c = m[0, 2]*(m[1, 0]*m[2, 1] - m[1, 1]*m[2, 0])
    result = a + (-1)*b + c
    print("-"*70)
    print("The result of v_1 . (V_2 X V_3) = {}".format(result))
    print("-"*70)
    

def triple_vector_product():
    # just for three vectors
    print("Just for 3 vectors with 3 element")
    print("calculate v_1 X (V_2 X V_3)")
    print("note : \"type in order\"")
    m = make_matrix(3, 3)
    # print(m)
    s_1 = 0
    s_2 = 0
    magnitude_sum = 0
    for i in range(len(m[0, :])):
        s_1 += m[0, i]*m[2,i]
        
    for j in range(len(m[0, :])):
        s_2 += m[0, j]*m[1, j]
        # print(s_2)
    
    x = s_1*m[1, 0] - s_2*m[2, 0]
    y = s_1*m[1, 1] - s_2*m[2, 1]
    z = s_1*m[1, 2] - s_2*m[2, 2]
    vector = [round(x, 3), round(y, 3), round(z, 3)]
    for k in vector:
        magnitude_sum += k**2
    magnitude = math.sqrt(magnitude_sum)
    print("-"*70)
    print("The result of v_1 X (V_2 X V_3) = {}".format(vector))
    print("The magnitude |v_1 X (V_2 X V_3)| = {}".format(round(magnitude, 3)))
    print("-"*70)
    
def validation_METHOD(valor_INPUT):
    # using validation
    while True:
        try:
            valor = float(input(valor_INPUT))
            return valor
        except ValueError:
            print("-"*40)
            print("Type a number. Try again")
            print("-"*40)

def add_rows(any_matrix):
    am = any_matrix
    add_element = 0
    # [row, colum] 
    # [i:f, i:f]
    # print(len(am[:, 0]))
    vector = np.zeros(len(am[0, :])) # [0, 0, ..., 0] n times
    # print(vector)
    for k in range(len(am[:, 0])):
        vector += am[k, :]
    
    for i in vector:
        add_element += i**2
        
    magnitude = math.sqrt(add_element)
    # print(am[0, :]) # row 1
    # print(am[1, :]) # row 2
    # print(am[2, :]) # row 3
    # calculate the angle between two vectors
    if len(am[:, 0]) == 2:
        angle_product_scalar(am)
    print("The result R = {}".format(vector))
    print("The magnitude |R| = {}".format(round(magnitude, 3)))

def subtract(any_matrix):
    am = any_matrix
    add_element = 0
    dif = am[0, :] - am[1, :]
    # calculate the angle between two vectors
    angle_product_scalar(am)
    # calculate the magnitude
    for k in dif:
        add_element += k**2
    magnitude = math.sqrt(add_element)
    print("The subtract R =  {}".format(dif))
    print("The magnitude |R| = {}".format(round(magnitude, 3)))
    
   
def angle_product_scalar(am):
    add_r1 = 0
    add_r2 = 0
    add_product = 0
    if len(am[0, :]) == 2 or len(am[0, :]) == 3:
        for i in am[0, :]:
            add_r1 += i**2
            
        for j in am[1,:]:
            add_r2 += j**2
        for k in range(len(am[0, :])):
            add_product += am[0, k]*am[1, k]
        r1 = math.sqrt(add_r1)
        # print(r1)
        r2 = math.sqrt(add_r2)
        # print(r2)
        # print(add_product)
        
        angle_rad = math.acos((add_product)/(r1*r2))
        angle_s = angle_rad*(180/math.pi)
        print("The angle between the vectors = {} rad  = {}°".format(
                round(angle_rad, 3), round(angle_s, 3)))
        
def make_matrix(vectors, elements):
    v = []
    mx = []
    for k in range(1, vectors + 1):
        for e in range(1, elements + 1):
            ELEMENT = validation_METHOD("a_{} = ".format(e))
            v.append(ELEMENT)
        
        print("V_{} = {}".format(k, v))
        # print(v)
        mx.extend([v])
        # print(mx)
        v = []
    # print(mx)
    return np.array(mx)
    
    
    
options()
# triple_vector_product()
#scalar_product_two_vectors()
# print(math.acos(3/5)*180/math.pi)






