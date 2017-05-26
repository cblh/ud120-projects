from __future__ import division
def featureScaling(arr):
    maxOne = max(arr)
    minOne = min(arr)
    diferencia = maxOne - minOne
    def scaler(item):
        return (item - minOne) / diferencia
    return map(scaler, arr)

# tests of your feature scaler--line below is input data
data = [115, 140, 175]
print featureScaling(data)