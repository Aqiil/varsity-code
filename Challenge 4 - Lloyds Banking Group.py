import unittest

class Solution:

    def number_of_days_to_save(self, moneySaved):
        if not (0 <= moneySaved <= 74926):
            #print('ERROR')
            return -1
        
        initial_value = 1
        days = 1

        total_accured = 0

        while True:
            current_value = initial_value
            for i in range(1, 8):
                total_accured += current_value
                current_value += 1
                if total_accured >= moneySaved:
                    #print(total_accured, days)
                    return days
                days += 1
            initial_value += 1


class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        self.assertEqual(solution.number_of_days_to_save(8), 4)

    def test2(self):
        solution = Solution()
        self.assertEqual(solution.number_of_days_to_save(36), 10)

    def test3(self):
        solution = Solution()
        self.assertEqual(solution.number_of_days_to_save(2.5), 2)

if __name__ == '__main__':
    unittest.main()


'''
The Problem
Natalie wants to save money for her first laptop. She puts money into her ABC Bank Account every day.

She has come up with an interesting approach to reach her savings goal:

She puts £1 in her account on Monday, the first day. Every day from Tuesday to Sunday, she will add in £1 more than the day before.
On every subsequent Monday, she will put in £1 more than the previous Monday.
Given the laptop Natalie wants to purchase costs x pounds, how many days will she have to save with ABC bank?

Please consider edge case values which may cause your program to fail, such as how many days must she save to accumulate £0.

Constraints:

From no laptop, to that really expensive model with all of the latest software and accessories, these are the possible inputs:

0 <= x <=74926
You should return -1 if the MoneySaved input x value should not be considered.
'''