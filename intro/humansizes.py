#This looks like an object from JavaScript, but in Python Land, it's called a dictionary
SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

# Instead of the word `function`, in Python, you use `def`
def approximate_size(size, a_kilobyte_is_1024_bytes=True):

    '''Convert a file size to human-readable form.

    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
                                if False, use multiples of 1000

    Returns: string

    '''

    # For if and for blocks, you don't use {} to define the block scope. You use a colon, and then indent the corresponding code
    if size < 0:
        raise ValueError('number must be non-negative')

    # This is the style for writing a ternary condition in Python.
    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    for suffix in SUFFIXES[multiple]:
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)

    raise ValueError('number too large')

if __name__ == '__main__':
    # The print() method is Python's console.log()
    print(approximate_size(1638984, False))
    print(approximate_size(size=16384, a_kilobyte_is_1024_bytes=True))
    print(approximate_size(16384))