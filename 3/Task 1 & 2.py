import random

def minimax(depth, Index, maximizingPlayer, points, alpha, beta):
    if depth == 3:
        return points[Index]

    if maximizingPlayer:
        best = Min_value

        for i in range(0, 2):

            val = minimax(depth + 1, Index * 2 + i, False, points, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = Max_value

        for i in range(0, 2):
            val = minimax(depth + 1, Index * 2 + i, True, points, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break

    return best

# TASK-1:

Id = input('Enter ID = ')

# Converting any 0 digit in ID to 8
for i in Id:
    if i == '0':
        Id = Id.replace(i, '8')

shuffle_no = int(Id[3])

Min_value = int(Id[4])

last2digit = Id[6:]

pointstoWin = int(last2digit[::-1])

Max_value = int(pointstoWin * 1.5)

randomlist = []
for i in range(0, 8):
    n = random.randint(Min_value, Max_value)
    randomlist.append(n)

print('Generated 8 random points between the minimum and maximum point limits: ', randomlist)
print('Total points to win: ', pointstoWin)

result = minimax(0, 0, True, randomlist, Min_value, Max_value)

print("Achieved point by applying alpha-beta pruning =", result)

if result >= pointstoWin:
    print('The winner is Optimus Prime')
else:
    print('The winner is Megatron')

# TASK-2:

print('\nAfter the shuffle:')

resultList = []
for i in range(0, shuffle_no):
    random.shuffle(randomlist)
    result2 = minimax(0, 0, True, randomlist, Min_value, Max_value)
    resultList.append(result2)

print('List of all points values from each shuffle:', resultList)
print('The maximum value of all shuffles:', max(resultList))

win = 0
for i in resultList:
    if i >= pointstoWin:
        win += 1

print('Won', win, 'times out of', shuffle_no, 'number of shuffles')