from itertools import count
from math import ceil
from typing import List
import string

class Solution:
    # math
    def convertTemperature(self, celsius: float) -> List[float]:
        Kelvin = celsius + 273.15
        Fahrenheit = celsius * 1.80 + 32.00
        return [Kelvin, Fahrenheit]

    def sum(self, num1: int, num2: int) -> int:
        return num1 + num2

    def numIdenticalPairs_1(self, nums: List[int]) -> int:
        ans = 0
        for i, item1 in enumerate(nums):
            for j, item2 in enumerate(nums):
                if item1 == item2 and i < j:
                    ans += 1
        return ans

    def smallestEvenMultiple(self, n: int) -> int:
        b = n
        if b % 2 == 0:
            ans = n
        else:
            ans = n * 2
        return ans

    def minimumSum(self, num: int) -> int:
        nums = list()
        while num > 0:
            nums.append(num % 10)
            num //= 10
        nums.sort()
        new1 = 10 * nums[0] + nums[2]
        new2 = 10 * nums[1] + nums[3]
        return new1 + new2

    def subtractProductAndSum(self, n: int) -> int:
        nums = list()
        num_sum = 0
        num_multiple = 1
        while n > 0:
            nums.append(n % 10)
            n //= 10
            nums.sort()
        for i in nums:
            num_sum += i
            num_multiple *= i
        return num_multiple - num_sum

    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + (t * 2)

    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        ans = 0
        nums = [start + n * 2 for n in range(n)]
        for num in nums:
            ans = ans ^ num
        return ans

    def sumOfMultiples(self, n: int) -> int:
        ans = 0
        for item in range(1, n + 1):
            if item % 3 == 0 or item % 5 == 0 or item % 7 == 0:
                ans += item
        return ans

    def numberOfSteps(self, num: int) -> int:
        ans = 0
        for i in range(num):
            if num % 2 == 0:
                num = num / 2
                ans += 1
                if num == 0:
                    break
            elif num % 2 != 0:
                num = num - 1
                ans += 1
                if num == 0:
                    break
        return ans

    def countDigits(self, num: int) -> int:
        ans = 0
        for i in str(num):
            if int(num) % int(i) == 0:
                ans += 1
        return ans

    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)
        digit_sum = 0
        for i in nums:
            for j in str(i):
                digit_sum += int(j)
        return abs(element_sum - digit_sum)

    def sumOddLengthSubarrays(self, arr: List[int]) -> int:  # [1, 4, 2, 5, 3]
        ans = 0
        for i in range(len(arr)):
            for j in range(i, len(arr), 2):
                ans += sum(arr[i : j + 1])
        return ans

    def numberOfMatches(self, n: int) -> int:
        ans = 0
        while n != 1:
            if n % 2 == 0:  # для четного
                ans = ans + (n / 2)
                n = n / 2
            elif n % 2 != 0:  # для нечетного
                ans = ans + (n - 1) / 2
                ans += 1
                n = (n - 1) / 2
        return int(ans)

    def maximum69Number(self, num: int) -> int:
        a = list(str(num))
        for i in range(len(a)):
            if a[i] == "6":
                a[i] = "9"
                break
        return int("".join(a))

    def pivotInteger(self, n: int) -> int:
        ans = 0
        arr1 = list()
        arr2 = arr1
        for i in range(1, n + 1):
            arr1.append(i)
        for j in range(n):
            if sum(arr1[j:]) == sum(arr2[: j + 1]):
                ans = arr1[j]
                return ans
        return -1

    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        if arrivalTime + delayedTime < 24:
            return arrivalTime + delayedTime
        else:
            return abs(24 - (arrivalTime + delayedTime))

    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        fin = 0
        for i in range(len(points) - 1):
            first = points[i]
            second = points[i + 1]
            res = [e2 - e1 for e2, e1 in zip(second, first)]
            fin += abs(max(res, key=abs))
            print(res)
        return fin

    def commonFactors(self, a: int, b: int) -> int:
        ans = 0
        for i in range(1, a + 1):
            if a % i == 0:
                if b % (i) == 0:
                    ans += 1
        return ans

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def SelfDivision(n):
            str_n = str(n)
            for el in str_n:
                if el == "0":
                    return False
                if n % int(el) != 0:
                    return False
            return True

        ans = []
        for num in range(left, right + 1):
            if SelfDivision(num):
                ans.append(num)
        return ans

    # array
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(2):
            for i in nums:
                ans.append(i)
        return ans

    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ans.append(nums[nums[i]])
        return ans

    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        # num_of_operations = int(input('Введите количество операций: '))
        # actions = [input("Введите строку: ").upper() for _ in range(num_of_operations)]
        # если раскомментировать, то функция будет принимать operations с консоли
        for i in operations:
            if i in ("X++", "++X", "x++", "++x"):
                x += 1
            elif i in ("X--", "--X", "x--", "--x"):
                x -= 1
        return x

    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[n + i])
        return ans

    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        # hours = [0,1,2,3,4], target = 2
        ans = 0
        for i in hours:
            if i >= target:
                ans += 1
        return ans

    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for i in accounts:
            summ = sum(i)
            if summ >= ans:
                ans = summ
        return ans

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # candies = [2,3,5,1,3], extraCandies = 3
        result = []
        for i in candies:
            if i + extraCandies >= max(candies):
                result.append(True)
            else:
                result.append(False)
        return result

    def countPairs(self, nums: List[int], target: int) -> int:
        #nums = [-1,1,2,3,1], target = 2
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] < target:
                    ans+=1
        return ans

    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        for i in range(1, n+1):
            result.append(sum(nums[:i]))
        return result

    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    result[i] += 1
        return result


# hash-table
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        for i in list(stones):
            if i in jewels:
                ans+=1
        return ans

    def decodeMessage(self, key: str, message: str) -> str:
        lower = string.ascii_lowercase
        key_word_list = []
        ans = ''
        for i in list(key):
            if i == ' ':
                continue
            elif i in key_word_list:
                continue
            elif i in lower:
                key_word_list.append(i)
        for i in message:
            if i == " ":
                ans+=(" ")
            else:
                ans+=(lower[key_word_list.index(i)])
        return ans

    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        using_set = set()
        ans = 0
        for num in nums:
            if num - diff in using_set and num - diff * 2 in using_set:
                ans += 1
            using_set.add(num)
        return ans

    def checkIfPangram(self, sentence: str) -> bool:
        if len(set(sentence)) < 26:
            return False
        else:
            return True

    def countKDifference(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] - nums[j] == k:
                    ans+=1
        return ans

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        lower = string.ascii_lowercase
        contain = []
        add_word = ''
        lower = list(lower)
        Morze = [".-","-...","-.-.","-..",".","..-.","--.","....", "..",".---","-.-",".-..","--",
                "-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for word in words:
            for symbol in word:
                add_word += Morze[lower.index(symbol)]
            contain.append(add_word)
            add_word = ''
            # какой же он гений, ЧТО ОН ТВОРИТ???!!!
            # уберите детей от экранов.
        return set(contain)

    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        wrong_word_num = 0
        for word in words:
            for symbol in word:
                if symbol not in allowed:
                    wrong_word_num+=1
                    break
        return len(words) - wrong_word_num

    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        ans = 0
        for i in range(len(words)):
            print(">>>", words[i])
            for j in range(len(words)):
                if i == j:
                    continue
                print(words[j][::-1])
                if words[i] == words[j][::-1]:
                    ans+=1
        return int(ans/2)

    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dock = dict(zip(heights, names))
        sorted_keys = sorted(dock, reverse=True)
        sorted_dock = {}
        for key in sorted_keys:
            sorted_dock[key] = dock[key]
        return list(sorted_dock.values())

a = Solution()



# hash-table
#print(a.sortPeople(["Mary","John","Emma"], [180,165,170]))
#print(a.maximumNumberOfStringPairs(["wk","xf","ot","je","hd","kw","fx","to","ej"]))
#print(a.countConsistentStrings("fstqyienx", ["n","eeitfns","eqqqsfs","i","feniqis","lhoa","yqyitei","sqtn","kug","z","neqqis"]))
#print(a.uniqueMorseRepresentations(["rwjje","aittjje","auyyn","lqtktn","lmjwn"]))
#print(a.numJewelsInStones("aA", "aAAbbbb"))
#print(a.decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"))
#print(a.arithmeticTriplets([0,1,4,6,7,10], 3))
#print(a.checkIfPangram("leetcode"))
#print(a.countKDifference([1,2,2,1], 1))


# array
#print(a.smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
#print(a.runningSum([1,2,3,4]))
# print(a.buildArray([0,2,1,5,3,4]))
# print(a.finalValueAfterOperations(['x--', '--x', '++x']))
# print(a.shuffle([2,5,1,3,4,7], n = 3))
# print(a.numberOfEmployeesWhoMetTarget([0, 1, 2, 3, 4], 2))
# print(a.maximumWealth([[1,2,3],[3,3,1]]))
#print(a.kidsWithCandies([2,3,5,1,3], 3))
#print(a.countPairs([-1,1,2,3,1], 2))



# math
# print(a.selfDividingNumbers(1, 22))
# print(a.commonFactors(12, 6))
# print(a.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))
# print(a.findDelayedArrivalTime(13, 11))
# print(a.pivotInteger(8))
# print(a.maximum69Number(9999))
# print(a.numberOfMatches(14))
# print(a.sumOddLengthSubarrays([1, 4, 2, 5, 3]))
# print(a.differenceOfSum([1, 15, 6, 3]))
# print(a.countDigits(121))
# print(a.numberOfSteps(8))
# print(a.sumOfMultiples(10))
# print(a.xorOperation(5, 0))
# print(a.subtractProductAndSum(4421))
# print(a.minimumSum(2932))
# print(a.smallestEvenMultiple(int(input("INPUT NUM:"))))
# print(a.numIdenticalPairs_1(nums = [1,2,3,1,1,3]))
# print(a.sum(1, 2))
# print(a.convertTemperature(36.5))
