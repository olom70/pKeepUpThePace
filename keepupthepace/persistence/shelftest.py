import shelve

class IterRegistry(type):
    def __iter__(cls):
        return iter(cls._registry)

class MyClass(object):
    _counter = 0
    _registry = []

    def __init__(self):
        self._registry.append(self)
        MyClass._counter += +1
        self.id = MyClass._counter
 
    def addText(self, text):
        self.text = text


firstC = MyClass()
firstC.addText("Un")

scondC = MyClass()
scondC.addText("deux")

shelf = shelve.open("profileshelf.db")
try:
    for myClassObject in MyClass._registry:
        pass
finally:
    shelf.close



