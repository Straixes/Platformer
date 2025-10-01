class State:
    def __init__(self, game):
        self.game = game
    def handle_events(self, events,ScreenInfo=None): pass
    def update(self,ScreenInfo=None): pass
    def draw(self, screen,ScreenInfo=None): pass