
import math
import turtle

class SolarSys:
    def __init__(self, width, height):
        self.center = None
        self.planets = []
        self.ssturtle = turtle.Turtle()
        self.ssturtle.hideturtle()
        self.ssscreen = turtle.Screen()
        self.ssscreen.setworldcoordinates(-width/2.0, -height/2.0, width/2.0, height/2.0)
        self.ssscreen.tracer(50)

    def addPlanet(self, aplanet):
        aelf.planets.append(aplanet)

    def addCenter(self, acen):
        self.center = acen

    def showPlanets(self):
        for aplanet in self.planets:
            print(aplanet)

    def freeze(self):
        self.ssscreen.exitonclick()

    def movePlanets(self):
        G = 0.1
        dt = 0.001

        for p in self.planets:
            p.moveTo(p.getPosx() + dt * p.getVelx(), p.getPosy() + dt * p.getVely())

            rx = self.center.getPosx() - p.getPosx()
            ry = self.center.getPosy() - p.getPosy()
            r = math.sqrt(rx**2 + ry**2)

            accx = G * self.center.getMass() * rx/r**3
            accy = G * self.center.getMass() * ry/r**3

            p.setVelx(p.getVelx() + dt * accx)
            p.setVely(p.getVely() + dt * accy)


class Center:
    def __init__(self, crad, cm):
        self.radius = crad
        self.mass = cm
        self.x = 0
        self.y = 0

        self.sturtle = turtle.Turtle()
        self.sturtle.shape("circle")
        self.sturtle.color("red")

    def getRadius(self):
        return self.radius

    def getMass(self):
        return self.mass

    def getXPos(self):
        return self.x

    def getYPos(self):
        return self.y


class Planet:
    def __init__(self, pdist, prad, pm, pvx, pvy, pc):
        self.distance = pdist
        self.radius = prad
        self.mass = pm
        self.velx = pvx
        self.vely = pvy
        self.color = pc
        self.x = pdist
        self.y = 0

        self.pturtle = turtle.Turtle()
        self.pturtle.up()
        self.pturtle.color(self.color)
        self.pturtle.shape("circle")
        self.goto(self.x,self.y)
        self.pturtle.down()

    def getDistance(self):
        return self.distance

    def getRadius(self):
        return self.radius

    def getMass(self):
        return self.mass

    def getVelx(self):
        return self.velx

    def getVely(self):
        return self.vely

    def getPosx(self):
        return self.x

    def getposy(self):
        return self.y


    def moveTo(self, newx, newy):
        self.x = newx
        self.y = newy
        self.pturtle.goto(newx, newy)

    def setVelx(self):
        self.velx = newx

    def setVely(self):
        self.vely = newy






def createSSandAnimate():
    ss = SolarSys(2,2)

    cent = Center(20, 1000)
    ss.addCenter(cent)

    m = Planet(2, 1, 500, 0, 2, "black")
    ss.addPlanet(m)

    timePeriods = 1000
    
    for amove in range(timePeriods):
        ss.movePlanets()


    ss.freeze()

createSSandAnimate()





























