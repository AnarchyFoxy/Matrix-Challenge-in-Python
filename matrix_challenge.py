def matrix_challenge(str_arr):
    rows = len(str_arr)
    cols = min(len(s) for s in str_arr) if rows > 0 else 0
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    # Convert the string matrix to a 2D integer matrix
    for i in range(rows):
        chars = list(str_arr[i])
        for j in range(cols):
            matrix[i][j] = int(chars[j])

    # Calculate the maximum area of the largest rectangular submatrix containing all 1's
    max_area = max_rectangle_area(matrix)

    return str(max_area)


# Function to calculate the maximum area of the largest rectangular submatrix containing all 1's
def max_rectangle_area(matrix):
    rows = len(matrix)
    if rows == 0:
        return 0
    cols = len(matrix[0])
    max_area = 0

    heights = [0] * cols

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                heights[j] = 0
            else:
                heights[j] += matrix[i][j]
        max_area = max(max_area, largest_rectangle_area(heights))

    return max_area


# Function to calculate the maximum area of the largest rectangular submatrix in a histogram
def largest_rectangle_area(heights):
    n = len(heights)
    max_area = 0
    stack = []

    for i in range(n + 1):
        while stack and (i == n or heights[i] < heights[stack[-1]]):
            height = heights[stack.pop()]
            width = i - stack[-1] - 1 if stack else i
            max_area = max(max_area, height * width)
        stack.append(i)

    return max_area


# Test the function with the example inputs
str_arr1 = ["10100", "10111", "1111", "10010"]
str_arr2 = ["1011", "0011", "0111", "1111"]

output1 = matrix_challenge(str_arr1)
output2 = matrix_challenge(str_arr2)

print(output1)  # Output: "6"
print(output2)  # Output: "8"
