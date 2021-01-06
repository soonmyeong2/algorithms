class MinStack(object):

    def __init__(self):
        self.stack = list()
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append((x, min(x, self.getMin())))
       
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][1]
        return float('inf')
