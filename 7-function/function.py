

def performLoop(scoreList):
    
    new_score = []
    for score in scoreList:
        item = score + 20
        new_score.append(item)

    return new_score


scoreList = [20, 13, 24, 56, 23.4, 50, 40, 50, 80, 100, 134, 7, 9, 70]



data = performLoop(scoreList)


# print(data)


