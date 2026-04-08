# WRITE LOGIC OF MATRIX ADDITON AND MULTIPLICATUIN:

#EXAMPLE-1:
'''Algorithm Sum(A,n)
    {s=0;
        for(i=0;i<n;i++)
        {s=s+A[i];
        }
        return s;
    }

f(n) = 2n+3
Time Complexity: O(n)
Space Complexity: O(n)
''' 
# Sum of 2 matrices:
'''
algorith Add(A,B,n)
    {for(i=0 ;i<n; i++)
        {for(j=0; j<n; j++)
            {c[i,j] = A[i,j] + B[i,j];
            }
        }
    }

f(n) = 2n^2+2n+1
Time Complexity: O(n^2)
Space Complexity: O(n^2)
'''
# Multiplication of 2 matrices:
'''
algorith Multiply(A,B,n)
    {for(i=0 ;i<n; i++)
        {for(j=0; j<n; j++)
            {C[i,j] = 0;
            for(k=0; k<n; k++)
                {C[i,j] = C[i,j] + A[k,j] * B[k,j];
                }
            }
        }
    }
Time Complexity:
f(n) = 2n^3+3n^2+2n+1
       O(n^3)

Space Complexity:
f(n) = 3n^2+4
       O(n^2)
'''