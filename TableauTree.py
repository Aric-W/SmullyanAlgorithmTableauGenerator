class TableauTree:
    directInferences = []
    left = None
    right = None
    
    #Python constructor
    def __init__(self):
        #each node has it's own list
        self.directInferences = []
        """#put some initial thing in the directInferences list
        self.directInferences.append(inp)"""
    
    def branch(self,l):
        #if there's no left branch, make one
        if(self.left == None):
            self.left = TableauTree()
            self.left.directInferences.append(l)
            return
        #if there's no right branch, make one
        elif(self.right == None):
            self.right = TableauTree()
            self.right.directInferences.append(l)
            return
        #branches are made in pairs
        else:
            self.branch(l)
    

    def infer(self, inp):
        #if there are no subtrees, then put on inferences
        if(self.left == None and self.right == None):
            self.directInferences.append(inp)
        #go down the left and then go down the right
        else:
            self.left.infer(inp)
            self.right.infer(inp)
            
            

    #This method makes a list of branches, branches are lists of inferred atomic statements
    def goDownTheBranches(self,branches,branch):
        branch = branch + self.directInferences
        if(self.left == None):
            branches.append(branch)
            return
        else:
            self.left.goDownTheBranches(branches,branch)
        if self.right == None:
            branches.append(branch)
            return
        else:
            self.right.goDownTheBranches(branches,branch)




