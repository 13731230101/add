class Watercup:
    __gaodu= ""
    __rongji= ""
    __yanse= ""
    __caizhi= ""

    def setgaodu(self,gaodu):
        if gaodu > 30 or gaodu < 5:
            print("你这不叫水杯")
        else:
            self.__gaodu = gaodu
    def geigaodu(self):
        return self.__gaodu


    def setrongji(self,rongji):
        if rongji >500 or rongji < 0:
            print("你这不叫水杯")
        else:
            self.__rongji= rongji
    def getrongji(self):
        return self.__rongji


    def setyanse(self,yanse):
        if yanse=="":
            print("你这颜色还挺好看")
        else:self.__yanse=yanse
    def getyanse(self):
        return self.__yanse


    def setcaizhi(self,caizhi):
        if caizhi=="":
            print("你这质量挺好")
        else:self.__caizhi=caizhi
    def getcaizhi(self):
        return self.__caizhi


    def cunshui(self,shuliang):
        print(self,"这个水杯还有",self.__rongji,"的水")

    def shuibei(self):
        print("这个高度",self.__gaodu,"厘米",self.__caizhi,"材质的，",self.__yanse,"的水杯可以装",self.__rongji,"的水")




p=Watercup()

p.setrongji(450)
p.setcaizhi("不锈钢")
p.setyanse("黑色")
p.setgaodu(30)





print(p.shuibei)

p.shuibei()