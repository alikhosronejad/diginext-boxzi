from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)
    
    for s in strs:
        # Sort the string and use it as a key
        key = ''.join(sorted(s))
        anagrams[key].append(s)
    
    # Return the values of the dictionary which are the grouped anagrams
    return list(anagrams.values())

# Example usage:
input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = group_anagrams(input_strs)
print(output)  # Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
