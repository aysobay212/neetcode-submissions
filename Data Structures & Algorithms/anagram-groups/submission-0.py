class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
     # encode each string in strs into a 26 length array
        encoded_array = []
        for word in strs:
            encoded_word = [0 for _ in range(0, 26)] # array of size 26
            for char in word:
                encoded_word[ord(char) - ord("a")] += 1
            encoded_array.append(encoded_word)

        # we have a 1-to-1 correspondence between strs and encoded_word
        # convert the encodings into a hashmap

        hashmap = {}
        counter = 0
        for encodings in encoded_array:
            if f"{encodings}" not in hashmap:
                hashmap[f"{encodings}"] = counter
                counter += 1

        # create array of arrays of size counter
        output_array = [[] for _ in range(0, counter)]
        for index, word in enumerate(strs):
            output_array[hashmap[f"{encoded_array[index]}"]].append(word)
        return output_array