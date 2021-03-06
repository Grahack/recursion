"""List all of the series' of letters (non-dictionary words,
'asd' and 'w' count) that can be formed with some scrabble tiles
on a blank board. (In scrabble, you don't have to use all your
tiles at once) (permutations of combinations)"""

from permutations import permutations
import itertools

def perm_of_comb(s):
    ret = []
    for i in range(1, len(s) + 1):
        ret.extend(permutations(s, i))

    return ret

print sorted(perm_of_comb("")) # no '' returned because range starts at 1 and only 0 makes ''
print sorted(perm_of_comb("a"))
print sorted(perm_of_comb("abc"))
