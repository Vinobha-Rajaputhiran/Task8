#Task: Part - B
#Inherit a TV class add additional properties like screen thickness, energy usage , Lifespan , Refresh rate , functionalities like viewingAngle , Backlight, DisplayDetails , which displays the detailed features of the TV
#Multiple Inheritance is used here
class TV:# Parent Class
    def __init__(self, brand, OnOFF_status, channel, volume):
        self.price = 1500
        self.inches = 23
        self.channel=channel
        self.volume=volume
        self.brand = brand
        self.OnOFF_status= OnOFF_status

    def volume_change(self, value):
        if value<=100:
            self.volume=value
        elif value>self.volume:
            pass
        print("The current volume is", self.volume)

    def channel_change(self,value):
        if value<=50:
            self.channel=value
        elif value>self.channel:
            pass
        print("The current channel is", self.channel)

    def reset_settings(self):
        self.channel=1
        self.volume=50

    def status(self):
        print(self.brand, "at channel", self.channel, "and at volume",  self.volume)

set1=TV("Panasonic","On", 1,50)#Objects defined with default parameters
set2=TV("Samsung","On", 1,50)

class plasma(TV):#Child Class One
    def __init__(self, channel, volume, brand):
        self.screen='Wide'
        self.thickness= 24
        self.energy_usage='High'
        self.Lifespan= 'Low'
        self.Refresh_rate= 'Slow'
        self.viewingAngle= 90
        self.Backlight= 'ON'
        self.channel = channel
        self.volume = volume
        self.brand = brand

    def DisplayDetails1(self):
        print("Volume:", self.volume, "Channel: ",self.channel, "Screen: ", self.screen, "Thickness: ", self.thickness, "Energy: ", self.energy_usage, "Lifespan: ", self.Lifespan, "Refresh_rate: ", self.Refresh_rate, "viewingAngle", self.viewingAngle, "Backlight: ", self.Backlight)


class LED(TV):#Child Class Two
    def __init__(self, channel, volume, brand):
        self.screen='Flat'
        self.thickness= 32
        self.energy_usage='Low'
        self.Lifespan= 'High'
        self.Refresh_rate= 'Fast'
        self.viewingAngle= 180
        self.Backlight= 'OFF'
        self.channel = channel
        self.volume = volume
        self.brand = brand

    def DisplayDetails2(self):
        print("Volume:", self.volume, "Channel: ",self.channel, "Screen: ", self.screen, "Thickness: ", self.thickness, "Energy: ", self.energy_usage, "Lifespan: ", self.Lifespan, "Refresh_rate: ", self.Refresh_rate, "viewingAngle", self.viewingAngle, "Backlight: ", self.Backlight)
#The Methods from parent class is called as below:
plasma1= plasma(23,5,'LG')
plasma1.channel_change(12)
plasma1.volume_change(150)
plasma1.status()
plasma1.DisplayDetails1()
print()#Line Break for viewing purposes
LED1=LED(65, 77,'OnePlus')
LED1.volume_change(12)
LED1.channel_change(43)
LED1.status()
LED1.DisplayDetails2()
