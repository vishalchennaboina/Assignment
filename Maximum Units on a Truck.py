def maximumUnits(boxTypes, truckSize):
    boxTypes.sort(key=lambda x: x[1], reverse=True)
    total_units = 0
    
    for boxes, units in boxTypes:
        if truckSize <= 0:
            break
        boxes_to_take = min(boxes, truckSize)
        total_units += boxes_to_take * units
        truckSize -= boxes_to_take
    
    return total_units

#Example-1
print(maximumUnits([[1,3],[2,2],[3,1]], 4))

#Example-2
print(maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10))