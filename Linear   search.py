#Christopher Pullen
#09.01.2015
#Linear Search

def linear_search (search_list, search_item):
    found = False
    count = 0
    while not found and count < len(search_list):
        if search_list[count] == search_item:
            print ("found")
            found = True
        else :
            count = count + 1
    return found

def found_check (found):
    if found == False:
        print ("not found")

# mian program


search_list = [ "pink", "purple" , "green" , "orange " , "blue" , "red" ]

search_item = input("please enter the coulor you wish to search for :D ")

found = linear_search (search_list , search_item)

found_check (found)
    
