from main.gilhyeon.StageOneSnowTheme import StageOneSnowTheme
from main.gilhyeon.StageTwoTheme import StageTwoSnowTheme
from main.gilhyeon.FirstToSecond import FirstToSecond
from main.gilhyeon.StageThreeTheme import StageThreeSnowTheme
from main.gilhyeon.SecondToThird import SecondToThird
from main.display.EndingScreen import endingScene

class MainGame:
    def run(self):
        self.fistStage = StageOneSnowTheme()

        self.firstToSecond = FirstToSecond()

        self.secondStage = StageTwoSnowTheme()

        self.secondToThird = SecondToThird()

        self.thirdStage = StageThreeSnowTheme()


        if(self.fistStage.run()==1):
            print("1 스테이지 클리어")

        if(self.firstToSecond.run()==1):
            print("2 스테이지 시작")

        if(self.secondStage.run()==1):
            print("2 스테이지 클리어")

        if (self.secondToThird.run() == 1):
            print("3 스테이지 시작")

        if (self.thirdStage.run() == 1):
            print("3 스테이지 클리어")
            endstart = endingScene()
            endstart.endingRun()


#Test
# test = MainGame()
# test.run()
