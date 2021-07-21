# calculating the bit information value for each of the inputs

bitvalue_array = []

for x in range(0, len(weightedinputwithnoisearray)):
  float = weightedinputwithnoisearray[x]
  integer = math.floor(float)
  if float - integer > 0.5:
    integer = integer + 1
    try:
      integer = math.log(integer) / math.log(2)
      bitvalue_array.append(integer)
    except:
        integer = 0
        bitvalue_array.append(integer)
  else:
    try:
      integer = math.log(integer) / math.log(2)
      bitvalue_array.append(integer)
    except:
      integer = 0
      bitvalue_array.append(integer)

print(bitvalue_array)
