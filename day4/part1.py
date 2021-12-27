file = open('input.txt','r')

numbers = file.readline().strip().split(',')
numbers = list(map(int,numbers))

allBoards = []
board = []
while True:
    line = file.readline()
    if not line:
        break
    if not line.strip():
        # empty line -> new board
        for i in range(5):
            row = file.readline().strip().split(' ')
            rowCleaned = filter(lambda x: x != '', row)
            rowCleaned = list(map(int,rowCleaned))
            board.append(rowCleaned)
        allBoards.append({"board": board, "score": [], "bingo": []})
        board = []
    else:
        print("Unexpected line... don't know what to do with: %s" % line)
        continue

winner = None

# iterate the numbers
for n in numbers:
    print("Checking number: %s" % n)
    # iterate all boards to mark numbers
    for b in allBoards:
        #iterate all rows in a board
        for r in b['board']:
            if n in r:
                b['score'].append([b['board'].index(r),r.index(n)])
        rowHits = list(map(lambda x: x[0], b['score']))
        rowScore = {i:rowHits.count(i) for i in rowHits}
        if 5 in rowScore.values():
            winner = b
            index = rowScore.values().index(5)
            b['bingo'] = ['r',rowScore.keys()[index]]
            break
        colHits = list(map(lambda x: x[1], b['score']))
        colScore = {i:colHits.count(i) for i in colHits}
        if 5 in colScore.values():
            winner = b
            index = colScore.values().index(5)
            b['bingo'] = ['c',colScore.keys()[index]]
            break

    if winner:
        print("The winner is:")
        for r in b['board']:
            print(r)
        # summ all non marked numbers on board
        summary = 0
        for r in range(5):
            for c in range(5):
                if not [r,c] in b['score']:
                    summary += b['board'][r][c]
        
        print("Summary: ", summary, " score: ", (summary*n))
        break

