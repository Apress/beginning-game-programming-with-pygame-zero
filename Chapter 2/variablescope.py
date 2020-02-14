variable1 = 1
variable2 = 1

def local_function (variable1):
    variable1 += 1
    variable2 = 5
    print ("variable1 in local_function {}".format(variable1))
    print ("variable2 in local_function {}\n".format(variable2))
    
def global_function (argument1):
    global variable1, variable2
    variable1 = argument1 + 10
    variable2 = 15
    print ("variable1 in global_function {}".format(variable1))
    print ("variable2 in global_function {}\n".format(variable2))
    

print ("variable1 in top level code {}".format(variable1))
print ("variable2 in top level code {}\n".format(variable2))

local_function (variable1)

print ("variable1 in top level code {}".format(variable1))
print ("variable2 in top level code {}\n".format(variable2))

global_function (variable1)

print ("variable1 in top level code {}".format(variable1))
print ("variable2 in top level code {}".format(variable2))