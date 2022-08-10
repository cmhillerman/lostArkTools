

import os
import pprint
from re import I, sub
from tracemalloc import start

from pip import main


def calcNumGemsToFuse(startingGemLevel, fusedGemLevel):
    return 3**(fusedGemLevel-startingGemLevel)

if __name__ == '__main__':

    levelPrice = dict()

    with open("gems.data", 'r') as f:
        f.readline()
        for line in f: 
            level, coolDownPrice, atkPrice = line.split(' ')
            
            levelPrice[int(level)] = (int(coolDownPrice), int(atkPrice))

    data = dict()
    print("{: >22}{: >22}{: >22}{: >22}{: >22}{: >22}{: >22}{: >22}".format("Starting Level", "Fused Gem Level", 
        "Cool: Starting Price", "Cool: Fuse Price", "Cool: Profit", 
        "Atk: Starting Price", "Atk: Fuse Price", "Atk: Profit"))
    for startingGemLevel, startingPrices in levelPrice.items():
        startingCoolDownGemPrice, startingAtkGemPrice = startingPrices
        for fusedGemLevel in range(startingGemLevel+1, 11):
            numGemsToFuse = calcNumGemsToFuse(startingGemLevel, fusedGemLevel)

            coolDownPriceToFuse = numGemsToFuse*startingCoolDownGemPrice
            atkPriceToFuse = numGemsToFuse*startingAtkGemPrice

            coolDownProfit = levelPrice[fusedGemLevel][0] - coolDownPriceToFuse
            atkProfit = levelPrice[fusedGemLevel][1] - atkPriceToFuse

            print("{: >22}{: >22}{: >22}{: >22}{: >22}{: >22}{: >22}{: >2}".format(startingGemLevel, fusedGemLevel, 
                startingCoolDownGemPrice, coolDownPriceToFuse, coolDownProfit, 
                startingAtkGemPrice, atkPriceToFuse, atkProfit))



