class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        cnt=0
        for i in range(len(items)):
            if (ruleKey=='color') and (items[i][1]==ruleValue):
                cnt+=1
            elif (ruleKey=='type') and (items[i][0]==ruleValue):
                cnt+=1
            elif (ruleKey=='name') and (items[i][2]==ruleValue):
                cnt+=1
        return cnt