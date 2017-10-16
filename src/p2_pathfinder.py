
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
      ##print("not the destination!")
    
   

    return path, boxes.keys()
