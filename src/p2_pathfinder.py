
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
    
    ## find location of src point
    for element in mesh['boxes']:
      if int(element[0]) < source_point[0]:
        if int(element[1]) < source_point[1]:
          if int(element[2]) > source_point[0]:
            if int(element[3]) > source_point[1]:
              print("We found the src in box: " + str(element))
              source_box = element
      print("not the source!")
      
    ## find location of dest point
    for element in mesh['boxes']:
      if int(element[0]) < destination_point[0]:
        if int(element[1]) < destination_point[1]:
          if int(element[2]) > destination_point[0]:
            if int(element[3]) > destination_point[1]:
              print("We found the destination_point in box: " + str(element))
              dest_box = element
      print("not the destination_point!")
    
   

    return path, boxes.keys()
