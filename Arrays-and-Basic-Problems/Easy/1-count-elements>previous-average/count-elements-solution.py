# Count the number of times a response time exceeds the average of all previous response times.

def countResponseTimeRegressions(responseTimes):
    count = 0

    if not responseTimes or len(responseTimes) == 1:
        print(f"The total count: {count}")
        return count
    
    for index, item in enumerate(responseTimes):
        total, average = 0, 0
        if index == 0:
            continue
        for j in range(index):
            total += responseTimes[j]
        average = total / index
        
        if item > average:
            count += 1
    print(f"The total count: {count}")
    return count

if __name__ == '__main__':
    countResponseTimeRegressions([100, 200, 150, 300])
    countResponseTimeRegressions([100, 200, -5, 0, 800, 5, 6])
    countResponseTimeRegressions([])
    countResponseTimeRegressions([50])