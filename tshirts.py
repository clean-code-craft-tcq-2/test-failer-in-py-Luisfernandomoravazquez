MAX_SIZE = 50
MIN_SIZE = 30

S_M_Umbral_Size = 38
M_L_Umbral_Size = 42

RECOMEND_BIGGER = False

def size(cms):
    if( cms < MIN_SIZE or cms > MAX_SIZE ):
        return 'NA'

    if(RECOMEND_BIGGER):
        cms += 1

    if cms <= S_M_Umbral_Size:
        return 'S'
    elif cms > S_M_Umbral_Size and cms <= M_L_Umbral_Size:
        return 'M'
    else:
        return 'L'

def testValidValues():
    # Test all valid values
    for ZeroBasedShirtSizeinCM in range(MAX_SIZE-MIN_SIZE):
        # Convert Zero based to size
        ShirtSizeinCM = ZeroBasedShirtSizeinCM+MIN_SIZE
        ShirtSizeLetter = size(ShirtSizeinCM) 

        # Test Small sizes
        if(ShirtSizeinCM < S_M_Umbral_Size):
            assert(ShirtSizeLetter == 'S')
        elif(ShirtSizeinCM == S_M_Umbral_Size):
            if(RECOMEND_BIGGER is True):
                assert(ShirtSizeLetter == 'M')
            else:
                assert(ShirtSizeLetter == 'S')
        # Test Medium sizes
        elif(ShirtSizeinCM < M_L_Umbral_Size):
            assert(ShirtSizeLetter == 'M')
        elif(ShirtSizeinCM == M_L_Umbral_Size):
            if(RECOMEND_BIGGER is True):
                assert(ShirtSizeLetter == 'L')
            else:
                assert(ShirtSizeLetter == 'M')
        # Test Large sizes
        else:
            assert(ShirtSizeLetter == 'L')

        print(str(ShirtSizeinCM)+" is "+ ShirtSizeLetter)

def testUncoherentValues():
    # Test uncoherent values
    ShirtSizeLetter = size(MIN_SIZE-1)
    assert(ShirtSizeLetter == 'NA')
    print(str(MIN_SIZE-1)+" is "+ ShirtSizeLetter)

    ShirtSizeLetter = size(MAX_SIZE+1)
    assert(ShirtSizeLetter == 'NA')
    print(str(MAX_SIZE+1)+" is "+ ShirtSizeLetter)


testValidValues()
testUncoherentValues()
print("All is well \n")
