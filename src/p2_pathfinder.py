
from heapq import heappop, heappush

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
            print("We found the src in box: " + str(source_box))

        if int(element[0]) < destination_point[0] and int(element[1]) > destination_point[0] and int(element[2]) < destination_point[1] and int(element[3]) > destination_point[1]:
            dest_box = element
            print("We found the dest in box: " + str(dest_box))


    ## implement BFS to see if a possible path exists
    queue = []
    visited = []
    detail_points = {}
    path = []

    heappush(queue,(0,source_box))
    while(queue):
        node = heappop(queue)
        box = node[1]

        if(box == dest_box):
            print("Path exists!")
        else:
            # show we visited this node
            visited.append(box)

            if(box == source_box):
                y = source_point[0]
                x = source_point[1]
                detail_points[box] = (x,y)

            # find center of box (center isn't good but will work for this test)
            else:
                y = (int(box[1]) + int(box[0])) / 2
                x = (int(box[3]) + int(box[2])) / 2
                detail_points[box] = (x,y)

            #print("(x,y): " + str(x) + ',' + str(y))

        # now look for neighboors and add to queue
        for neighboor in mesh['adj'][box]:
            print(neighboor)
            if neighboor not in visited and neighboor not in queue:
                heappush(queue,(1, neighboor))

    #print(detail_points)
    return path, boxes.keys()