  def dijkstra(self, s): # s is starting position to find all the shortests paths from
        open = APQ() # open stars as an empty APQ
        locs = {} # Empty dictionary - keys are vertices, values are location in open)
        closed = {} # closed starts as an empty dictionary
        preds = {s: None} # preds starts as a dictionary with value for s = None
        element = open.addToHeap(0, s) # add s with key 0 to open
        locs[s] = element # add s: element to locs
        while open.length() is not 0: # while open is not empty
            apq = open.removemin()   # remove the min element from open
            vertex = apq._value # get vertex value
            cost = apq._key # initiate cost
            locs.pop(vertex) # remove the entry for vertex from locs
            predecessor = preds.pop(vertex) # remove the entry for vertex from preds
            closed[vertex] = (cost, predecessor)  # add an entry for v :(cost, predecessor) into closed
            for edge in self.get_edges(vertex): # for each edge e from v
                w = edge.opposite(vertex) # w is the opposite vertex to v in e
                if w not in closed: # if w is not in closed
                    new_cost = cost + edge._element # newcost is v's key plus e's cost
                    if w not in locs: # if w is not in locs
                        preds[w] = vertex #add w:v to preds,
                        element = open.addToHeap(new_cost, w) # add w:newcost to open,
                        locs[w] = element # add w:(elt returned from open) to locs
                    elif new_cost < open.get_key(locs[w]): # else if newcost is better than w's oldcost
                        preds[w] = vertex # update w:v in preds
                        open.update_key(locs[w], new_cost) #  update w's cost in open to newcost
        return closed