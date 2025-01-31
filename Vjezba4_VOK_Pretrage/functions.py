from state import State
    
def generate(state, state_graph):
    if state.__str__() in state_graph.keys():
        return state_graph
    
    if not state.is_terminal() or state.is_solved():
        state_graph[state.__str__()] = state.copy()
        
    for action in state.all_actions():
        state.action(action)
        state_graph = generate(state, state_graph)
        state.undo_action(action)
        
    return state_graph     


def print_graph(state_graph):
    for key in state_graph.keys():
        print(key)


def check(element, visited):
    for v in visited:
        if v.__str__() == element.__str__():
            return True
    return False

def solution_bfs(start_state):
    visited = set()
    parent = {}
    queue = [start_state]

    while queue:
        current_state = queue.pop(0)
        if current_state.is_solved():
            visited.add(current_state)
            path = []
            
            while current_state:
                path.append(current_state)
                current_state = parent.get(current_state)
            print("Visited:", len(visited))
            return path[::-1]

        if not check(current_state, visited):
            visited.add(current_state)
            for next_state in current_state.next_states():
                if not next_state.is_terminal():
                    queue.append(next_state)
                    parent[next_state] = current_state
    
    return None

def solution_dfs(start_state):
    visited = set()
    parent = {}
    stack = [start_state]

    while stack:
        current_state = stack.pop()
        if current_state.is_solved():
            visited.add(current_state)
            path = []
            while current_state:
                path.append(current_state)
                current_state = parent.get(current_state)
                
            print("Visited:", len(visited))
            return path[::-1]

        if not check(current_state, visited):
            visited.add(current_state)
            for next_state in current_state.next_states():
                if not next_state.is_terminal():
                    stack.append(next_state)
                    parent[next_state] = current_state
    
    return None

def heuristic(state):
    counter = 0
    right_side = state.description[9:11]
        
    for i in right_side:
        if i != "-":
            counter += 1
    return counter

def solution_bestFS(start_state):
    visited = set()
    parent = {}
    queue = [start_state]

    while queue:
        current_state = queue.pop(0)
        if current_state.is_solved():
            visited.add(current_state)
            path = []
            while current_state:
                path.append(current_state)
                current_state = parent.get(current_state)
            print("Visited:", len(visited))
            return path[::-1]

        if not check(current_state, visited):
            visited.add(current_state)
            for next_state in current_state.next_states():
                    if not next_state.is_terminal():
                        queue.append(next_state)
                        parent[next_state] = current_state
            
            queue = sorted(queue, key = heuristic)
    return None
    
 
        
def main():
    state = State()
    
    graph = {}
    generate(state, graph)
    #print_graph(graph)
    
    print("Broj stanja:", len(graph))
    
    print("\nSolution BFS")
    path = solution_bfs(state)
    #print("Path:", len(path))
    #for element in path:
    #    print(element)
    
    print("\nSolution DFS")
    path = solution_dfs(state)
    #print("Path:", len(path))
    
    print("\nSolution bestFS")
    path = solution_bestFS(state)
    #print("Path: ", len(path))
    
if __name__ == "__main__":
    main()