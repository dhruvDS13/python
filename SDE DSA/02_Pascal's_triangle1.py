'''
# Method 1: Iterative Approach
# Class containing Pascal's Triangle generation logic
class Solution:
    # Function to generate Pascal's Triangle up to numRows
    def generate(self, numRows):
        # Result list to hold all rows
        triangle = []

        # Loop for each row
        for i in range(numRows):
            # Create a row with size (i+1) and initialize all elements to 1
            row = [1] * (i + 1)

            # Fill elements from index 1 to i-1 (middle values)
            for j in range(1, i):
                # Each element = sum of two elements above it
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            # Add current row to the triangle
            triangle.append(row)

        return triangle


if __name__ == "__main__":
    obj = Solution()
    n = 5

    # Generate and print Pascal's Triangle
    result = obj.generate(n)
    for row in result:
        print(" ".join(map(str, row)))
# Time Complexity: O(N^2), we generate all the elements in first N rows sequentially one by one.
# Space Complexity: O(N^2), additional space used for storing the entire pascal triangle.
'''


# Method 2: Recursive Approach
# Class containing Pascal's Triangle row generation logic
class Solution:
    def getNthRow(self, N):
        row = [1]
        val = 1
        
        for k in range(1, N + 1):
            val = val * (N - k + 1) // k
            row.append(val)
        
        return row


# Example
N = 5
sol = Solution()
print(sol.getNthRow(N))




'''
# Solution class to find the (r, c) element of Pascal's Triangle
class Solution:
    # Function to compute binomial coefficient (nCr)
    def findPascalElement(self, r, c):
        # Element is C(r-1, c-1)
        n = r - 1
        k = c - 1

        result = 1

        # Compute C(n, k) using iterative formula
        for i in range(k):
            result *= (n - i)
            result //= (i + 1)

        return result


# Main code to test the solution
if __name__ == "__main__":
    sol = Solution()
    r, c = 5, 3
    print(sol.findPascalElement(r, c))
# Time Complexity: O(r), we compute the binomial coefficient using a loop that runs k times, where k is at most r.
# Space Complexity: O(1), we use only a constant amount of space to store the result and loop variables.
'''