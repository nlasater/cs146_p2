
from heapq import heappop, heappush
import math


def find_path (source_point, destination_point, mesh):
    """
    Searches for a path from source_point to destination_point through the mesh

    Args:
        source_point: starting point of the pathfinder
        destination_point: the ultimate goal the pathfinder must reach
        mesh: pathway constraints the path adheres to
    Returns:
        A path (list of points) from source_point to destination_point if exists
        A list of boxes explored by the algorithm
    """
    path = []
    boxes = {}
    source_box = None;
    dest_box = None;

    print("Destination point: ")
    print(destination_point)

    print("Source point: ")
    print(source_point)

    ## find location of src and dest point
    for element in mesh['boxes']:
 #     if int(element[0]) < source_point[1] and int(element[1]) > source_point[1] and int(element[2]) < source_point[0] and int(element[3]) > source_point[0]:
 #       source_box = element
 #       print("We found the src in box: " + str(source_box))
        
 #     if int(element[0]) < destination_point[1] and int(element[1]) > destination_point[1] and int(element[2]) < destination_point[0] and int(element[3]) > destination_point[0]:
 #       dest_box = element
 #       print("We found the dest in box: " + str(dest_box))    for element in mesh['boxes']:

        if int(element[0]) < source_point[0] and int(element[1]) > source_point[0] and int(element[2]) < source_point[1] and int(element[3]) > source_point[1]:
            source_box = element
            #print("We found the src in box: " + str(source_box))

        if int(element[0]) < destination_point[0] and int(element[1]) > destination_point[0] and int(element[2]) < destination_point[1] and int(element[3]) > destination_point[1]:
            dest_box = element
            #print("We found the dest in box: " + str(dest_box))


    queue = []
    visited = []
    detail_points = {}
    path = []

    dist = {}
    prev = {}

    for square in mesh['boxes']:
        dist[square] = math.inf
        prev[square] = None

    dist[source_box] = 0
    detail_points[source_box] = (source_point[1],source_point[0])
    detail_points[dest_box] = (destination_point[1],destination_point[0])
    heappush(queue,(0,source_box))

    while(queue):
        node = heappop(queue)
        box = node[1]

        if box == dest_box:
            print("Path exists!")
        else:
            # show we visited this node
            visited.append(box)

        # now look for neighboors and add to queue
        for neighboor in mesh['adj'][box]:
            y = (int(neighboor[1]) + int(neighboor[0])) / 2
            x = (int(neighboor[3]) + int(neighboor[2])) / 2
            detail_points[neighboor] = (x,y)

            heuristic = math.sqrt((detail_points[dest_box][1] - detail_points[neighboor][1])**2 + (detail_points[dest_box][0] - detail_points[neighboor][0])**2)
            alt = math.sqrt((detail_points[source_box][1] - detail_points[neighboor][1])**2 + (detail_points[source_box][0] - detail_points[neighboor][0])**2)
            if dist[neighboor] > alt + heuristic:
                if neighboor not in visited and dist[neighboor] == math.inf:
                    heappush(queue,(alt + heuristic, neighboor))
                dist[neighboor] = alt
                prev[neighboor] = box

        #print(len(queue))
        #print(queue)

    if dist[dest_box] == math.inf:
        print("No path found")
        return None
    else:
        print("entered?")
        shortpath = []
        #oshortpath = []
        shortpath.append(box)
        #oshortpath.append(detail_points[box])
        w = box
        while dist[w] != 0:
            print(prev[w])
            shortpath.append(prev[w])
            #oshortpath.append(detail_points[w])
            w = prev[w]
        shortpath.reverse()
        #oshortpath.reverse()
        print(shortpath)
        print()
        #print(oshortpath)
        print()
        return shortpath, visited