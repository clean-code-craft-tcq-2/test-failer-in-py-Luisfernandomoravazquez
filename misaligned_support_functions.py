def resize_array_to_biggest_element(array):
    newArray=[]
    maxSize=len( max(array,key=len) )
    for element in array:
        diference = maxSize-len(element)
        newElement=element
        for value in range(diference):
            newElement+=" "
        newArray.append(newElement)
    return newArray
    
def get_color_index(major_index,minor_index):
    return major_index * 5 + minor_index + 1

def get_columns_from_color_map_array(color_map_array):
    index_array=[]
    major_array=[]
    minor_array=[]
    for element in color_map_array:
        index_array.append(str(element[0]))
        major_array.append(element[1])
        minor_array.append(element[2])
    return index_array,major_array,minor_array

def get_color_map_array_from_columns(index_array,major_array,minor_array):
    aligned_array = []
    for i in range(len(index_array)):
        aligned_array.append([index_array[i],major_array[i],minor_array[i]])
    return aligned_array
