
from heapq import heappop, heappush
import math


def find_path(source_point, destination_point, mesh):
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
    source_box = None
    dest_box = None

    ## find location of src and dest point
    for element in mesh['boxes']:
        if int(element[0]) < source_point[0] and int(element[1]) > source_point[0] and int(element[2]) < source_point[1] and int(element[3]) > source_point[1]:
            source_box = element

        if int(element[0]) < destination_point[0] and int(element[1]) > destination_point[0] and int(element[2]) < destination_point[1] and int(element[3]) > destination_point[1]:
            dest_box = element

    queue = []
    visited = []

#    path_exists = False
#    queue.append(source_box);
#    while(queue):
#      node = queue.pop()
#      if(node == dest_box):
#        print("Path exists!")
#        path_exists = True
#      else:
#        ## show we visited this node
#        visited.append(node)
#        ## find center of box (center isn't good but will work for this test)
#        y = node[1] - node[0]
#        x = node[3] - node[2]
#        print("(x,y): " + str(x) + ',' + str(y))
        
#        ## now look for neighboors and add to queue
#        for neighboor in mesh['adj'][node]:
#          print(str(neighboor))
#          if neighboor in visited:
#            continue
#          else:
#            queue.append(neighboor)
      
      
#    if path_exists = False:
#      print("No path possible")
#      return path, boxes.keys()

#=======
    detail_points = {}
#>>>>>>> duncan
    
    if source_box == dest_box and source_box != None:
        shortpath = []
        shortpath.append(((destination_point[0],destination_point[1]), (source_point[0], source_point[1])))
        return shortpath, visited

    dist = {}
    prev = {}

    for square in mesh['boxes']:
        dist[square] = math.inf
        prev[square] = None

    detail_points[source_box] = (source_point[1],source_point[0])
    detail_points[dest_box] = (destination_point[1],destination_point[0])
    dist[source_box] = 0
    heappush(queue,(0,source_box))

    while queue != []:
        node = heappop(queue)
        box = node[1]
        print("Source box: " + str(box))
        current_dist = node[0]

        if box == dest_box:
            print("Path exists!")
        else:
            # show we visited this node
            visited.append(box)

        # now look for neighboors and add to queue
        for neighboor in mesh['adj'][box]:
            nx = None
            ny = None

            if neighboor not in detail_points:
                max_x = max(box[2],neighboor[2])
                min_x = min(box[3],neighboor[3])
                max_y = max(box[0],neighboor[0])
                min_y = min(box[1],neighboor[1])

                if max_x <= detail_points[box][0] and detail_points[box][0] <= min_x:
                    nx = detail_points[box][0]
                elif max_x > detail_points[box][0]:
                    nx = max_x
                else:
                    nx = min_x

                if max_y <= detail_points[box][1] and detail_points[box][1] <= min_y:
                    ny = detail_points[box][1]
                elif max_y > detail_points[box][1]:
                    ny = max_y
                else:
                    ny = min_y

                detail_points[neighboor] = (nx,ny)

            heuristic = math.sqrt((detail_points[dest_box][1] - detail_points[neighboor][1])**2
                                + (detail_points[dest_box][0] - detail_points[neighboor][0])**2)
            alt = math.sqrt((detail_points[box][1] - detail_points[neighboor][1])**2
                          + (detail_points[box][0] - detail_points[neighboor][0])**2)

            if dist[neighboor] > dist[box] + alt + heuristic:
                if neighboor not in visited and dist[neighboor] == math.inf:
                    heappush(queue,(dist[box] + alt + heuristic, neighboor))
                dist[neighboor] = alt + dist[box]
                prev[neighboor] = box

    if dist[dest_box] == math.inf:
        print("No path found")
        return None
    else:
        shortpath = []
        w = dest_box
        last = prev[w]
        shortpath.append(((detail_points[last][1], detail_points[last][0]), (destination_point[0], destination_point[1])))

        while w != source_box:
            w = prev[last]
            shortpath.append(((detail_points[last][1], detail_points[last][0]), (detail_points[w][1], detail_points[w][0])))
            last = w

        shortpath.append(((detail_points[w][1], detail_points[w][0]), (source_point[0], source_point[1])))
        shortpath.reverse()
        return shortpath, visited
