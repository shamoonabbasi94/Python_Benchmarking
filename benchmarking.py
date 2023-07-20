import timeit
setup_code = """
x = 'Carecloud'
"""
main_code = """ 
if type(x)==str:
    pass
"""
print(timeit.timeit(stmt=main_code,
                    setup=setup_code,
                    number=100000000))





import timeit
setup_code = """
x = 'Carecloud'
"""
main_code = """
if isinstance(x,str):
    pass
"""
print(timeit.timeit(stmt=main_code,
                    setup=setup_code,
                    number=100000000))




# Python 3 to check 
# Method 1 is the fastest
from timeit import timeit

setup = """
name = "Carecloud"
"""

method1 = """f'Hello, {name}, how is your day?'"""
method2 = """'Hello, {0}, how is your day?'.format(name)"""
method3 = """'Hello, %(who)s, how is your lamb?' % {'who': name}"""
method4 = """Hello, %s, how is your lamb?' % (name,)"""

for method in (method1, method2, method3, method4):
    print(timeit(setup=setup, stmt=method))



import timeit
setup_code = """
data=[12,12,34,681]
"""
main_code = """
result=[obj for obj in data if obj%2==0]
"""
print(timeit.timeit(stmt=main_code,
                    setup=setup_code,
                    number=10000000))



import timeit
setup_code = """
data=[12,12,34,681]
"""
main_code = """
result=filter(lambda x: x%2==0,data)
"""
print(timeit.timeit(stmt=main_code,
                    setup=setup_code,
                    number=10000000))



import timeit
setup_code = """
data=[12,12,34,681]

"""
main_code = """
result=[]
for obj in data:
    if obj%2==0:
        result.append(obj)
"""
print(timeit.timeit(stmt=main_code,
                    setup=setup_code,
                    number=10000000))



import timeit
setup_code = """
import pandas as pd
df=pd.read_csv('cpt_mod_xwalk.csv')

"""
main_code = """
df_=df[(df["Cpt_Code"] == '00100') & (df["Mod_code"] == '77')]
required_params = df_.values.tolist()
# print(required_params)
required_params = [_ for _ in required_params[0]]
"""
print(timeit.timeit(stmt=main_code,
                    setup=setup_code,
                    number=10))



import timeit
setup_code = """
temp_list=['hi','hello','test','dummy','demo']
dd_dict={}
id_dict={}

"""
main_code = """
for index,obj in enumerate(temp_list):
    dd_dict.update({index:obj})
    id_dict.update({index:obj})

dd_values = ' '.join(map(str,dd_dict.values()))
id_values = ' '.join(map(str,id_dict.values()))

#values = ' '.join(str(val) for val in my_dict.values())
"""
print(timeit.timeit(stmt=main_code,
                    setup=setup_code,
                    number=400))



import timeit
setup_code = """
temp_list=['hi','hello','test','dummy','demo']
my_list=[]
id_list=[]

"""
main_code = """
for obj in temp_list:
    my_list.append(obj)
    id_list.append(obj)

dd_values = ' '.join(my_list)
id_values = ' '.join(id_list)

"""
print(timeit.timeit(stmt=main_code,
                    setup=setup_code,
                    number=400))



import timeit
setup_code = """
import numpy as np
l1 = ['RTS','LTS','50']
l3 = ['RTSs','LTS','50s']

"""
main_code = """
if set(l1)== set(l3):
    x=1
    print('hi')

"""
print(timeit.timeit(stmt=main_code,
                    setup=setup_code,
                    number=500))



import timeit
setup_code = """
import numpy as np
l1= ['RT','LT','50']
l3 = ['Hello','RTS','LTS','50s']

"""
main_code = """
if np.sum(np.in1d(np.asarray(l1),l3))==0:
    x=1

"""
print(timeit.timeit(stmt=main_code,
                    setup=setup_code,
                    number=500))