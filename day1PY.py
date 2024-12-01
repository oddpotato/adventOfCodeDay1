import csv

class DayOne:

    def __init__(self):
        self.day1List1 = []
        self.day1List2 = []

    def part1(self):
        with open('input.csv', 'r') as file:
            input = csv.reader(file)
            for row in input:
                rowArr = row[0].split('   ')
                self.day1List1.append(int(rowArr[0]))
                self.day1List2.append(int(rowArr[1]))
        self.day1List1.sort()
        self.day1List2.sort()
        result = list(map(lambda x, y: abs(x - y), self.day1List1, self.day1List2))
        return sum(result)

newDay = DayOne().part1()