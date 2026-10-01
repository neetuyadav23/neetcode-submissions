class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j=0,0
        maxx=0
        sset=set()

        while j < len(s):
            sset.add(s[j])
            size=j-i+1

            if len(sset) != size:
                while s[j] in sset:
                    sset.remove(s[i]) # ❌ KeyError if s[i] doesn't exist
                    # sset.discard(s[i])   # ✅ does nothing if s[i] doesn't exist
                    i+=1
            
                sset.add(s[j])
            
            j+=1
            maxx=max(maxx,len(sset))
        return maxx

        # brute is O(N^2) using nested loops -- Generate every substring
        '''maxx=0
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                substr=s[i:j+1]

                if len(substr)==len(set(substr)):
                    ll=len(substr)

                maxx=max(maxx,ll)

        return maxx'''

        # this is optimal code O(N)-- using variable sliding window

        '''i,j,maxx,ll=0,0,0,0
        mpp={}

        while j < len(s):
            size=j-i+1

            if s[j] not in mpp:
                mpp[s[j]]=1
            else:
                mpp[s[j]]+=1

            if len(mpp)==size:
                ll=size
            else:
                mpp[s[i]]-=1
                if mpp[s[i]]==0:
                    del mpp[s[i]]
                i+=1

            maxx=max(maxx,ll)
            j+=1

        return maxx'''

        