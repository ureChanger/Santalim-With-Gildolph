from main.gilhyeon.StageOneSnowTheme import StageOneSnowTheme
from main.gilhyeon.StageTwoTheme import StageTwoSnowTheme
from main.gilhyeon.FirstToSecond import FirstToSecond

class MainGame:
    def run(self):
        self.a = StageOneSnowTheme()
        self.stageOne = 0

        self.b = StageTwoSnowTheme()

        self.c = FirstToSecond()


        if(self.a.run()==1):
            print("1 스테이지 클리어")

        if(self.c.run()==1):
            print("2 스테이지 시작")

        if(self.b.run()==1):
            print("2 스테이지 클리어")