class Jet:

  def _init_(self,jetEngineSizeInput,jetbodycolorInput,wingspansizeInput,jetframeTypeInput,isjet):
    self.jetEngine=jetEngineSizeInput
    self.jetbodycolor=jetbodycolorInput
    self.jetWingspan=wingspansizeInput
    self.jetframe=jetframeTypeInput
    self.jet=isjet


  def fly(self):
    print("Feel that wind!")

  def speedup(self):
    print("FASTER! FASTER")

  def falling(self):
    print("WE ARE ALL GOING TO DIE!!!")

  def turn(self,turnDirection):
   print("your turning"+turnDirection)

RussJet=Jet()
NicholasJet=Jet(200,"gray",150,"rough",True) 




print(NicholasJet.jetEngine)
NicholasJet.fly()
NicholasJet.speedup()
NicholasJet.falling()
NicholasJet.turn("right")

#class Car:

  #Constructor Method
#  def _init_(self,engineSizeInput,bodycolorInput,wheelSizeInput,frameTypeInput,isTruck):
#    self.engine=engineSizeInput
#    self.bodyColor=bodycolorInput
#    self.wheelSize=wheelSizeInput
#    self.frame=frameTypeInput
#    self.truck=isTruck