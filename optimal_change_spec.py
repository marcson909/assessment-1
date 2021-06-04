# Write your unit tests here!
import unittest
from optimal_change import optimal_change


class OptimalChangeTestCase(unittest.TestCase):

    #check if function returns string
    def test_string_output(self):
        self.assertIsInstance(optimal_change(1, 1), str)

    #check exact change edge case
    def test_exact_change(self):
        self.assertEqual(optimal_change(1.05, 1.05), "You paid with exact change!")
    
    #check if amount paid less than item cost
    def test_not_enough(self):
        self.assertEqual(optimal_change(10, 4.27), "You still owe $5.73!")
    
    #check if change is 1 penny
    def test_one_penny(self):
        self.assertEqual(optimal_change(1, 1.01), "The optimal change for an item that costs $1 with an amount paid of $1.01 is 1 penny.")
    
    #check if change is multiple pennies
    def test_multiple_pennies(self):
        self.assertEqual(optimal_change(1, 1.04), "The optimal change for an item that costs $1 with an amount paid of $1.04 is 4 pennies.")
    
    #check if output matches 1st readme example
    def test_readme_test1(self):
        self.assertEqual(optimal_change(62.13, 100), "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")
        
    #check if output matches 2nd readme example
    def test_readme_test1(self):
        self.assertEqual(optimal_change(31.51, 50), "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")


if __name__ == "__main__":
    unittest.main
