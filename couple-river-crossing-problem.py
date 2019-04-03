def Solver():
    """
    Input: None.

    Output: the shortest path in a reable way.

    """
    S = genStates()
    G = genGraph(S)
    s = "EEEEEEE" #source node
    d = "WWWWWWW" #destination node
    result = genShortestPath(G,s,d) 

    husband_wife = [' blue husband',' blue wife',' green husband',' green wife',' red husband',' red wife']
    genTrip(result,husband_wife)

def genTrip(result, husband_wife):
    """
    Input: p, the shortest path from s to d

    Output: print out the solution to the problem
    
    """
    for i in range(1,len(result)): 
        if result[i][6] == "E":
            source = "west"
            direction = "east"
        else:
            source = "east"
            direction = "west"

        who= []
        for j in range(6): #from 0 to 5 referring to 6 ppl
            if result[i-1][j] != result[i][j]:
                who.append(husband_wife[j])
        
        if len(who) > 1:
            print(str(i) +" The" +  who[0] + " and" + who[1] +" go"+" from the "+ source +" to the " + direction + ".")
        else:
            print(str(i) +" The" +  who[0] +" goes" +" from the "+ source +" to the " + direction + ".")
        

def genStates(): #generates all 128 states
    """
    Input: None
    Output: Return a set of all possible states for the problem
    """
    side = ("E", "W")
    states = []
    for i in side:
        for j in side:
            for k in side:
                for l in side:
                    for m in side:
                        for n in side:
                            for b in side: #b for boat
                                aState = i + j + k + l + m + n + b
                                states.append(aState)
    return states

def genGraph(S):
    """
    Input: S, a set of all possible states
    Output: Return a graph connnecting all the legal states in S
    """

    G = [] #G is the set that contains all legal states
    graph={} #create dictionary for the Graph
    for i in range(len(S)):
        if isLegal(S[i]) == True:
            G.append(S[i])

    
    for i in range(len(G)):
        result1 = nextStates(G[i],G)
        graph.update({G[i]:result1[1:]}) #add possible states to each legal states, put it in graph
    return graph
            
def isLegal(S):
    """
    Input: S, a state
    Output: return True if s is legal; otherwise, return False.
    """
    if ( S[1] != S[0] and ( S[1] == S[2] or S[1] == S[4])) or ( S[3] != S[2] and ( S[3] == S[0] or S[3] == S[4])) or( S[5] != S[4] and ( S[5] == S[0] or S[5] == S[2])) :
        return False
    elif (S[0] == S[1] and S[0] == S[2] and S[0] == S[3] and S[0] == S[4] and S[0] == S[5] and S[6] != S[0] ) :
        return False
    else:
        return True

    
def nextStates(n,R):
    """
    Input: n, the starting node (one entity in R); R, the set of legal states
    Output: return a set of n's neighboring states in R
    """
    possible = [n] # a set of n's possible neighboring states 

    
    for i in range(len(R)):

        if n[6] =="E" and R[i][6] == "W":
            c = 0
            valid = 1
            for j in range(6):
                if n[j] != R[i][j] and n[j] == "E":
                    c+=1
                    #continue
                elif n[j] != R[i][j] and n[j] == "W":
                    valid=0

            if c >= 1 and c <= 2 and valid !=0:
                possible.append(R[i])
            continue
        elif n[6] == "W" and R[i][6] == "E":
            c = 0
            valid = 1
            for j in range(6):
                if n[j] != R[i][j] and n[j] == "W":
                    c+=1
                    #continue
                elif n[j] != R[i][j] and n[j] == "E":
                    valid=0
            if c >= 1 and c <= 2 and valid !=0:
                possible.append(R[i])
    return possible
"""
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return None
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths
"""
def genShortestPath(graph, start, end, path=[]): #find the shortest path using recursion method
    """
    Input:graph, a graph; start, a source node; end, a distination node.
    Output: shortest, a path connecting from s to d with minimum distance.
    Source: https://www.python.org/doc/essays/graphs/
    """
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = genShortestPath(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

"""
   
def find_all_paths(graph, start, end, path=[]):
    
    path = path + [start]
    
    if start == end:
        return [path]
    
    if not graph.has_key(start):
        return []
    
    paths = []
    
    for node in graph[start]:
    
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
    
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def genShortestPath(graph, start, end, path=[]):
    path = path + [start] #1. work on the path- a list from start to end

    if start == end:    
        return [path]
    
    if not (start in graph):
        return None
    
    shortest = None
    
    paths = []
    
    for node in graph[start]:
    
        if node not in path:
            
            newpath = genShortestPath(graph, node, end, path)
            
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
                    paths.append(shortest)
                elif len(newpath) == len(shortest):
                    paths.append(newpath)
    return paths   
"""
Solver()

