def solution(enroll, referral, seller, amount):
    answer = []
    perPrice = 100
    
    sellAmt = dict()
    parent = dict() #key의 부모를 저장하는 딕셔너리
    for i, name in enumerate(enroll):
        parent[name] = referral[i]
        sellAmt[name] = 0
        
    for i in range(len(seller)):
        name, sellCnt = seller[i], amount[i]
        amt = sellCnt * perPrice
        #print("판매자 :", name)
        while (parent[name] != "-"):
            parentName = parent[name]
            payment = int(amt/10)
            if payment < 1:
                payment = 0
                break
            
            # 상납을 제외한 금액을 수익으로
            sellAmt[name] += amt - payment
            #print("{}가 {}의 수익을 얻음".format(name, amt-payment))
            
            #print("{}가 {}에게 {} 상납".format(name, parent[name], payment))
            name = parent[name]
            amt = payment
        
        payment = int(amt/10) 
        if payment < 1:
            payment = 0
        sellAmt[name] += amt - payment
        #print("{}가 {}의 수익을 얻음".format(name, amt-payment))
            
        
    for name in enroll:
        answer.append(sellAmt[name])
    
    #print(sellAmt)
    #print(answer)
        
    return answer