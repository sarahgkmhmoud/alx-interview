def canUnlockAll(boxes):
    """solve this"""

    setofkeys = []
    counter = 0
    totalboxes = len(boxes)
    for key in boxes[0]:
        if key < totalboxes and key not in setofkeys and key > 0:
            setofkeys.append(key)
            counter += 1
    index = 0
    while index < len(setofkeys):
        setkey = setofkeys[index]
        for key in boxes[setkey]:
            if key < totalboxes and key not in setofkeys and key > 0:
                setofkeys.append(key)
                counter += 1
        index += 1
    if counter == totalboxes - 1:
        return True
    else:
        return False
