import numpy as np #External module, need to install using pip
#pip freeze | grep numpy  grep is linux commmand to find version of module
q1 = np.array([
    [123, 333, 555],
    [666, 777, 888],
    [999, 1000, 1111]
])

q2 = np.array([
    [222, 333, 444],
    [555, 666, 777],
    [888, 999, 1000]
])
print(q1 + q2)