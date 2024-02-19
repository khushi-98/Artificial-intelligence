import copy 
q=[]
visited=[]

def compare(s,g):
    if s==g:
        return 1
    else:
        return 0
    

def find_pos(s):
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j]==0:
                return [i,j]
            

def up(s):
    pos=find_pos(s)
    row=pos[0]
    col=pos[1]

    new_state=copy.deepcopy(s)
    if row>0:
        new_state[row][col]=new_state[row-1][col]
        new_state[row-1][col]=0

    return new_state

def down(s):
    pos=find_pos(s)
    row=pos[0]
    col=pos[1]

    new_state=copy.deepcopy(s)
    if row<2:
        new_state[row][col]=new_state[row+1][col]
        new_state[row+1][col]=0
    
    return new_state

def left(s):
    pos =find_pos(s)
    row=pos[0]
    col=pos[1]

    new_state=copy.deepcopy(s)
    if col>0:
        new_state[row][col]=new_state[row][col-1]
        new_state[row][col-1]=0

    return new_state

def right(s):
    pos=find_pos(s)
    row=pos[0]
    col=pos[1]

    new_state=copy.deepcopy(s)
    if col<2:
        new_state[row][col]=new_state[row][col+1]
        new_state[row][col+1]=0
    return new_state

def generate_children(s):
    global q 
    global visited
    new_state=up(s)
    if new_state not in visited and new_state not in q:
        q.append(new_state)
    
    new_state=down(s)
    if new_state not in visited and new_state not in q:
        q.append(new_state)
    
    new_state=left(s)
    if new_state not in visited and new_state not in q:
        q.append(new_state)
    
    new_state=right(s)
    if new_state not in visited and new_state not in q:
        q.append(new_state)


def search(g):
    global q
    global visited

    while(1):
        curr_state=q[0]
        del q[0]
        if compare(curr_state,g)==1:
            print("Found")
            exit()
        else:
            generate_children(curr_state)
            visited.append(curr_state)


def main():
    global q
    s=[[1,2,3],[8,4,0],[7,6,5]]

    g=[[2,8,1],[0,4,3],[7,6,5]]

    q.append(s)
    search(g)


main()