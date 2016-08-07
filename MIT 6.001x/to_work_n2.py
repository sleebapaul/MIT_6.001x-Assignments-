def item_order(string):
    my_string = string.lower().split()
    count1=0
    count2=0
    count3=0
    for item in my_string:
        if item =='salad':
            count1+=1
        elif item=='hamburger':
            count2+=1
        elif item=='water':
            count3+=1
    return 'salad:'+str(count1)+' hamburger:'+str(count2)+' water:'+str(count3)
 
order = "salad hamburger hamburger"
item_order(order)
  

    
    