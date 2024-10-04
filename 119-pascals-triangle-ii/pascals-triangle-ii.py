class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]  # Start with the first element as 1
        for i in range(1, rowIndex + 1):
        # Use the previous row's element to calculate the next one
            row.append(row[-1] * (rowIndex - i + 1) // i)

        return row    