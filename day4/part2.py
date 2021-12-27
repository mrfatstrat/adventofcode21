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

lastWinner = None

# iterate the numbers
for n in numbers:
    print("Playing number: %s" % n)
    # iterate all boards to mark numbers
    for b in allBoards:
        if b['bingo']:
            continue
        #iterate all rows in a board
        for r in b['board']:
            if n in r:
                b['score'].append([b['board'].index(r),r.index(n)])
        rowHits = list(map(lambda x: x[0], b['score']))
        rowScore = {i:rowHits.count(i) for i in rowHits}
        if 5 in rowScore.values():
            print('Bingo on board %s' % allBoards.index(b))
            lastWinner = b
            index = rowScore.values().index(5)
            b['bingo'] = ['r',rowScore.keys()[index]]
        colHits = list(map(lambda x: x[1], b['score']))
        colScore = {i:colHits.count(i) for i in colHits}
        if not b['bingo'] and 5 in colScore.values():
            print('Bingo on board %s' % allBoards.index(b))
            lastWinner = b
            index = colScore.values().index(5)
            b['bingo'] = ['c',colScore.keys()[index]]
    boardsStillPlaying = len(filter(lambda x: not x['bingo'], allBoards))
    if boardsStillPlaying == 0:
        print('No more boards are playing')
        break

if lastWinner:
    print('')
    print("The last winner is board %s" % allBoards.index(lastWinner))
    print('')
    for r in lastWinner['board']:
        print(r)
    # summ all non marked numbers on board
    summary = 0
    for r in range(5):
        for c in range(5):
            if not [r,c] in lastWinner['score']:
                summary += lastWinner['board'][r][c]
    print('')
    print("Summary: ", summary, " score: ", (summary*n))

