'''
->TASK0045:
     Basic set initialization and summing distinct values

'''
def average(array):
    # your code goes here
    arr_set = set(array)
    sum_arr = sum(list(arr_set))
    return sum_arr/len(arr_set)
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)