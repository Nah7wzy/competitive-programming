class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        for hour in range(12):
            for minute in range(60):
                hour_bit_count, minute_bit_count = hour.bit_count(), minute.bit_count()
                if hour_bit_count + minute_bit_count == turnedOn:
                    res.append(str(hour) + ':' + (str(minute) if minute >= 10 else f'0{minute}'))
        return res