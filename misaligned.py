major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]

def print_color_map():
    color_map_to_Print = ""
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            color_map_to_Print += f'{i * 5 + j} | {major} | {minor}\n'
    color_map_to_Print = color_map_to_Print[:-1] # Remove last '\n'
    print(color_map_to_Print)
    return len(major_colors) * len(minor_colors), color_map_to_Print

result, printedText = print_color_map()

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
