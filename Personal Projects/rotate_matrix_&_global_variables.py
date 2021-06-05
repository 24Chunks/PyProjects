# python 3.9
# This program will rotate a matrix 90 degrees clockwise

n = 5
mat = [[0] * n for i in range(n)]



def enter_values():
    for i in range(n):
        s = input("ENTER ROW VALUES: ")
        values_l = s.split()
        for j, val in enumerate(values_l):
            mat[i][j] = val

def print_matrix():
    for i in range(n):
        for j in range(n):
            print(f"{mat[i][j]}".ljust(5), end="")
        print()


#FORMULA [new i = old j] [new j = 4 - old i]
def rotate90_clockwise():
    global mat
    rotated_mat = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_mat[j][(n-1)-i] = mat[i][j]
    mat = rotated_mat


def main():
    global n
    global mat

    n = int(input("Whats the matrix size: "))
    mat = [[0] * n for i in range(n)]

    enter_values()
    print_matrix()
    rotate90_clockwise()
    
    print()
    print("ROTATED 90*---->")
    print()
    
    print_matrix()

main()
