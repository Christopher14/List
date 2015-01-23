#Christopher pullen
#09.01.15
# bubble sort

def bubble_sort (unsorted_list):
    sort = False 
    while sort== False :
        sort = True
        for colors in range(len(unsorted_list)-1):
            if unsorted_list[colors] > unsorted_list[colors+1]:
                sort=False
                temp= unsorted_list[colors]
                unsorted_list[colors] = unsorted_list[colors+1]
                unsorted_list[colors+1] = temp
    return unsorted_list

#main program 
unsorted_list = [ "pink", "yellow" , "green" , "orange" , "blue" , "red" ]
sorted_list = bubble_sort (unsorted_list)
print ("{0} " .format (sorted_list)) 






                          
        
                        
    
