MAX_SIZE = 50
MIN_SIZE = 30

S_M_Umbral_Size = 38
M_L_Umbral_Size = 42

RECOMEND_BIGGER = True

def size(cms):
    if cms < 38:
        return 'S'
    elif cms > 38 and cms < 42:
        return 'M'
    else:
        return 'L'

# Test all valid values
for ZeroBasedShirtSizeinCM in range(MAX_SIZE-MIN_SIZE):
    # Convert Zero based to size
    ShirtSizeinCM = ZeroBasedShirtSizeinCM+MIN_SIZE 
    # Test Small sizes
    if(ShirtSizeinCM < S_M_Umbral_Size):
        assert(size(ShirtSizeinCM) == 'S')
    elif(ShirtSizeinCM == S_M_Umbral_Size):
        if(RECOMEND_BIGGER is True):
            assert(size(ShirtSizeinCM) == 'M')
        else:
            assert(size(ShirtSizeinCM) == 'S')
    # Test Medium sizes
    elif(ShirtSizeinCM < M_L_Umbral_Size):
        assert(size(ShirtSizeinCM) == 'M')
    elif(ShirtSizeinCM == M_L_Umbral_Size):
        if(RECOMEND_BIGGER is True):
            assert(size(ShirtSizeinCM) == 'L')
        else:
            assert(size(ShirtSizeinCM) == 'M')
    # Test Large sizes
    else:
        assert(size(ShirtSizeinCM) == 'L')

# Test uncoherent values
assert(size(MIN_SIZE-1) == 'NA')
assert(size(MAX_SIZE+1) == 'NA')

print("All is well \n")
