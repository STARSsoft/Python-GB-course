import random as rnd

'''
каждый ферзь будет на различной горизонтали и вертикали, что облегчит подбор.
'''
def get_values():

    my_list=[]
    v_val=[1,2,3,4,5,6,7,8]
    
    for i in range(8):
        v=rnd.choice(v_val)
        v_val.remove(v)
        g=i+1
        my_list.append([g,v])
    return my_list