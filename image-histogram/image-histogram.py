def image_histogram(image: list) -> list:
    """
    Returns a list of intensity and count pairs.
    """
    # Write code here

    height = len(image)
    width = len(image[0])
    counts = {}

    for i in range(height):
        for j in range(width):
            val = image[i][j]
            counts[val] = counts.get(val, 0) + 1

    result = [[intensity, counts[intensity]] for intensity in sorted(counts)]
    return result