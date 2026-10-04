class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # TC: O(n*m) for dict comparison, but m <= 26 
        # (fixed lowercase alphabet), so O(n*26) = O(n).
        # Space: O(m) → O(1) because m ≤ 26

        # Instead of comparing entire dictionaries, we could maintain a        
        # match/count variable (or fixed-size frequency arrays) and 
        # update it as the window slides.-----the tc however would be SAME
        k=len(s1)
        i,j=0,0
        mpp={}
        mpp2={}

        for char in s1:
            if char not in mpp:
                mpp[char]=1
            else:
                mpp[char]+=1

        while j < len(s2):
            size=j-i+1
            
            if s2[j] not in mpp2:
                mpp2[s2[j]]=1
            else:
                mpp2[s2[j]]+=1

            if size == k:
                if mpp==mpp2:
                    return True
                else:
                    mpp2[s2[i]]-=1
                    if mpp2[s2[i]]==0:
                        del mpp2[s2[i]]
                    i+=1
            
            j+=1

        return False
        