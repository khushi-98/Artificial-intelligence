import copy 

q = []
visited = []

def compare(s, g):
    if s == g:
        return 1
    else:
        return 0

def find_pos(s):
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == 0:
                return [i, j]

def empty_jug1(s):
    new_state = copy.deepcopy(s)
    new_state[0] = 0
    return new_state

def empty_jug2(s):
    new_state = copy.deepcopy(s)
    new_state[1] = 0
    return new_state

def full_jug1(s):
    new_state = copy.deepcopy(s)
    new_state[0] = 4
    return new_state

def full_jug2(s):
    new_state = copy.deepcopy(s)
    new_state[1] = 3
    return new_state

def transfer1(s):
    new_state = copy.deepcopy(s)
    if s[0] + s[1] <= 4:
        new_state[0] = s[0] + s[1]
        new_state[1] = 0
    else:
        new_state[1] = s[1] - (4 - s[0])
        new_state[0] = 4
    return new_state

def transfer2(s):
    new_state = copy.deepcopy(s)
    if s[0] + s[1] <= 3:
        new_state[1] = s[0] + s[1]
        new_state[0] = 0
    else:
        new_state[0] = s[0] - (3 - s[1])
        new_state[1] = 3
    return new_state

def generate_children(s):
    global q
    global visited

    operations = [empty_jug1, empty_jug2, full_jug1, full_jug2, transfer1, transfer2]

    for operation in operations:
        new_state = operation(s)
        if new_state not in q and new_state not in visited:
            q.append(new_state)

def search(initial_state, goal_state):
    global q
    global visited
    q.append(initial_state)
    while q:
        curr_state = q.pop(0)
        if compare(curr_state, goal_state) == 1:
            print("Found")
            return
        else:
            generate_children(curr_state)
            visited.append(curr_state)
    print("Not found")

def main():
    initial_state = [4, 0]
    goal_state = [2, 0]
    search(initial_state, goal_state)

main()
