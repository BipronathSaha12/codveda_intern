from solver import NQueensSolver

# solution for row
def print_solutions(solutions):
    for idx, sol in enumerate(solutions, 1):
        print(f"\nSolution {idx}:")
        for row in sol:
            print(row)


def main():
    try:
        n = int(input("Enter value of N: "))
        solver = NQueensSolver(n)

        solutions = solver.solve()

        print(f"\nTotal Solutions: {len(solutions)}")
        print_solutions(solutions)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()