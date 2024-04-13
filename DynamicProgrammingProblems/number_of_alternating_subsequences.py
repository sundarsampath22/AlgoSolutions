#given a binary string, how many subsequences of length 3 can you form with the stipulation that no two consecutive characters in each subsequence can be the same (i.e alternating 1s and 0s)
class Solution:
    def numberOfWays(self, s: str) -> int:
        offices = []
        restaurants = []
        for i,c in enumerate(s):
            if c == '0':
                offices.append(i)
            else:
                restaurants.append(i)
        positionsHmap = {}
        recent1 = len(restaurants)
        recent0 = len(offices)
        for i in range(len(s) - 1, -1, -1):
            curChar = s[i]
            if curChar == '1':
                recent1 -= 1
                positionsHmap[i] = recent0
            else:
                recent0 -= 1
                positionsHmap[i] = recent1
        res = 0
        restaurantPrefixSum = [0 for _ in range(len(restaurants)+1)]
        officePrefixSum = [0 for _ in range(len(offices)+ 1)]  

        for i in range(0, len(restaurants)):
            nextRestaurant = restaurants[i]
            nextOfficeIndex = positionsHmap[nextRestaurant]
            restaurantPrefixSum[i+1] = restaurantPrefixSum[i] + (len(offices) - nextOfficeIndex)
        
        for i in range(0, len(offices)):
            nextOffice = offices[i]
            nextRestaurantIndex = positionsHmap[nextOffice]
            officePrefixSum[i+1] = officePrefixSum[i] + (len(restaurants) - nextRestaurantIndex)

        for office in offices:
            nextRestaurantIndex = positionsHmap[office]
            res += restaurantPrefixSum[-1] - restaurantPrefixSum[nextRestaurantIndex]
                
        for restaurant in restaurants:
            nextOfficeIndex = positionsHmap[restaurant]
            res += officePrefixSum[-1] - officePrefixSum[nextOfficeIndex]

        return res