def solution(board, moves):
    cnt = 0 
    stack = []
    
    for idx in moves : 
        for i in range(len(board)):
            if board[i][idx-1] != 0:
                if stack and stack[-1] == board[i][idx-1]:
                    stack.pop()
                    cnt += 2
                    
                else:
                    stack.append(board[i][idx-1])
                    
                board[i][idx-1] = 0
                break
                
            else: 
                continue  
                
    return cnt
     