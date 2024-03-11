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


    def goDownTheBranches(self,branches):
        branch = []
        for i in self.directInferences:
            branch.append(i)
        branches.append(branch)
        if(self.left != None):
            branch = branch + self.left.goDownTheBranches(branches)
        elif(self.right != None):
            branch = branch + self.right.goDowntheBranches(branches)
        return branches