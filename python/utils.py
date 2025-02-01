def extract_q(link):
    """
    Directly extract q value the link

    :param link: Original url to extract Q from
    :return: q value extracted from url.
    """
    q = ""
    for char in link:
        #End condition
        if q and char=="/":
            #removing the key
            q=q[2:]
            #padding for base64 decoding
            q += "=" * (4 - len(q) % 4)
            break
        #from start until the end condition
        if char=="q" or q:
            q+=char
    return q