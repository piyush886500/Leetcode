arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
# for i in range(len(arr)):
#     for j in range(len(arr[0])):
#         print(arr[i][j]," ",end="")

m = len(arr)
n = len(arr[0])
top = 0
bottom = m-1
left = 0
right = n-1


while top <= bottom and left <= right:

    for i in range(left,right+1):
        print(arr[top][i],end="  ")
    top+=1

    for j in range(top,bottom+1):
        print(arr[j][right],end="  ")
    right-=1

    for k in range(right,left-1,-1):
        print(arr[bottom][k],end="  ")
    bottom-=1

    for l in range(bottom,top-1,-1):
        print(arr[l][left],end="  ")
    left+=1
    