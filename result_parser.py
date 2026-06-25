def valid_result(m):

    if m["gain"] is None:
        return False

    if m["ugf"] is None:
        return False

    if m["pm"] is None:
        return False

    # remove extremely bad circuits
    if abs(m["gain"]) < 5:
        return False

    return True
