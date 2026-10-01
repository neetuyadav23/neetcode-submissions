class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j,maxx,ll=0,0,0,0
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

        return maxx

        