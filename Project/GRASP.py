import random
import time
from data import data



MAX_ITER = 10
INFEASIBLE = -1
LOCAL_SEARCH  = 0   # 1-FI OR 2-BI
BUSUSED = 0
ALPHA = 0


BUSES = data.get('numBuses')
DRIVERS = data.get('numDrivers')
SERVICES = data.get('numServices')
MAX_BUSES = data.get('maxBuses')
BM = data.get('BM')
CBM = data.get('CBM')
CEM = data.get('CEM')

STARTTIME = data.get('startTime')
MINUTESDURATION = data.get('minutesDuration')
KMDURATION = data.get('kmDuration')
PASSANGERS = data.get('passangers')

CAPACITY = data.get('capacity')
EUROSMIN = data.get('eurosMin')
EUROSKM = data.get('eurosKm')

MAXMINUTES = data.get('maxMinutes')



#if DEBUG:
#   import pdb


def grasp(aplha, algorthim):
    APLHA = aplha
    LOCAL_SEARCH = algorthim
    start = time.time()
    bestIter = 0
    bestSolution = []
    bestCost = 0
    B = initBuses()
    D = initDrivers()
    S = initServices()
    for i in xrange(MAX_ITER):
        B = initBuses()
        D = initDrivers()
        S = initServices()
        print "Iteration: ", i
        solB, solD = constructionPhase(B,S,D)
        if (solB == INFEASIBLE and solD == INFEASIBLE):
            continue
        bestSolB, bestSolD, bestCostB, bestCostD = localSearch(solB, solD)
        if (len(bestSolution) == 0): 
            bestIter = i
            bestSolution = bestSolB, bestSolD
            #print "cost 1st iter B: ", bestCostB
            #print "cost 1st iter D: ", bestCostD
            bestCost = bestCostB + bestCostD
        elif ( bestCostB + bestCostD < bestCost):
            bestIter = i
            bestSolution = bestSolB, bestSolD
            bestCost = bestCostB + bestCostD

    print "Best solution:  Iteration number ",  bestIter
    #for i in bestSolution:
     #   BS, DS = bestSolution[i]
      #  b,s = BS
       # d,s = DS
        #print b.idBus
        #print s.idService
        #print d.idDriver
        #print s.idService

    print "With cost: ", bestCost
    end = time.time() - start
    return end, bestCost

def constructionPhase(B,S,D):
    iterator = 0
    solutionBuses = []
    solutionDrivers = []
    sortedS = S
    count = 0

    sortedS.sort(key=lambda x: x.minutesDuration, reverse = True)
    for s in sortedS: 
        count += 1
        solutionB = []
        solutionD = []
        selectedD = 0
        selectedB = 0
        print "Service: ", count
        for b in B:
            if (b.capacity >= s.passangers):
                for serviceTime in b.emptyAt:
                    if (s.startTime + s.minutesDuration < serviceTime[0] or serviceTime[1] < s.startTime ):
                        solutionB.append((b,s))
        if (len(solutionB) == 0): 
            return (-1,-1)
        costsB = listcostsBus(solutionB)
        sb_min = min(costsB)
        print "Min Cost constructionPhase B: ", sb_min
        sb_max = max(costsB)
        print "Max Cost constructionPhase B: ", sb_max
        RCLB = []
        for sol in solutionB:
            if (costBus(sol) <= sb_min - ALPHA*(sb_max - sb_min)):
                RCLB.append(sol)
        selectedB = RCLB[random.randrange(len(RCLB))]

        for b in B:
            if (b.idBus == selectedB[0].idBus):
                b.emptyAt.append((s.startTime, s.startTime + s.minutesDuration))
                selectedB[0].emptyAt.append((s.startTime, s.startTime + s.minutesDuration))
                solutionBuses.append(selectedB)

        for d in D:
            #print "minutesWorked: ", d.minutesWorked
            if (d.minutesWorked + s.minutesDuration <= d.maxMinutes):
                #print "1"
                solutionD.append((d,s))
        if (len(solutionD) == 0): 
            return (-1,-1)
        #print "2"
        costsD = listcostsDriver(solutionD)
        sd_min = min(costsD)
        print "Min Cost constructionPhase D: ", sd_min
        sd_max = max(costsD)
        print "Max Cost constructionPhase D: ", sd_max
        RCLD = []
        for sol in solutionD:
            if (costDriver(sol) <= sb_min - ALPHA*(sb_max - sb_min)):
                RCLD.append(sol)
        selectedD = RCLD[random.randrange(len(RCLD))]
        for d in D:
            #print "D.idDriver: ", d.idDriver
            #print "selectedD id: ", selectedD[0].idDriver 
            if (d.idDriver == selectedD[0].idDriver):
                #print "Fa la suma de minutes"
                d.availableAt.append((s.startTime, s.startTime + s.minutesDuration))
                selectedD[0].availableAt.append((s.startTime, s.startTime + s.minutesDuration))
                #print "before Sum value selected", selectedD[0].minutesWorked
                #print "before Sum value s", s.minutesDuration
                #d.minutesWorked = d.minutesWorked + s.minutesDuration
                selectedD[0].minutesWorked = selectedD[0].minutesWorked + s.minutesDuration
                #print "selectedD: ", selectedD[0].minutesWorked
                solutionDrivers.append(selectedD)


        iterator = iterator + 1

    costB = costBusTotal(solutionBuses) 
    costD = costDriverTotal(solutionDrivers)
    print "Total Final Cost constructionPhase Bus: ", costB
    print "Total Final Cost constructionPhase Driver: ", costD

    return (solutionBuses, solutionDrivers)

def localSearch(solB, solD):

    best_costB = costBusTotal(solB)
    best_costD = costDriverTotal(solD)
    print "Start local Search cost: ", best_costB+best_costD
    bestSolB = 0
    bestSolD = 0
    if LOCAL_SEARCH == 1 :
        
        for x in xrange(SERVICES):
            for y in xrange(SERVICES):
                tmp_solB1 = solB[x]
                tmp_solB2 = solB[y]
                if (tmp_solB1[0].idBus != tmp_solB2[0].idBus):
                    neighbour = generateNewSolB(solB, x, y)
                    if (isFeasibleB(neighbour) and costBusTotal(neighbour) < best_costB): 
                        bestSolB = neighbour
                        best_costB = costBusTotal(neighbour)
                        break
        for x2 in xrange(SERVICES):
            for y2 in xrange(SERVICES):
                tmp_solD1 = solD[x2]
                tmp_solD2 = solD[y2]
                if (tmp_solD1[0].idDriver != tmp_solD2[0].idDriver):
                    neighbour = generateNewSolD(solD, x2, y2)
                    if (isFeasibleD(neighbour) and costDriverTotal(neighbour) < best_costD):
                        bestSolD = neighbour
                        best_costD = costDriverTotal(neighbour)
                        break
    else :
        for x in xrange(SERVICES):
            for y in xrange(SERVICES):
                tmp_solB1 = solB[x]
                tmp_solB2 = solB[y]
                if (tmp_solB1[0].idBus != tmp_solB2[0].idBus):
                    neighbour = generateNewSolB(solB, x, y)
                    if (isFeasibleB(neighbour) and costBusTotal(neighbour) < best_costB): 
                        bestSolB = neighbour
                        best_costB = costBusTotal(neighbour)
        for x2 in xrange(SERVICES):
            for y2 in xrange(SERVICES):
                tmp_solD1 = solD[x2]
                tmp_solD2 = solD[y2]
                if (tmp_solD1[0].idDriver != tmp_solD2[0].idDriver):
                    neighbour = generateNewSolD(solD, x2, y2)
                    if (isFeasibleD(neighbour) and costDriverTotal(neighbour) < best_costD):
                        bestSolD = neighbour
                        best_costD = costDriverTotal(neighbour)

    print "End localSearch Cost: ", best_costB+best_costD
    return bestSolB, bestSolD, best_costB, best_costD


def listcostsBus(solB):
    costs = []
    for i in xrange(len(solB)):
        bus, service = solB[i]
        costs.append( bus.eurosMin * service.minutesDuration + bus.eurosKm * service.kmDuration)

    return costs
    #list

def listcostsDriver(solD):
    costs = []
    for i in xrange(len(solD)):
        driver, service = solD[i]
        time = driver.minutesWorked + service.minutesDuration
        if ( time <= BM):
            costs.append(CBM * time)
            #print "minutes Driver: ", time
        else:
            costs.append(BM * CBM + CEM * (time - BM))
            #print "minutes Driver: ", time
    return costs
    #list

def costBus(solB):
    cost = 0
    bus, service = solB
    cost = cost + bus.eurosMin * service.minutesDuration + bus.eurosKm * service.kmDuration

    return cost
    #list

def costDriver(solD):
    cost = 0
    driver, service = solD
    if (driver.minutesWorked <= BM):
        cost = CBM * driver.minutesWorked
    else:
        cost = BM * CBM + CEM * (driver.minutesWorked - BM)
    return cost

def costBusTotal(solB):
    cost = 0
    for i in xrange(len(solB)):
        bus, service = solB[i]
        cost = cost + bus.eurosMin * service.minutesDuration + bus.eurosKm * service.kmDuration

    return cost
    #list

def costDriverTotal(solD):
    cost = 0
    for i in xrange(len(solD)):
        driver, service = solD[i]
        if (driver.minutesWorked <= BM):
            cost = cost + CBM * driver.minutesWorked
            #print "Minutes driver i: ", driver.minutesWorked
        else:
            cost = cost + BM * CBM + CEM * (driver.minutesWorked - BM)
            #print "Minutes driver i: ", driver.minutesWorked
    return cost
    #list

def generateNewSolB(solB, x, y):
    sol2 = solB
    busx, servicex = sol2[x]
    busy, servicey = sol2[y]
    busx.emptyAt = []
    busy.emptyAt = []

    sol2[x] = (busy, servicex)
    sol2[y] = (busx, servicey)
    return sol2

def generateNewSolD(solD, x, y):
    sol2 = solD
    driverx, servicex = sol2[x]
    drivery, servicey = sol2[y]
    driverx.availableAt = []
    driverx.minutesWorked = 0
    drivery.availableAt = []
    drivery.minutesWorked = 0

    sol2[x] = (drivery, servicex)
    sol2[y] = (driverx, servicey)
    return sol2

def isFeasibleB(solB):
    busesUsed = 0
    listBuses =[]
    for i in xrange(len(solB)):
        bus,service = solB[i]
        if (bus.capacity < service.passangers): return False
        for x in xrange(len(bus.emptyAt)):
            start, end = bus.emptyAt[x]
            serStart = service.startTime
            serEnd = service.startTime + service.minutesDuration
            if (serStart < start and start < serEnd): return False
            if (serStart < end and end < serEnd): return False
        x = (service.startTime, service.startTime + service.minutesDuration)
        bus.emptyAt.append(x)
        if (len(bus.emptyAt) > 0  and bus.idBus not in listBuses):
            listBuses.append(bus.idBus)
            busesUsed = busesUsed + 1
    return True

def isFeasibleD(solD):
    for i in xrange(len(solD)):
        driver, service = solD[i]
        if (driver.minutesWorked + service.minutesDuration > driver.maxMinutes): return False
        for x in xrange(len(driver.availableAt)):
            start, end = driver.availableAt[x]
            serStart = service.startTime
            serEnd = service.startTime + service.minutesDuration
            if (serStart < start and start < serEnd): return False
            if (serStart < end and end < serEnd): return False
        x = (service.startTime, service.startTime + service.minutesDuration)
        driver.availableAt.append(x)
        driver.minutesWorked = driver.minutesWorked + service.minutesDuration
    return True

def initBuses():
    buses = []
    for i in xrange(BUSES):
        bus = Bus(i, CAPACITY[i], EUROSMIN[i], EUROSKM[i])
        buses.append(bus)
    return buses

def initDrivers():
    drivers = []
    for i in xrange(DRIVERS):
        driver = Driver(i, MAXMINUTES[i])
        drivers.append(driver)
    return drivers

def initServices():
    services = []
    for i in xrange(SERVICES):
        service = Service(i, STARTTIME[i],MINUTESDURATION[i],KMDURATION[i], PASSANGERS[i])
        services.append(service)
    return services

class Bus:
    idBus = 0
    capacity = 0
    eurosMin = 0
    eurosKm = 0
    emptyAt= []


    def __init__(self, i,capacity, eurosMin, eurosKm): 
        self.idBus = i 
        self.capacity = capacity  
        self.eurosMin = eurosMin
        self.eurosKm = eurosKm 
        self.emptyAt.append((-1,0))

    def busUsed(x):
        self.emptyAt.append(x)

class Driver:
    idDriver = 0
    maxMinutes = 0
    minutesWorked = 0
    availableAt = []

    def __init__(self, i, maxMinutes):  
        self.idDriver = i
        self.maxMinutes = maxMinutes
        self.minutesWorked = 0
        self.availableAt.append((-1,0))

    def driverUsed(x):
        self.availableAt.append(x)

class Service:
    idService = 0
    startTime = 0
    minutesDuration = 0
    kmDuration = 0
    passangers = 0

    def __init__(self, i, startTime, minutesDuration, kmDuration, passangers):  
        self.idService = i
        self.startTime = startTime  
        self.minutesDuration = minutesDuration
        self.kmDuration = kmDuration 
        self.passangers = passangers 

if __name__ == '__main__':
    print "Starting"
    grasp()
    print "End"