class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        def find_number_of_set_bits(n):
            count=0
            while n:
                count+=n&1
                n>>=1
            return count
        
        from collections import defaultdict
        dict_bits=defaultdict(list)
        
        for i in arr:
            dict_bits[find_number_of_set_bits(i)].append(i)
        
        final_list = list()

        for key in sorted(dict_bits.keys()):
            for elem in sorted(dict_bits[key]):
                final_list.append(elem)
        return final_list
