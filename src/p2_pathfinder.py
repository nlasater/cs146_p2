
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
    
    ## find location of src and dest point
    for element in mesh['boxes']:
      if int(element[0]) < source_point[1] and int(element[1]) > source_point[1] and int(element[2]) < source_point[0] and int(element[3]) > source_point[0]:
        source_box = element
        print("We found the src in box: " + str(source_box))
        
      if int(element[0]) < destination_point[1] and int(element[1]) > destination_point[1] and int(element[2]) < destination_point[0] and int(element[3]) > destination_point[0]:
        dest_box = element
        print("We found the dest in box: " + str(dest_box))
      
    ## implement BFS to see if a possible path exists
    queue = []
    visited = []
    queue.append(source_box);
    while(queue):
      node = queue.pop()
      if(node == dest_box):
        print("Path exists!")
      else:
        ## show we visited this node
        visited.append(node)
        ## find center of box (center isn't good but will work for this test)
        y = node[1] - node[0]
        x = node[3] - node[2]
        print("(x,y): " + str(x) + ',' + str(y))
        
        ## now look for neighboors and add to queue
        for neighboor in mesh['adj'][node]:
          print(str(neighboor))
          if neighboor in visited:
            continue
          else:
            queue.append(neighboor)
      
      
    
    

    return path, boxes.keys()
