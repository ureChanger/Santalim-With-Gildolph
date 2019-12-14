from main.gilhyeon.StageOneSnowTheme import StageOneSnowTheme
from main.gilhyeon.StageTwoTheme import StageTwoSnowTheme
from main.gilhyeon.FirstToSecond import FirstToSecond

a = StageOneSnowTheme()
stageOne = 0

c = FirstToSecond()


if(a.run()==1):
    print("1 스테이지 클리어")
    stageOne = 1

c.run()

if stageOne:
    b = StageTwoSnowTheme()
    b.run()
    print("2 스테이지 클리어")