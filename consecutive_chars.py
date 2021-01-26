# https://leetcode.com/problems/consecutive-characters/

class Solution:
    def maxPower(self, s: str) -> int:
        count = 1
        current_max = 1
        current_letter = s[0]
        for letter in s[1:]:
            if(letter == current_letter):
                count += 1
            else:
                count = 1
                current_letter = letter
            current_max = max(current_max, count) 
        return current_max

if __name__ == "__main__":
    sol = Solution()
    # inp_str = "leetcodeeeeeee"
    inp_str = "abbcccddddeeeeedcba"
    inp_str = "triplepillooooow"
    inp_str = "hooraaaaaaaaaaay"
    inp_str = "tourist"
    #inp_str = "" # not supported as it's not required
    inp_str = 'eihlergvuyeuukndgkqkvnkhhohtqwvmgppcgtsopvrcdigbupxdffnhbqbrkxuggyvtnnsnutxfcnnvwuvkgfqkbgdvwuycvnlxyllbxalslvckaelyxovfrxouyfkmqmpinwubadqrqkblyolkgybdywyiiypqbwhqqucvvwhunmuahxcpvhnvvpfxlbamlyshixtysiciplumtyrsomcoesnmergagtnacvattmmbulpnmtapjtuidqmrtphtflknfmiesfqvijlcusnesexlwrqdonhnwcmxgauhuemixylvjsygaitdmyuwkvhsmngvddimligipclagrgveckvflpemdxulyclafbxymoskjupaxkncmnitfwhkyjrmjhqgixcqlcbjcftkvmerlmxpfdpwifgnrdxtrmfdegdqexugguvfiqegmlvluwlgvokehowevedqwtltdrxemxhujtwidpxngbdudkimbhnajecayem'
    inp_str = 'j'
    res = sol.maxPower(inp_str)
    print(res)
        
