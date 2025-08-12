"""
Problem:
You are given a string consisting only of '(' and ')'.
Every opening parenthesis '(' has a matching closing parenthesis ')',
so the string is always a valid set of parentheses.

Define the evaluation of such a string, Eval(s), according to these rules:

Rule 1:
An empty string "" has a value of 0.
    Eval("") = 0

Rule 2:
If s is a valid parentheses string, then the value of (s) is:
    Eval("(" + s + ")") = 2 ^ Eval(s)

Rule 3:
If s and q are valid parentheses strings, then concatenating them
is evaluated as the sum of their evaluations:
    Eval(s + q) = Eval(s) + Eval(q)

Examples:
    "()"           => 2 ^ 0 = 1
    "()()"         => 1 + 1 = 2
    "(())"         => 2 ^ 1 = 2
    "(()())"       => 2 ^ (1 + 1) = 4
    "()(())()"     => 1 + (2 ^ 1) + 1 = 4
    "()(()())()"   => 1 + (2 ^ (1 + 1)) + 1 = 6
    "(()()()())()" => 2 ^ (1 + 1 + 1 + 1) + 1 = 17
    "((()())(()())(()()))" => 2 ^ (4 + 4 + 4) = 2 ^ 12 = 4096
"""

import unittest

PARAN_CLOSE, PARAN_OPEN = ")", "("


def solution(s: str) -> int:
    if not s:
        return 0

    stack = []
    eval_stack = []
    current_eval = 0

    for char in s:
        if char == PARAN_OPEN:
            stack.append(char)
            eval_stack.append(current_eval)
            current_eval = 0
        elif char == PARAN_CLOSE:
            if stack:
                stack.pop()
                if eval_stack:  # If there's a previous eval context
                    current_eval = 2**current_eval + eval_stack.pop()
            else:
                current_eval = 1

    return current_eval


class TestSolution(unittest.TestCase):
    TEST_CASES = [
        ("()", 1),
        ("()()", 2),
        ("(())", 2),
        ("(()())", 4),
        ("()(())()", 4),
        ("()(()())()", 6),
        ("(()()()())()", 17),
        ("((()())(()())(()()))", 4096),
    ]

    def test_examples(self):
        for case, expected in self.TEST_CASES:
            with self.subTest(case=case):
                self.assertEqual(solution(case), expected)


if __name__ == "__main__":
    unittest.main()
