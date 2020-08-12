class Solution:
    def getRow(self, rowIndex: int):
        index = 0
        result = []

        while rowIndex >= index:
            result = self.calculateLine(index, result)
            index += 1

        return result


    def calculateLine(self, row, result):
        if row == 0:
            return [1]

        elif row == 1:
            return [1,1]

        else:
            old_result = result
            result = [1]
            for i in range(len(old_result)):
                try:
                    result.append(old_result[i] + old_result[i+1])
                except:
                    break
            result.append(1)
        
        return result
                
            

ans = Solution()
row = ans.getRow(3)      
print(row)