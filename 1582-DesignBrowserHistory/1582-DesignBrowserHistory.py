# Last updated: 2/11/2026, 11:08:17 AM
class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """

        self.index = 0
        self.url_arr = [homepage]
        

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.index+=1
        self.url_arr = self.url_arr[0:self.index]
        self.url_arr.append(url)

        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.index-=steps
        self.index = max (0, self.index)

        return self.url_arr[self.index]
        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """

        self.index+= steps
        self.index = min(len(self.url_arr)-1,self.index)

        return self.url_arr[self.index]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)