class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        from datetime import datetime
        date_object1 = datetime.strptime(date1, "%Y-%m-%d")
        date_object2 = datetime.strptime(date2, "%Y-%m-%d")
        difference = date_object2 - date_object1
        return abs(difference.days)
