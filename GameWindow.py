import pyglet
from pyglet.window import key
from memeCar import memeCar
from gameObject import GameObject 
from lineWalls import lineWalls
from checkpointLines import checkpointLines
from carScore import carScore
import torch

#add prompts for the scores of each action so I can drive around and see if the game has learned 

#console 
import threading
from consoleActions import consoleActions

consoleObj = consoleActions()
#function to give console commands for the game
def consoleStart():
    consoleRunFlag = False
    
    while not consoleRunFlag:
        userInput = input(">")
        consoleObj.parseConsoleActions(userInput)
        consoleRunFlag = consoleObj.exitFlag

#learning! oooooohhh
from DQNagentSimple import Agent

def saveData(scoreList):
    a_file = open("output/score.txt", "w")
    
    ctr = 0
    for score in scoreList:
        outputString = "Game " + str(ctr) +  ": " +  str(score) + "\n"
        a_file.write(outputString)
        ctr += 1

    a_file.close()

class GameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_location(0, 0)
        self.frame_rate = 1/30.0

        self.carScore = carScore()

        self.player = memeCar(100, 1080 - 950, 0.00001, 'nyoom.png')
        self.wallPosArr = [[[17, 1080 - 991],[24, 1080 - 98]],
            [[24, 1080 - 95],[216, 1080 - 36]],
            [[220, 1080 - 36],[1669, 1080 - 37]],
            [[1669, 1080 - 37],[1819, 1080 - 89]],
            [[1819, 1080 - 89],[1872, 1080 - 153]],
            [[1872, 1080 - 153],[1876, 1080 - 954]],
            [[1876, 1080 - 954],[1655, 1080 - 1046]],
            [[1655, 1080 - 1046],[683, 1080 - 1052]],
            [[683, 1080 - 1052],[603, 1080 - 999]],
            [[603, 1080 - 999],[611, 1080 - 564]],
            [[611, 1080 - 564],[1250, 1080 - 534]],
            [[1250, 1080 - 534],[1341, 1080 - 686]],
            [[1341, 1080 - 686],[1517, 1080 - 704]],
            [[1517, 1080 - 700],[1578, 1080 - 546]],
            [[1578, 1080 - 543],[1488, 1080 - 571]],
            [[1486, 1080 - 573],[1344, 1080 - 502]],
            [[1344, 1080 - 502],[1095, 1080 - 490]],
            [[1095, 1080 - 490],[517, 1080 - 493]],
            [[517, 1080 - 493],[400, 1080 - 418]],
            [[400, 1080 - 418],[478, 1080 - 313]],
            [[478, 1080 - 313],[343, 1080 - 306]],
            [[343, 1080 - 306],[388, 1080 - 534]],
            [[388, 1080 - 534],[546,1080 - 556]],
            [[546,1080 - 556],[535, 1080 - 960]],
            [[535, 1080 - 960],[400, 1080 - 1048]],
            [[400, 1080 - 1048],[52, 1080 - 1051]],
            [[52, 1080 - 1051],[16, 1080 - 991]],
            [[193, 1080 - 862],[381, 1080 - 868]],
            [[381, 1080 - 868],[399, 1080 - 666]],
            [[399, 1080 - 666],[274, 1080 - 648]],
            [[274, 1080 - 648],[234, 1080 -229]],
            [[232, 1080 - 213],[634, 1080 - 217]],
            [[634, 1080 - 217],[610, 1080 - 370]],
            [[610, 1080 - 370],[1363, 1080 - 375]],
            [[1363,1080 - 375],[1525, 1080 - 421]],
            [[1525, 1080 - 421],[1612, 1080 - 387]],
            [[1612, 1080 - 387],[1671 , 1080 - 423]],
            [[1671, 1080 - 423],[1696, 1080 - 589]],
            [[1696, 1080 - 589],[1680, 1080 - 802]],
            [[1680, 1080 - 802],[1596, 1080 - 819]],
            [[1596, 1080 - 819],[1230, 1080 - 841]],
            [[1230, 1080 - 841],[1168, 1080 - 690]],
            [[1168, 1080 - 690],[822, 1080 - 723]],
            [[822, 1080 - 723],[856, 1080 - 903]],
            [[856, 1080 - 903],[1720, 1080 - 846]],
            [[1720, 1080 - 846],[1719, 1080 - 732]],
            [[1719, 1080 - 732],[1684, 1080 - 240]],
            [[1684, 1080 - 240],[1626, 1080 - 181]],
            [[1626, 1080 - 181],[231, 1080 - 190]],
            [[231, 1080 - 190],[192, 1080 - 861]]
            ]
        
        self.checkPointPosArray = [
                [[193, 1080 - 861], [18, 1080 - 855]],
                [[222, 1080 - 369], [21, 1080 - 372]],
                [[412, 1080 - 189],  [415, 1080 - 34]],
                [[1043, 1080 - 0] ,  [1045, 1080 - 184]],
                [[1623, 1080 - 181], [1669, 1080 - 34]],
                [[1710, 1080 - 628], [1875, 1080 - 619]],
                [[1654, 1080 - 1050],[1620, 1080 - 850]],
                [[1033, 1080 - 888],[1029, 1080 - 1050]],
                [[829, 1080 - 760],[606, 1080 - 772]],
                [[1134, 1080 - 537],[1141, 1080 - 694]],
                [[1536, 1080 - 652],[1692, 1080 - 678]],
                [[1246, 1080 - 499],[1257, 1080 - 372]],
                [[648, 1080 - 366],[631, 1080 - 493]],
                [[351, 1080 - 337],[241, 1080 - 349]],
                [[391, 1080 - 742],[543, 1080 - 751]]
            ]

        self.collision = False
        self.labelBatch = pyglet.graphics.Batch()
       	self.inRangeLabel = pyglet.text.Label("Collision: ", x= 1650, y = 600, batch=self.labelBatch)
        self.inRangeValue = pyglet.text.Label(str(self.collision), x= 1750, y = 600, batch=self.labelBatch)

        self.actionScoreLabel = pyglet.text.Label("Actions Score: ", x= 1600, y = 1000, batch=self.labelBatch)
        self.action0 = pyglet.text.Label("null ", x= 1600, y = 950, batch=self.labelBatch)
        self.action1 = pyglet.text.Label("null ", x= 1500, y = 900, batch=self.labelBatch)
        self.action2 = pyglet.text.Label("null ", x= 1700, y = 900, batch=self.labelBatch)
        self.action3 = pyglet.text.Label("null ", x= 1500, y = 850, batch=self.labelBatch)
        self.action4 = pyglet.text.Label("null ", x= 1700, y = 850, batch=self.labelBatch)
        self.action5 = pyglet.text.Label("null ", x= 1500, y = 800, batch=self.labelBatch)
        self.action6 = pyglet.text.Label("null ", x= 1700, y = 800, batch=self.labelBatch)
        
        self.frontDis = pyglet.text.Label("front ", x= 1600, y = 750, batch=self.labelBatch)
        self.backDis = pyglet.text.Label("back ", x= 1600, y = 650, batch=self.labelBatch)
        self.topRightDist = pyglet.text.Label("top right ", x= 1700, y = 725, batch=self.labelBatch)
        self.bottomLeftDist = pyglet.text.Label("bottom left ", x= 1500, y = 675, batch=self.labelBatch)
        self.rightDist = pyglet.text.Label("right ", x= 1700, y = 700, batch=self.labelBatch)
        self.leftDist = pyglet.text.Label("left ", x= 1500, y = 700, batch=self.labelBatch)
        self.topLeftDist = pyglet.text.Label("top left ", x= 1500, y = 725, batch=self.labelBatch)
        self.bottomRighttDist = pyglet.text.Label("bottom right ", x= 1700, y = 675, batch=self.labelBatch)
        
        self.ai_action = "null"
       	self.AI_actionLabel = pyglet.text.Label("AI action: ", x= 1650, y = 500, batch=self.labelBatch)
        self.AI_actionValue = pyglet.text.Label(str(self.ai_action), x= 1750, y = 500, batch=self.labelBatch)

        self.wallObj = lineWalls(self.wallPosArr)

        self.checkPointObj = checkpointLines(self.checkPointPosArray)

        self.background = pyglet.graphics.OrderedGroup(0)
        self.foreground = pyglet.graphics.OrderedGroup(1)

        trackimage = pyglet.image.load('Res/sprites/Track.png')
        self.trackbackground = pyglet.sprite.Sprite(trackimage, group = self.background)

        self.carScore.start()

        self.startUp = True
        self.AIvisionOld = []
        self.AIvisionNew = []

        self.resetFlag = 0
        self.resetNextFrame = 0

        self.gameCtr = 0

        self.localHighscore = 0
        self.localHighscoreGame = 0

    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.player.keyUP = True
        if symbol == key.DOWN:
            self.player.keyDOWN = True
        if symbol == key.LEFT:
            self.player.keyLEFT = True
        if symbol == key.RIGHT:
            self.player.keyRIGHT = True
        if symbol == key.SPACE:
            self.player.keySPACE = True

    def on_key_release(self, symbol, modifiers):
        if symbol == key.UP:
            self.player.keyUP = False
        if symbol == key.DOWN:
            self.player.keyDOWN = False
        if symbol == key.LEFT:
            self.player.keyLEFT = False
        if symbol == key.RIGHT:
            self.player.keyRIGHT = False
        if symbol == key.SPACE:
            self.player.keySPACE = False

    def on_draw(self):
        self.clear()
        self.trackbackground.draw()
        self.player.draw()
        self.labelBatch.draw()

    def update(self, dt):
        if self.resetNextFrame == 1:
            self.resetFlag = 1

        if self.carScore.checkTimeout():
            self.resetFlag = 1 
            pass
        
        if self.wallObj.checkCollision(self.player.carHitbox):
            self.collision = True
            self.resetNextFrame = 1
        else:
        	self.collision = False
        self.inRangeValue.text = str(self.collision)

        self.AIvisionNew = self.wallObj.getLineDistanceArr(self.player.carHitbox)
        #self.drawDistance(self.AIvisionNew)
        
        if self.startUp == True:
            self.startUp = False
        else:
            score = 0
            action = self.AI_ACTION(self.AIvisionNew)
            self.drawLabels(agent.get_action_array(self.AIvisionNew))

            if self.checkPointObj.checkCollision(self.player.carHitbox):
                self.carScore.checkPointReached()
                score = self.carScore.getLastIncremental()
            if self.collision:
                self.carScore.hitWall()
                score = self.carScore.getLastIncremental()

            agent.store_transition(self.AIvisionOld, action, self.carScore.score ,self.AIvisionNew, self.resetFlag )
            agent.learn()

            #check for console flags
            if consoleObj.getHSFlag():
                print("local Highscore is: ", str(self.localHighscore))
                print("on game:", str(self.localHighscoreGame))
            
            if consoleObj.getPrintEpFlag():
                print("EP Value: ", str(agent.getEPValue()))
            
            if consoleObj.getPrintGameNumFlag():
                print("Game Number: ", str(self.gameCtr))
            
            flag, value = consoleObj.getSetEpFlag()
            if flag:
                agent.setEPValue(value)
            
            flag, value = consoleObj.getSaveFlag()
            if flag:
                print("saving to... " , value)
                agent.saveModel(value)
            
            flag, value = consoleObj.getLoadFlag()
            if flag:
                print("loading from... ", value)
                agent.loadModel(value)
            
        self.AIvisionOld = self.AIvisionNew

        if self.resetFlag == 1:
            self.reset()
              
        self.player.update(dt)
    
    def reset(self):
        if self.gameCtr % 500 == 1:
            agent.save(self.gameCtr)
            saveData(scores)
        self.gameCtr += 1
        scores.append(self.carScore.score)
        eps_history.append(agent.epsilon)

        finalScore = self.carScore.reset()
        if finalScore > self.localHighscore:
            self.localHighscore = finalScore
            self.localHighscoreGame = self.gameCtr
        self.checkPointObj.reset()
        
        self.player.reset()

        self.carScore.start()

        self.resetFlag = 0

        self.resetNextFrame = 0

        self.startUp = True
    
    def AI_ACTION(self, input):
        action = agent.choose_action(input)

        #single key presses
        if action == 0:
            self.player.keyUP = True
            self.player.keyDOWN = False
            self.player.keyLEFT = False
            self.player.keyRIGHT = False
            self.player.keySPACE = False
            self.AI_actionValue.text = "UP"
        #double key presses
        elif action == 1:
            self.player.keyUP = True
            self.player.keyLEFT = True
            self.player.keyDOWN = False
            self.player.keyRIGHT = False
            self.player.keySPACE = False
            self.AI_actionValue.text = "UP LEFT"
        elif action == 2:
            self.player.keyUP = True
            self.player.keyRIGHT = True
            self.player.keyDOWN = False
            self.player.keyLEFT = False
            self.player.keySPACE = False
            self.AI_actionValue.text = "UP RIGHT"

        elif action == 3:
            self.player.keyLEFT = True
            self.player.keySPACE = True
            self.player.keyUP = False
            self.player.keyDOWN = False
            self.player.keyRIGHT = False          
            self.AI_actionValue.text = "LEFT SPACE"
        elif action == 4:
            self.player.keyRIGHT = True
            self.player.keySPACE = True
            self.player.keyUP = False
            self.player.keyDOWN = False
            self.player.keyLEFT = False
            self.AI_actionValue.text = "RIGHT SPACE"

        #tripple key presses
        elif action == 5:
            self.player.keyUP = True
            self.player.keyLEFT = True
            self.player.keySPACE = True
            self.player.keyDOWN = False
            self.player.keyRIGHT = False
            self.AI_actionValue.text = "UP LEFT SPACE"
        elif action == 6:
            self.player.keyUP = True
            self.player.keyRIGHT = True
            self.player.keySPACE = True
            self.player.keyDOWN = False
            self.player.keyLEFT = False
            self.AI_actionValue.text = "UP RIGHT SPACE"

        return action   
    def drawLabels(self, scoreArray):
        #print(scoreArray[0][0].item())
        self.action0.text = str(scoreArray[0][0].item())
        self.action1.text = str(scoreArray[0][1].item())
        self.action2.text = str(scoreArray[0][2].item())
        self.action3.text = str(scoreArray[0][3].item())
        self.action4.text = str(scoreArray[0][4].item())
        self.action5.text = str(scoreArray[0][5].item())
        self.action6.text = str(scoreArray[0][6].item())

    def drawDistance(self, distanceArray):
        self.frontDis.text = str(distanceArray[0])
        self.backDis.text = str(distanceArray[1])
        self.topRightDist.text = str(distanceArray[2])
        self.bottomLeftDist.text = str(distanceArray[3])
        self.leftDist.text = str(distanceArray[4])
        self.rightDist.text = str(distanceArray[5])
        self.topLeftDist.text = str(distanceArray[6])
        self.bottomRighttDist.text = str(distanceArray[7])
        
if __name__ == "__main__":

    #actions
    #left, right, up, down, space, 
    # upright, upleft, updown, upspace, 
    # rightleft, rightdown, rightspace,
    # leftdown, leftspace,
    # downspace

    consoleThread = threading.Thread(target=consoleStart, args=())
  
    # starting thread 1
    consoleThread.start()

    agent = Agent(gamma = .999, epsilon = 1.0, batch_size = 1000, n_actions=7,
                    mem_size = 50000, eps_end=0.1,eps_dec=5e-7, replace =1000, 
                    input_dims=[8], lr=0.0001)
                
    scores, eps_history = [], []

    workingGameScore = 0

    window = GameWindow(1920, 1080, "meme car", resizable=True, fullscreen=False)
    pyglet.clock.schedule_interval(window.update, window.frame_rate)
    pyglet.app.run()

    consoleThread.join()