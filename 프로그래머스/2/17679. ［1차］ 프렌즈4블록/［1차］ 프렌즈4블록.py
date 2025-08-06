
def solution(m, n, board):
    answer = 0
    
    for y in range(m):
        board[y] = list(board[y])
        
    isRemoved = True
    while isRemoved:
        removeBlocks = set()
        for y in range(m-1):
            for x in range(n-1):
                # (y, x) (y, x+1) (y+1, x) (y+1, x+1) 이 같은 블록인지 판단
                normBlock = board[y][x]
                if normBlock == 0:
                    continue

                for py, px in [(y, x+1), (y+1, x), (y+1, x+1)]:
                    if board[py][px] == 0 or normBlock != board[py][px]:
                        break;
                else:
                    removeBlocks.add((y, x))
                    removeBlocks.add((y, x+1))
                    removeBlocks.add((y+1, x))
                    removeBlocks.add((y+1, x+1))
        
        if len(removeBlocks) <= 0:
            isRemoved = False

        answer += len(removeBlocks)
        # 블록 제거
        for y, x in removeBlocks:
            board[y][x] = 0

        # 제거후 블록 아래로 떨어짐
        for x in range(n):
            blocks = [] # 제거후 남은 블록

            for y in range(m):
                if board[y][x] != 0:
                    blocks.append(board[y][x])
            nBlock = len(blocks)

            # 아래에서 부터 나머지 블록(blocks)을 쌓기
            for y in range(m-1, m-1-nBlock, -1):
                board[y][x] = blocks.pop()

            # 빈 공간의 수만큼 채우기
            for y in range(m-1-nBlock, -1, -1):
                board[y][x] = 0

        """
        for y in range(len(board)):
            print(board[y]) 
        print()
        """
    
    return answer