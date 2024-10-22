class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # 3 Cases
        while tx >= sx and ty >= sy:

            if ty == sy and tx == sx:
                return True

            if ty > tx:
                if tx == sx:
                    return (ty - sy) % tx == 0
                ty %= tx

            else:
                if ty == sy:
                    return (tx - sx) % ty == 0
                tx %= ty   

        return False             