from collections import Counter

def solution(friends, gifts):
    answer = 0
    
    nameToIndex = dict();
    indexToName = dict();
    giftScore = Counter();
    
    for i, name in enumerate(friends):
        nameToIndex[name] = i
        indexToName[i] = name
        
    board = [[0 for _ in range(len(nameToIndex))] for _ in range(len(nameToIndex))]
    for record in gifts:
        sender, receiver = record.split()
        senderIndex = nameToIndex[sender]
        receiverIndex = nameToIndex[receiver]
        
        giftScore[senderIndex] += 1
        giftScore[receiverIndex] -= 1
        board[senderIndex][receiverIndex] += 1
        
    maxValue = 0
    for senderIndex in range(len(friends)):
        nGift = 0
        targetGiftScore = giftScore[senderIndex]
        for receiverIndex in range(len(friends)):
            #print("준 사람", indexToName[senderIndex])
            #print("받은 사람", indexToName[receiverIndex])
            # 본인 제외
            if senderIndex == receiverIndex: 
                continue;
            
            # 두 사람이 선물을 주고받은 기록이 있을 경우
            if board[senderIndex][receiverIndex] != 0:
                if board[senderIndex][receiverIndex] > board[receiverIndex][senderIndex]: 
                    nGift += 1
                # 두 사람이 같은 개수의 선물을 주고 받았을 경우
                elif board[senderIndex][receiverIndex] == board[receiverIndex][senderIndex]:
                    if targetGiftScore > giftScore[receiverIndex]:
                        nGift +=1

            # 두 사람이 선물을 주고받은 기록이 하나도 없는 경우
            elif board[receiverIndex][senderIndex] == 0:
                if targetGiftScore > giftScore[receiverIndex]:
                    nGift +=1
        
        maxValue = max(maxValue, nGift)
            
    return maxValue