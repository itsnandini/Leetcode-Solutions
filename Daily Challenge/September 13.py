class Solution:
    def validUtf8(self, data: List[int], i=0) -> bool:

        def check_rem(i,total):

            return all(i<len(data) and (data[i]>>6)==0b10 for i in range(i,i+total))

        while i<len(data):

            if data[i]>>7==0: i+=1

            elif data[i]>>5==0b110 and check_rem(i+1,1): i+=2

            elif data[i]>>4==0b1110 and check_rem(i+1,2): i+=3

            elif data[i]>>3==0b11110 and check_rem(i+1,3): i+=4

            else: return False

        return True
