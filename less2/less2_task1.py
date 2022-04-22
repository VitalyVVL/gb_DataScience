my_list = [1,2.3,None, True,'String',[3,4,5],(4,3,5,7),{1:'Vitaly', 2:'Lubin'}]
for i, item in enumerate(my_list,1):
    print(f"{i}  {item} - {type(item)}")