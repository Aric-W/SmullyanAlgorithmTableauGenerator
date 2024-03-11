class TableauTree:
    directInferences = []
    left = None
    right = None
    
    def __init__(self, inp):
        self.directInferences = []
        self.directInferences.append(inp)
    
    def branch(self,l):
        if(self.left == None):
            self.left = TableauTree(l)
            return
        elif(self.right == None):
            self.right = TableauTree(l)
            return
        else:
            self.branch(l)
    
    def infer(self, inp):
        if(self.left == None and self.right == None):
            self.directInferences.append(inp)
        else:
            self.left.infer(inp)
            self.right.infer(inp)


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
        