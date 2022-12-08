# Towers of Hanoi solution using a recursive algorithm
# Dr Gary Allen, University of Huddersfield

# Define the recursive function
def TowerOfHanoi(n, from_rod, to_rod, swap_rod):
    if n == 0:
     return
    TowerOfHanoi(n - 1, from_rod, swap_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n - 1, swap_rod, to_rod, from_rod)

# Input number of disks
print("Enter number of disks?")
number_of_disks = int(input())

# Call the recursive function
TowerOfHanoi(number_of_disks, 'A', 'C', 'B')  # A, B, anc C are the names of the three rods
