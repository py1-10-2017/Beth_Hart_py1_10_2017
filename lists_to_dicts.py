name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "bear", "giraffe", "ticks", "dolphins", "llamas"]


"""zips 2 lists into single dictionary, longer list forms the keys;
and additional keys without value, are set to None"""
def lists_to_dict(arr1,arr2):
    #find which list is longer to use as keys
    if len(arr1) == len(arr2):
        new_dict = dict(zip(arr1,arr2))
    else:
        if len(arr1) > len(arr2):
            new_dict = zip(arr1,arr2)
            """cache keys w/o value pair in trailing keys list"""
            trail_keys = arr1[-(len(arr1)-len(arr2)):] #subtract short from long list, result splices long list, captures keys w/no value
        elif len(arr2) > len(arr1): #if arr2 is longer -- repeat above process
            new_dict = zip(arr2,arr1)
            trail_keys = arr2[-(len(arr2)-len(arr1)):]
        new_dict = dict(new_dict) #convert sipped tuple to dict
        new_dict.update({}.fromkeys(trail_keys))  #capture trailing keys in new_dict; set value as None      
    print new_dict
    return new_dict

    
