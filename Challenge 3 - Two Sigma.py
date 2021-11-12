import unittest
import numpy as np
from decimal import *
import re

class Solution:

    def fix_fuel_config(self, config):
        invalid_config = "KEEP_PREVIOUS"
        valid_config = config

        points = self.parse_coordinates(config)

        points, validity = self.check_valid_config(points)
        if validity == False:
            return invalid_config

        new_config, validity = self.determine_collinearity(config, points, valid_config, invalid_config)
        if validity == True:
            return new_config
        else:
            return invalid_config

    def parse_coordinates(self, config):
        # Parses input into a list of coordinates
        points = []
        split_config = config.split(";")
        for pair in split_config:
            string_coordinate = pair.split(":")
            float_coordinate = [float(i) for i in string_coordinate]
            points.append(float_coordinate)
        
        return points

    def check_valid_config(self, points):
        validity = False

        # If 4 input points are not entered, the config is incorrect
        if len(points) != 4:
            return points, validity
        
        # If the x coordinates are not unique or the values of x and y are not between 0 and 100, the config is incorrect
        unique_x = set()
        for pair in points:
            x = float(pair[0])
            y = float(pair[1])
            if (0 <= x <= 100) and (0 <= y <= 100):
                if x in unique_x:
                    return points, validity
                else:
                    unique_x.add(x)
            else:
                return points, validity

        validity = True
        return points, validity

    def determine_collinearity(self, config, points, valid_config, invalid_config):
        validity = False
        # Determines if the input points are collinear
        points_matrix = np.matrix(points)
        matrix_rank = np.linalg.matrix_rank(points_matrix)

        # If matrix rank of the input points is 1 then the config is valid
        if matrix_rank <= 1:
            validity = True
            return config, validity
        else:
            matrix3 = np.matrix([points[0], points[1], points[2]])
            rank3 = np.linalg.matrix_rank(matrix3)
            matrix0 = np.matrix([points[1], points[2], points[3]])
            rank0 = np.linalg.matrix_rank(matrix0)
            matrix1 = np.matrix([points[2], points[3], points[0]])
            rank1 = np.linalg.matrix_rank(matrix1)
            matrix2 = np.matrix([points[3], points[0], points[1]])
            rank2 = np.linalg.matrix_rank(matrix2)

            invalids = 0
            index = 0

            if rank3 == 1:
                invalids += 1
                index = 3
            if rank2 == 1:
                invalids += 1
                index = 2
            if rank1 == 1:
                invalids += 1
                index = 1
            if rank0 == 1:
                invalids += 1
                index = 0
            
            if invalids != 1:
                return config, validity
            else:
                x = points[index][0]

                # Removes the index of the invalid pair
                valid_pairs = [0, 1, 2, 3]
                valid_pairs.remove(index)

                # Calculates the equation of a straight line
                index1 = valid_pairs[0]
                index2 = valid_pairs[1] 

                index1x = points[index1][0]
                index1y = points[index1][1]

                index2x = points[index2][0]
                index2y = points[index2][1]

                gradient = (index2y - index1y)/float(index2x - index1x)

                y = gradient * (x - index1x) + index1y
                points[index][1] = y

                for pair in range(0, len(points)):
                    x = points[pair][0]
                    y = points[pair][1]

                    x = self.truncate_reccuring(str(x))
                    y = self.truncate_reccuring(str(y))

                    points[pair][0] = str(Decimal(float(x)).normalize())
                    points[pair][1] = str(Decimal(float(y)).normalize())
                
                tested_points, validity = self.check_valid_config(points)
                if validity == False:
                    return invalid_config
                
                new_config = []
                for pair in points:
                    joined_pairs = ':'.join(pair)
                    new_config.append(joined_pairs)
                
                new_config = ';'.join(new_config)

                validity = True
                return new_config, validity

    def truncate_reccuring(self, num):
        repeating_pair = re.escape(num.split('.')[1][:2])
        check_within = num.split('.')[1][2:]

        if re.match(repeating_pair, check_within):
            return("{:.2f}".format(float(num)))
        else:
            return("{:.1f}".format(float(num)))

class SolutionTests(unittest.TestCase):

    def test1(self):
        solution = Solution()
        self.assertEqual(solution.fix_fuel_config("1:2;2:4;3.5:7;4:8"), "1:2;2:4;3.5:7;4:8")

    def test2(self):
        solution = Solution()
        self.assertEqual(solution.fix_fuel_config("1:1;2:5;3:3;4:6"), "KEEP_PREVIOUS")

    def test3(self):
        solution = Solution()
        self.assertEqual(solution.fix_fuel_config("1:1;1:2;3:3;4:4"), "KEEP_PREVIOUS")

    def test4(self):
        solution = Solution()
        self.assertEqual(solution.fix_fuel_config("1:1;2:2;3.5:3.5;4:5"), "1:1;2:2;3.5:3.5;4:4")

    #PRIVATE TEST CASES

    def test5(self):
        solution = Solution()
        self.assertEqual(solution.fix_fuel_config("1:1;4:2;3.5:3.5;4:5"), "KEEP_PREVIOUS")

    def test6(self):
        solution = Solution()
        self.assertEqual(solution.fix_fuel_config("1:1;2:2;3.5:3.5;4:1.333"), "1:1;2:2;3.5:3.5;4:4")

if __name__ == '__main__':
    unittest.main()