class Solution:

    def encode(self, strs: List[str]) -> str:
        string = "%1%1%".join(strs)
        if len(strs)==0:
            string += "^>emptyarray"
        return string

    def decode(self, s: str) -> List[str]:
        if s.endswith("^>emptyarray"):
            return []
        arr = s.split("%1%1%")
        return arr
