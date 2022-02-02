from turtle import color


major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]


oneBasedCountinString = ['0','0','0','0','0','0','0','0',]


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

def get_color_map_array():
    colorMap_array = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            colorIndex = get_color_index(i,j)
            colorMap_array.append([colorIndex,major,minor])
    return colorMap_array

def color_map_array_align_elements(color_map_arrayMapArray):
    arraySize=len(color_map_arrayMapArray)
    index_array=[]
    major_array=[]
    minor_array=[]
    for element in color_map_arrayMapArray:
        index_array.append(str(element[0]))
        major_array.append(element[1])
        minor_array.append(element[2])
    index_array = resize_array_to_biggest_element(index_array)
    major_array = resize_array_to_biggest_element(major_array)
    minor_array = resize_array_to_biggest_element(minor_array)
    aligned_array = []
    for i in range(arraySize):
        aligned_array.append([index_array[i],major_array[i],minor_array[i]])
    return aligned_array

def color_map_array2text(colorMapArray, separator="|"):
    color_map_to_Print = ""
    for possibleCombination in colorMapArray:
        for column in possibleCombination:
            color_map_to_Print += str( column ) + separator
        color_map_to_Print = color_map_to_Print[:-1] # Remove last separator
        color_map_to_Print += '\n'
    color_map_to_Print = color_map_to_Print[:-1] # Remove last '\n'
    return color_map_to_Print

def print_color_map(colorMapText):
    print(colorMapText)
    return len(major_colors) * len(minor_colors), colorMapText

colorMap = get_color_map_array()
colorMap_aligned = color_map_array_align_elements(colorMap)
colorMap_text = color_map_array2text(colorMap_aligned)
result, printedText = print_color_map(colorMap_text)

printedText_array = printedText.split("\n")
assert(result == len(printedText_array))
index_divisor1_prev = printedText_array[0].find("|")
index_divisor2_prev = printedText_array[0].rfind("|")
for zeroBased_row,line in enumerate(printedText_array):
    index_divisor1 = line.find("|")
    index_divisor2 = line.rfind("|")
    assert(str(zeroBased_row+1) == line[:index_divisor1].strip())
    assert(index_divisor1 == index_divisor1_prev)
    assert(index_divisor2 == index_divisor2_prev)

print("All is well\n")
