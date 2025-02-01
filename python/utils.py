def extract_from_link(link,parameter):
    """
    Directly extract parameter value from the link.

    :param link: Original url to extract from.
    :param parameter: Parameter key to extract.
    :return: Value with parameter key  extracted from url.
    """
    q = ""
    for char in link:
        #End condition
        if q and char=="/":
            #removing the key
            q=q[2:]
            break
        #from start until the end condition
        if char == parameter or q:
            q+=char
    return q