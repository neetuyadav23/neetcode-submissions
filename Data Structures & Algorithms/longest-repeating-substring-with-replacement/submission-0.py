class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # TC = O(N) and SC = O(M)
        i,j,ll=0,0,0
        mpp={}

        while j < len(s):        # takes O(N)
            if s[j] not in mpp:
                mpp[s[j]]=1
            else:
                mpp[s[j]]+=1

            while ( (j-i+1) - max(mpp.values())) > k:   # takes O(N)
                mpp[s[i]]-=1                            # so total O(2N)=O(N)
                #if mpp[s[i]]==0:
                    #del mpp[s[i]]
                i+=1
            
            j+=1
            # after j += 1,j is pointing to the next character 
            # which is outside the current window, hence j-i 
            # OR you can calculate ll first then increment j
            ll=max(ll,j-i)
        return ll          