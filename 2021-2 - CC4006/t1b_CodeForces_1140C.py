# [Nyveon]
# Tarea 1 Ejercicio 2
# B - Playlist
# EL PODER DE PAITON

import sys
import heapq

# Data type: Song
'''
class Song:
    def __init__(self, length, beauty):
        self.length = length
        self.beauty = beauty

    def __repr__(self):
        return "<L:" + str(self.length) + " B:" + str(self.beauty) + ">"

    def __lt__(self, other):
        return self.length > other.length
'''

# Input
line = sys.stdin.readline()
nk = [int(x) for x in line.split()]
n = nk[0]
k = nk[1]

songs = []
for i in range(n):
    line = sys.stdin.readline()
    lb = [int(x) for x in line.split()]
    #this_song = Song(int(lb[0]), int(lb[1]))
    this_song = (int(lb[0]), int(lb[1]))
    songs.append(this_song)


# Sort arrays
songs.sort(key = lambda x: -x[1]) # reverse sort
#print(songs)

#songset = set()
songheap = []
length_sum = 0
subjective_value = 0

for i in range(n):
    this_song = songs[i]
    #songset.add(this_song)
    length_sum += this_song[0]
    heapq.heappush(songheap, this_song)

    if len(songheap) > k:
        current = heapq.heappop(songheap)
        length_sum -= current[0]

    subjective_value = max((this_song[1] * length_sum), subjective_value)

print(subjective_value)
