
# Complete the climbingLeaderboard function below
def climbingLeaderboard(scores, alice):
    positions = []
    
   
    for alice_score in {*alice}:
        # positions.append(climbHelper(scores, 0, len(scores)-1, int(alice_score))
        positions.append(climbHelper(scores, 0, len(scores)-1, int(alice_score)))        
    return positions


def climbHelper(arr, start, end, value):
    if start >= end: #the size of the sub set is 1
        if value  > arr[start]:
            return start + 1
        elif value < arr[start]:
            return start - 1
        return start
    
    mid = (start+end)//2
    
    if value > arr[mid]:
        return climbHelper(arr, mid +1, end, value)

    return climbHelper(arr, start, mid, value)



# 7
# 100 100 50 40 40 20 10
# 4
# 5 25 50 120