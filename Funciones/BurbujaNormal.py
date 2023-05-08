
def bubble_sort(data):
    intercambio = True
    while intercambio:
        intercambio = False
        for i in range(len(data)-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                intercambio = True
                
    return data
           
  
data=[0,24,42,2451,51,245]
a=bubble_sort(data)
print(a)