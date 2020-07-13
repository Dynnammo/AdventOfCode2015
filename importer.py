def open_single_line_file(file_name):
    return open('inputs/{}'.format(file_name), 'r').read()


def open_multiline_line_file(file_name):
    return open_single_line_file(file_name).split('\n')
