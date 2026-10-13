class Solution:

    def encode(self, strs: List[str]) -> str:
        cypher_text = ''
        for s in strs:
            l=len(s)
            cypher_text+='|'+str(l)+'|'
            cypher_text+=s
        print(cypher_text)
        return cypher_text


    def decode(self, s: str) -> List[str]:
        if len(s)==0:
            return []
        if len(s)==3:
            return [""]
        i=0
        strs = []
        len_start_pos = -1
        len_end_pos = -1
        reading_length = False
        while i<len(s):
            if s[i]=="|":
                print("Delimiter found at "+str(i)+":"+s[i])
                if not reading_length:
                    print("Opening length at:"+str(i))
                    reading_length=True
                    len_start_pos=i+1
                    i+=1
                    continue
                else:
                    print("closing length at:"+str(i))
                    reading_length=False
                    len_end_pos=i
                    sl = int(s[len_start_pos:len_end_pos])
                    print("length found:"+str(sl))
                    if sl==0:
                        curr_str=""
                        i+=1
                    else:
                        start = i+1
                        end = start+sl   
                        curr_str = s[start:end]
                        i=end
                    strs.append(curr_str)
                    continue
            else:
                i=i+1
        return strs
