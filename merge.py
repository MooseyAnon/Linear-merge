def lin_merge(l1, l2):

  i=0
  j=0
  newl=[]

  while i < len(l1) and j < len(l2):

    if l1[i] < l2[j]:
      newl.append(l1[i])
      i+=1
    elif l1[i] == l2[j]:
      newl.append(l1[i])
      newl.append(l2[j])
      i+=1
      j+=1
    else:
      newl.append(l2[j])
      j+=1

  while i < len(l1):
    newl.append(l1[i])
    i+=1 

  while j < len(l2):
    newl.append(l2[j])
    j+=1

  return newl


a = [1,3,4,7,8, 34, 65, 74]
b = [0,2,4,6,8,10,12]


print lin_merge(a, b)

# outputs: [0, 1, 2, 3, 4, 4, 6, 7, 8, 8, 10, 12, 34, 65, 74]
