class Solution:
    def distributeCandies(self, candies: int, num_people: int):
        people = [0] * num_people
        index = 0
        candy_to_give = 1
        while candies > 0:
            if index == num_people:
                index = 0
            if candies - (candy_to_give) >= 0:
                candies -= candy_to_give
                people[index] += candy_to_give
            else:
                people[index] += candies
                break
            
            index += 1
            candy_to_give += 1

        return people 

candies = 10
num_people = 3

ans = Solution()
print(ans.distributeCandies(candies = candies, num_people = num_people))
        