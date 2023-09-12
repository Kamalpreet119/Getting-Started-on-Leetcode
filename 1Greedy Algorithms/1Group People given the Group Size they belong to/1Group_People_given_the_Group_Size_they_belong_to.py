class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """
        dict1={}

        #Grouping People whose Team Size is Same
        for i in range(len(groupSizes)):
            if groupSizes[i] in dict1.keys():
                dict1[groupSizes[i]].append(i)
            else:
                dict1[groupSizes[i]]=[i]
        #print(dict1)

        ans=[]

        #Putting people with same number of Team Members in one Group Till needed Number of members are achieved
        for i in dict1.keys():
            count=1
            agroup=[]
            while(count<=i):
                person=dict1[i].pop()
                agroup.append(person)
                count+=1
            ans.append(agroup)
            while(len(dict1[i])!=0):
                count=1
                agroup=[]
                while(count<=i):
                    person=dict1[i].pop()
                    agroup.append(person)
                    count+=1
                ans.append(agroup)
        #print(ans)
        return ans