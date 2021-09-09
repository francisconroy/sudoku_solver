import unittest
from main import solve, printgrid, findrange


class MyTestCase(unittest.TestCase):
    def test_simple_grid(self):
        grid = [[0, 0, 0, 0, 0, 0, 9, 0, 0],
                [0, 0, 0, 2, 6, 0, 0, 0, 7],
                [0, 0, 0, 7, 5, 1, 0, 0, 0],
                [0, 8, 6, 0, 0, 2, 4, 0, 0],
                [0, 1, 2, 0, 0, 0, 3, 0, 0],
                [0, 0, 3, 4, 0, 0, 0, 9, 0],
                [7, 0, 0, 5, 8, 0, 0, 0, 3],
                [0, 0, 0, 0, 0, 7, 0, 5, 0],
                [0, 2, 0, 0, 0, 0, 7, 0, 4]]
        solution = solve(grid)
        sol = [[2, 5, 7, 8, 4, 3, 9, 6, 1],
               [8, 3, 1, 2, 6, 9, 5, 4, 7],
               [6, 9, 4, 7, 5, 1, 8, 3, 2],
               [9, 8, 6, 3, 7, 2, 4, 1, 5],
               [4, 1, 2, 6, 9, 5, 3, 7, 8],
               [5, 7, 3, 4, 1, 8, 2, 9, 6],
               [7, 6, 9, 5, 8, 4, 1, 2, 3],
               [3, 4, 8, 1, 2, 7, 6, 5, 9],
               [1, 2, 5, 9, 3, 6, 7, 8, 4]]

        self.assertEqual(solution, sol)

    def test_other_grid(self):
        grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 8, 4, 0, 1, 0, 0, 3],
                [1, 0, 7, 0, 2, 0, 0, 4, 0],
                [0, 0, 6, 7, 4, 2, 0, 0, 9],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [9, 0, 0, 5, 6, 8, 1, 0, 0],
                [0, 3, 0, 0, 1, 0, 6, 0, 8],
                [4, 0, 0, 9, 0, 3, 5, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        solution = solve(grid)
        sol = [[3, 5, 4, 8, 9, 6, 2, 1, 7],
               [6, 2, 8, 4, 7, 1, 9, 5, 3],
               [1, 9, 7, 3, 2, 5, 8, 4, 6],
               [5, 1, 6, 7, 4, 2, 3, 8, 9],
               [8, 4, 2, 1, 3, 9, 7, 6, 5],
               [9, 7, 3, 5, 6, 8, 1, 2, 4],
               [7, 3, 5, 2, 1, 4, 6, 9, 8],
               [4, 6, 1, 9, 8, 3, 5, 7, 2],
               [2, 8, 9, 6, 5, 7, 4, 3, 1]]
        self.assertEqual(solution, sol)

    def test_findrange(self):
        self.assertEqual(findrange(0), [0,1,2])
        self.assertEqual(findrange(1), [0,1,2])
        self.assertEqual(findrange(2), [0,1,2])
        self.assertEqual(findrange(3), [3,4,5])
        self.assertEqual(findrange(4), [3,4,5])
        self.assertEqual(findrange(5), [3,4,5])
        self.assertEqual(findrange(6), [6,7,8])
        self.assertEqual(findrange(7), [6,7,8])
        self.assertEqual(findrange(8), [6,7,8])


if __name__ == '__main__':
    unittest.main()
