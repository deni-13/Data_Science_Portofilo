#case 1

#1
#veri yapisi incele


x=8
type(x)
y=3.2
type(y)

z=8j +18
type(z)

a="Hello World"
type(a)

b=True
type(b)



c=23<22
type(c)


l=[1,2,3,4]
type(l)



d={"Name":"Jake","Age":27,"Address":"Downtown"}
type(d)


s={"Python","Machine Learning","Data Science"}
type(s)


#gorev 2:
#%% gorev 2
text="The goal is to turn data into information,and information into insight.".upper().split(" ")
text

#%%gorev 3
lst=["D","A","T","A","S","C","I","E","N","C","E"]


len(lst)
lst[0]
lst[10]
lst[0:4]
lst.pop(8)  #8. index
lst
lst.append("ai")

lst.insert(8,"n")
#%% gorev 4
dict ={'Christian': ["America", 18],
'Daisy':["England",12], 'Antonio':["Spain", 22], 'Dante': ["Italy", 25]}

dict.keys()
dict.values()
dict["Ahmet"]=["Turkey",24]
del dict["Antonio"]
#%% GOREV 5
def func(liste):
    even_list = []
    odd_list = []
    for i in liste:
        if i%2==0:
            even_list.append(i)
        else:
            odd_list.append(i)

    return even_list, odd_list

l = [2,13,18,93,22]
func(l)