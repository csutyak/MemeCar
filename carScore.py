import time
from checkpointLines import checkpointLines

class carScore:
    def __init__(self, maxScore):
        self.score = 0
        self.timer = Timer()
        self.maxScore = maxScore
        self.incrementalScore = 0
    
    def start(self):
        self.timer.start()
    
    def checkTimeout(self): 
        if self.timer.getTime() > self.maxScore:
            return True
        return False
    
    def reset(self):
        finalScore = self.score
        self.timer.reset()
        self.score = 0
        return finalScore
    
    def hitWall(self):
        self.incrementalScore = -100
        self.score += self.incrementalScore

    def getLastIncremental(self):
        return self.incrementalScore


    def checkPointReached(self):
        self.incrementalScore = self.maxScore
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