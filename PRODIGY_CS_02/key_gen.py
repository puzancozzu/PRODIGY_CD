#### Generating a key  using chaotic map -- using Logistic map

### the effectivness or strongness of encryption also relies on key value - diversity and randomness
### size = numbers of key we need to generate

## logistic map: small change in initial or control parameter result in drastic change in key-values
def keygen(initial, control, size):
    key = []

    for i in range(size):

        initial = control*initial*(1-initial)  ##logistic map
        key.append(int((initial* pow(10,16))%256)) 
        ### mod 256 - can generate key value range from 0-255

    return key

# print(keygen(0.001,3.915,10))
