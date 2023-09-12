class Solution(object):
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict1={}
        #Mapping Character to Frequency
        for i in s:
            if i in dict1.keys():
                dict1[i]+=1
            else:
                dict1[i]=1
        print(dict1)
        values=dict1.values()
        print(values)
        values=list(values)

        count=0
        i=0
        #Basically deleting characters until it's Frequency does not matches with that of other Characters
        #values-List Containing frequency of all characters
        #By values[:i]+values[i+1:]==>Frequency of all characters excluding current Character
        #If frequency of current character matches with other characters frequency,delete it till and update it's frequency
        #Do until it's frequency becomes unique(values[i] in lst becomes true) or character gets completely removed from the string(values[i]=0)
        for j in dict1.keys():
            lst=values[:i]+values[i+1:]
            while((values[i] in lst) and (values[i]>0)):
                count+=1
                values[i]-=1
                dict1[j]-=1
            i+=1

        print(dict1)
        print(values)
        return count