class Filter:
    def init(self):
        self.blocked = []
    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter):
    def init(self):
        self.blocked = ['SPAM']

class Calculator:
    


"""
f = Filter()
f.init()
f.filter([1, 2, 3])

issubclass(SPAMFilter, Filter)
SPAMFilter.__bases__
isinstance()
s.__class__
"""