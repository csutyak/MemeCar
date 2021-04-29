import pyglet
from pyglet.window import key
from memeCar import memeCar
from gameObject import GameObject 
from walls import walls
from lineWalls import lineWalls
from checkpointLines import checkpointLines
from carScore import carScore

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
        self.frame_rate = 1/185.0

        self.carScore = carScore(5)

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

        self.ai_action = "null"
       	self.AI_actionLabel = pyglet.text.Label("AI action: ", x= 1650, y = 500, batch=self.labelBatch)
        self.AI_actionValue = pyglet.text.Label(str(self.ai_action), x= 1750, y = 500, batch=self.labelBatch)

        self.wallObj = lineWalls(self.wallPosArr)

        self.checkPointObj = checkpointLines(self.checkPointPosArray)

        trackimage = pyglet.image.load('Res/sprites/Track.png')
        self.trackbackground = pyglet.sprite.Sprite(trackimage, x=0, y = 0)

        self.carScore.start()

        self.keyPressUp = False
        self.keyPressDown = False
        self.keyPressRight = False
        self.keyPressLeft = False
        self.keyPressSpace = False

        self.startUp = True
        self.AIvisionOld = []
        self.AIvisionNew = []

        self.resetFlag = 0

        self.gameCtr = 0

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
        self.wallObj.draw()
        self.checkPointObj.draw()
        self.player.draw()
        self.labelBatch.draw()

    def update(self, dt):

        if self.carScore.checkTimeout():
            #self.resetFlag = 1 
            pass
        
        self.player.update(dt)
        if self.wallObj.checkCollision(self.player.carHitbox):
            self.collision = True
            self.resetFlag = 1
        else:
        	self.collision = False
        self.inRangeValue.text = str(self.collision)

        self.AIvisionNew = self.wallObj.getLineDistanceArr(self.player.carHitbox)
        
        if self.startUp == True:
            self.startUp = False

        else:
            score = 0
            action = self.AI_ACTION(self.AIvisionNew)

            if self.checkPointObj.checkCollision(self.player.carHitbox):
                self.carScore.checkPointReached()
                score = self.carScore.getLastIncremental()
            if self.collision:
                self.carScore.hitWall()
                score = self.carScore.getLastIncremental()

            agent.store_transition(self.AIvisionOld, action, score,self.AIvisionNew, int(self.resetFlag) )

            agent.learn()

        self.AIvisionOld = self.AIvisionNew


        if self.resetFlag == 1:
            print(agent.epsilon)
            self.reset()
    
    def reset(self):
        print("Game: ", self.gameCtr, "Finished with score ", self.carScore.score)
        if self.gameCtr % 500 == 1:
            agent.save(self.gameCtr)
            saveData(scores)
            print("SAVING DATA...")
        self.gameCtr += 1
        scores.append(self.carScore.score)
        eps_history.append(agent.epsilon)

        finalScore = self.carScore.reset()
        self.checkPointObj.reset()
        
        self.player.reset()

        self.carScore.start()

        self.resetFlag = 0

        self.startUp = True

    def updatePlayerKeys(self):
        self.player.keyUP = self.keyPressUp
        self.player.keyDOWN = self.keyPressDown
        self.player.keyRIGHT = self.keyPressRight
        self.player.keyLEFT = self.keyPressLeft
        self.player.keySPACE = self.keyPressSpace
    
    def AI_ACTION(self, input):
        action = agent.choose_action(input)
        self.keyPressUp = False
        self.keyPressDown = False
        self.keyPressRight = False
        self.keyPressLeft = False
        self.keyPressSpace = False

        #single key presses
        if action == 0:
            self.keyPressUp = True
            self.AI_actionValue.text = "UP"
        #double key presses
        elif action == 1:
            self.keyPressUp = True
            self.keyPressRight = True
            self.AI_actionValue.text = "UP RIGHT"
        elif action == 2:
            self.keyPressUp = True
            self.keyPressLeft = True
            self.AI_actionValue.text = "UP LEFT"
        elif action == 4:
            self.keyPressRight = True
            self.keyPressSpace = True
            self.AI_actionValue.text = "RIGHT SPACE"
        
        elif action == 5:
            self.keyPressLeft = True
            self.keyPressSpace = True
            self.AI_actionValue.text = "LEFT SPACE"

        #tripple key presses
        elif action == 6:
            self.keyPressUp = True
            self.keyPressLeft = True
            self.keyPressSpace = True
            self.AI_actionValue.text = "UP LEFT SPACE"
        elif action == 7:
            self.keyPressUp = True
            self.keyPressRight = True
            self.keyPressSpace = True
            self.AI_actionValue.text = "UP RIGHT SPACE"
        
        #nothing
        self.updatePlayerKeys()

        return action
    

        
        
        

if __name__ == "__main__":

    #actions
    #left, right, up, down, space, 
    # upright, upleft, updown, upspace, 
    # rightleft, rightdown, rightspace,
    # leftdown, leftspace,
    # downspace

    #threes
    # 
    agent = Agent(gamma = 1, epsilon = 1.0, batch_size = 1, n_actions=8,
                    eps_end=0.05, input_dims=[8], lr=0.003)
    scores, eps_history = [], []

    workingGameScore = 0

    window = GameWindow(1920, 1080, "meme car", resizable=True, fullscreen=False)
    pyglet.clock.schedule_interval(window.update, window.frame_rate)
    pyglet.app.run()