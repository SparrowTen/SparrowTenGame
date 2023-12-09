class GlobalVariable:
    def __init__(self):
        self.STATE = 'lobby'
        self.TICK = 0.0
        self.SKIN = 'default'

    def set_state(self, state):
        self.STATE = state

    def set_tick(self, tick):
        self.TICK = tick


GV = GlobalVariable()
