class State(object):
    state = [];
    parent = [];
    child = [];
    def __init__(self,currentState,parent,child):
        self.state = currentState;
        self.parent = parent;
        self.child = child;
