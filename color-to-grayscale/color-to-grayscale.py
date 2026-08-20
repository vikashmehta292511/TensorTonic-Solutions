def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    # Write code here

    height = len(image)
    width = len(image[0])
    grayscale = []
    for i in range(height):
        row = []
        for j in range(width):
            pixel = image[i][j]
            red = pixel[0]
            green = pixel[1]
            blue = pixel[2]
            gray_value = 0.299 * red + 0.587 * green + 0.114 * blue
            row.append(gray_value)
        grayscale.append(row)
    return grayscale