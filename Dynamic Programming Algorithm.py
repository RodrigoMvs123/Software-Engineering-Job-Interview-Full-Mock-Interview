
def find_longest_substring(stringa, stringb, idxa=0, idxb=0, memo=None): 
                if memo is None: memo = [[-1]  * len(stringb)] * len(stringa)    
                if idxa == len(stringa) or idxb == len(stringb): return 0 
                if memo [idxa] [idxb] != -1 : return memo [idxa] [idxb] 
      possibility_1 = find_longest_substring(stringa, stringb, idxa+1, idxb) 
      possibility_2 find_longest_substring(stringa, stringb, idxa, idxb+1) 
                if stringa [idxa] == stringb [idxb]: 
      possibility_3 = find_longest_substring(stringa, stringb, idxa+1, idxb+1) 
                    +1 

           memo [idxa] [idxb] = max(possi_1, possi_2, possi_3 if applicable) 

           return memo [idxa] [idxb] 
