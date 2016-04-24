from utilities import *

def flood(color_of_tile, flooded_list, screen_size):
    for i in flooded_list:
        for j in up(i), down(i), left(i), right(i):
            if in_bounds(j,screen_size) and j not in flooded_list:
                if color_of_tile[j] == color_of_tile[flooded_list[0]]:
                    flooded_list.append(j)