"""
--- Day 3: Crossed Wires ---

The gravity assist was successful, and you're well on your way to the Venus refuelling station. During the rush back on Earth, the fuel management system wasn't completely installed, so that's next on the priority list.

Opening the front panel reveals a jumble of wires. Specifically, two wires are connected to a central port and extend outward on a grid. You trace the path each wire takes as it leaves the central port, one wire per line of text (your puzzle input).

The wires twist and turn, but the two wires occasionally cross paths. To fix the circuit, you need to find the intersection point closest to the central port. Because the wires are on a grid, use the Manhattan distance for this measurement. While the wires do technically cross right at the central port where they both start, this point does not count, nor does a wire count as crossing with itself.

For example, if the first wire's path is R8,U5,L5,D3, then starting from the central port (o), it goes right 8, up 5, left 5, and finally down 3:

...........
...........
...........
....+----+.
....|....|.
....|....|.
....|....|.
.........|.
.o-------+.
...........

Then, if the second wire's path is U7,R6,D4,L4, it goes up 7, right 6, down 4, and left 4:

...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........

These wires cross at two locations (marked X), but the lower-left one is closer to the central port: its distance is 3 + 3 = 6.

Here are a few more examples:

    R75,D30,R83,U83,L12,D49,R71,U7,L72
    U62,R66,U55,R34,D71,R55,D58,R83 = distance 159
    R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
    U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135

What is the Manhattan distance from the central port to the closest intersection?

--- Part Two ---

It turns out that this circuit is very timing-sensitive; you actually need to minimize the signal delay.

To do this, calculate the number of steps each wire takes to reach each intersection; choose the intersection where the sum of both wires' steps is lowest. If a wire visits a position on the grid multiple times, use the steps value from the first time it visits that position when calculating the total value of a specific intersection.

The number of steps a wire takes is the total number of grid squares the wire has entered to get to that location, including the intersection being considered. Again consider the example from above:

...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........

In the above example, the intersection closest to the central port is reached after 8+5+5+2 = 20 steps by the first wire and 7+6+4+3 = 20 steps by the second wire for a total of 20+20 = 40 steps.

However, the top-right intersection is better: the first wire takes only 8+5+2 = 15 and the second wire takes only 7+6+2 = 15, a total of 15+15 = 30 steps.

Here are the best steps for the extra examples from above:

    R75,D30,R83,U83,L12,D49,R71,U7,L72
    U62,R66,U55,R34,D71,R55,D58,R83 = 610 steps
    R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
    U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = 410 steps

What is the fewest combined steps the wires must take to reach an intersection?

"""
import sys
import re

def get_wire_paths(path):
    with open(path) as f:
        wires = []
        for l in f.readlines():
            wires.append(l.split(','))
        return wires

def parse_segment(seg_str):
    m = re.match(r'(\w)(\d+)', seg_str)
    return m.group(1), int(m.group(2))

def get_path(wire):
    dist_from_origin = {}
    current = (0,0)
    wire_distance = 0
    for segment in wire:
        direction, count = parse_segment(segment)
        for _ in range(count):
            if direction == 'U':
                current = (current[0]+1, current[1])
            if direction == 'D':
                current = (current[0]-1, current[1])
            if direction == 'L':
                current = (current[0], current[1]-1)
            if direction == 'R':
                current = (current[0], current[1]+1)
            
            wire_distance += 1

            if current in dist_from_origin:
                dist_from_origin[current] = min(dist_from_origin[current], wire_distance)
            else:
                dist_from_origin[current] = wire_distance
    return dist_from_origin


def manhattan(coord):
    """
    Manhattan distance for Part 1
    """
    return abs(coord[0]) + abs(coord[1])

def total_path(coord, m1, m2):
    """
    Minimum cumulative path distance for a given manhattan intersection for Part 2
    """
    return m1[coord] + m2[coord]

def find_min_intersection(wires):
    coords_1, coords_2 = get_path(wires[0]), get_path(wires[1])
    intersections = coords_1.keys() & coords_2.keys()
    min_dist_p1 = manhattan(min(intersections, key= lambda p: manhattan(p)))
    min_dist_p2 = total_path(
        min(intersections, key= lambda p: total_path(p, coords_1, coords_2)),
        coords_1, coords_2)
    return min_dist_p1, min_dist_p2

if __name__ == "__main__":
    wires = get_wire_paths(sys.argv[1])
    pt_1_sol, pt_2_sol = find_min_intersection(wires)
    print("Part 1: {}\nPart 2: {}".format(pt_1_sol, pt_2_sol))