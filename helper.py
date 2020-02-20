def conv2D_output_shape(input_shape, n_filters, kernel_size, stride = 1, padding = 0):
    in_x, in_y, in_z = input_shape
    output_x = (in_x - kernel_size + 2 * padding) / stride + 1
    output_y = (in_y - kernel_size + 2 * padding) / stride + 1
    output_z = n_filters
    return (output_x, output_y, output_z)