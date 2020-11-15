# selection sort
# Doesnt work properly
def selection_sort(lis):
    for i in range(len(lis) - 1): 
        min_idx = i 
        for j in range(i + 1, len(lis) - 1): 
            if lis[min_idx] > lis[j]: 
                min_idx = j 
        lis[i], lis[min_idx] = lis[min_idx], lis[i] 
        return lis


A = eval(input("Enter the list to be sorted : "))
data = selection_sort(A)
print(data)