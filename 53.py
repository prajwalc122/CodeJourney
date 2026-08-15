#TWO SUM USING AN ARRAY
''' Example: we target an 10 '''
arr=[11,22,44,5,2]
target=16
for i in range(len(arr)):
  for j in range (i+1,len(arr)):
    if arr[i]+arr[j] == target:
      print (i,j)
    else:
      print("Not sum because target element not in list of array")
