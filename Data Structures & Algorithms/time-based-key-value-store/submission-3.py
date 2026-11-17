class TimeMap:

    def __init__(self):
        # key: key, value: [(timestamp, value)]
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap.keys():
            self.hashmap[key] = [(timestamp, value)]
        
        else:
            # ASSUME THAT TIMESTAMPS ARE UNIQUE AND NOT DUPLICATES
            # # check if the timestamp value exists in the key
            # list_of_tuples = self.hashmap[key]
            # timestamps = [item[0] for item in list_of_tuples]
            # if timestamp in timestamps:
            #     # update the value
            #     self.hashmap[key](value, timestamp)
            # else:
            #     # append
            self.hashmap[key].append((timestamp, value))
        return
        

    def get(self, key: str, timestamp: int) -> str:
        # return smallest timestamp
        if key not in self.hashmap.keys():
            return ""
        list_of_tuples = self.hashmap[key]

        # binary search for the timestamp before `timestamp` since timestamps are strictly increasing
        l = 0
        r = len(list_of_tuples) - 1
        result = ""
        while l <= r:
            m = l + (r-l)//2
            if list_of_tuples[m][0] <= timestamp:
                result = list_of_tuples[m][1]
                l = m + 1
            else:
                r = m - 1
        return result
