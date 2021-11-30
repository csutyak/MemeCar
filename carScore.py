import time
from checkpointLines import checkpointLines

class carScore:
    def __init__(self):
        self.score = 0
        self.timer = Timer()
        self.incrementalScore = 0

        self.checkPointScore = 10
        self.timeout = 5
        self.hitWallScore = -10
    
    def start(self):
        self.timer.start()
    
    def checkTimeout(self): 
        if self.timer.getTime() > self.timeout:
            return True
        return False
    
    def reset(self):
        finalScore = self.score
        self.timer.reset()
        self.score = 0
        return finalScore
    
    def hitWall(self):
        self.incrementalScore = self.hitWallScore
        self.score += self.incrementalScore

    def getLastIncremental(self):
        return self.incrementalScore


    def checkPointReached(self):
        self.incrementalScore = self.checkPointScore
        self.score += self.incrementalScore
        self.timer.reset()
        self.timer.start()

class Timer:
    def __init__(self):
        self._start_time = None

    def start(self):
        """Start a new timer"""

        self._start_time = time.perf_counter()

    def reset(self):
        """Stop the timer, and report the elapsed time"""

        self._start_time = 0
    
    def getTime(self):
        return time.perf_counter() - self._start_time