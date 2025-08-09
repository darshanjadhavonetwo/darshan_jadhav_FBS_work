
def custom_range(start, stop=None, step=1):

    if stop is None:
        stop = start
        start = 0


    if step > 0:
        while start < stop:
            yield start
            start += step
    elif step < 0:
        while start > stop:
            yield start
            start += step
    else:
        raise ValueError("step argument must not be zero")

print("Custom range output:")
for num in custom_range(2, 10, 2):
    print(num, end=' ')
