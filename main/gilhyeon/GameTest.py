from main.gilhyeon.StageOneSnowTheme import StageOneSnowTheme
from main.gilhyeon.StageTwoTheme import StageTwoSnowTheme
from main.gilhyeon.FirstToSecond import FirstToSecond

a = StageOneSnowTheme()
stageOne = 0

b = StageTwoSnowTheme()

c = FirstToSecond()


if(a.run()==1):
    print("1 스테이지 클리어")

if(c.run()==1):
    print("2 스테이지 시작")

if(b.run()==1):
    print("2 스테이지 클리어")