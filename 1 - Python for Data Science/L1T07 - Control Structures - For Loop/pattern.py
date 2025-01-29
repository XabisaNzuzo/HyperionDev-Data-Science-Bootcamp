# This defines the number of rows for the star pattern
total_rows = 9

# Loops through the range of rows

for x in range(0, total_rows + 1):
    if x <= total_rows // 2 + 1: 

        # Print increasing stars for the first half

        print('*' * x)
    else:

        # Print decreasing stars for second half

        print('*' *(total_rows - x + 1))
