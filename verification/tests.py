"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[4, 2, 0, 3, 2], [1, 3]],
            "answer": 1,
        },
        {
            "input": [[1, 3, 2, 5], [3, 3, 3, 4]],
            "answer": 3,
        },
        {
            "input": [[0, 0, 0], [1, 2, 3]],
            "answer": 0,
        },
        {
            "input": [[1, 5, 5], [1, 1, 2, 2, 3, 3]],
            "answer": 5,
        },
        {
            "input": [[10, 0, 10, 0, 10], [2, 4, 1, 3, 5]],
            "answer": 3,
        },
    ],
    "Extra": [
        {
            "input": [[2, 2, 2, 2, 2], [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]],
            "answer": 10,
        },
        {
            "input": [[1, 1, 1, 1, 1], [6, 7, 8, 9]],
            "answer": 0,
        },
        {
            "input": [[5], [1, 1, 1, 1, 1]],
            "answer": 5,
        },
        {
            "input": [[0], [1, 1, 1, 1, 1]],
            "answer": 0,
        },
        {
            "input": [[0, 5, 2, 7, 10, 2, 1],[1, 3, 5, 7, 7]],
            "answer": 3,
        },
    ]
}