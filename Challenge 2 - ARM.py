import unittest

class Solution:
    
    def number_prediction(self, number):
        # Pads the number with 10 0s in the event the first number is blank
        #print(number)
        number = '0000000000' + number
        #print(list(number))

        # List to store the index of each blank
        blanks = [] 

        # Iterates through number sequence to locate blank spaces
        index = 0        
        for digit in number:
            #print(digit)
            if digit.isdigit():
                pass
            else:
                number = self.fill_in_blank(index, number)
                #number = '0000000000' + number
            index += 1
        fnumber = number[10:]
        #print(f'FINAL NUMBER: {fnumber}')
        return fnumber

    # Identifies the preceding 10 digits of each blank space
    def fill_in_blank(self, blank_index, number):
        # Fills in the missng number for each blank
        underscore_position = int(blank_index)
        previous_digit = number[underscore_position - 1] # Digit before the underscore
        previous_digit_position = underscore_position-1
        preceding_10_digits = number[underscore_position-10: underscore_position] # Preceding 10 digits before underscore /// Always starts from leftmost underscore so there will not be any underscores within the preceding 10 digits

        #print(underscore_position, previous_digit, preceding_10_digits)

        # Identifies possible subsequences that match the original preceding 10 digits before the underscore
        possible_subsequences = {}

        index = 9
        for digit in range(9, len(number)):
            if number[digit] == previous_digit and index < previous_digit_position and index : # Looks through sequence to find any number that matches preceding number
                possible_subsequences[index] = number[index-9: index+1] # Adds the index of the preceeding digit as the key and the preceding 10 digits as the value
            index += 1
        
        #print(f'[*] {possible_subsequences}')

        # Stores matching subsequences
        matches = {}

        # Finds the nearest match for each possible subsequence
        for index in possible_subsequences:
            subsequence_index = index
            subsequence = possible_subsequences[index]

            #print(f'{subsequence_index}, {subsequence}')
            # Compares the subsequnce with original preceding 10 digits
            count = -1
            matching_numbers = 0

            #print(f'Comparing: {preceding_10_digits} and {subsequence}')
            for position in range(0, len(preceding_10_digits)):
                #print(f'Compare {preceding_10_digits[count]} with {subsequence[count]}')
                preceding_10_digit_at_index = preceding_10_digits[count]
                subsequence_didgit_at_index = subsequence[count]

                if preceding_10_digit_at_index == subsequence_didgit_at_index:
                    matching_numbers += 1
                else:
                    break # Ends loop if numbers do not match
                count -= 1

            #print(f'Longest match is: {matching_numbers}')
            matches[subsequence_index] = matching_numbers
        
        #print(f'Matches: {matches}')

        # Find the longest and most recent match
        longest_match = 0
        longest_match_index = 0

        for index in matches:
            match = matches[index]
            # If the current match is longer than the longest_match
            if match > longest_match:
                longest_match = match
                longest_match_index = index
                continue
            # If the current match and the longest_match are of equal length
            elif match == longest_match:
                # If the current match is more recent than the longest_match
                if index > longest_match_index:
                    longest_match = match
                    longest_match_index = index
        
        #print(f'Longest match: {longest_match}, index: {longest_match_index}')

        # Find the number after the index of the longest match
        if longest_match == 0:
            number_after = previous_digit
        # If there are no matches fill the gap with the previous number
        else:
            number_after = number[longest_match_index+1]
        
        #print(underscore_position, number_after)
        number = number[0: underscore_position] + number_after + number[underscore_position+1:] # Duplicates string to update underscore value and replaces original.

        return number

### TESTING ###

class SolutionTests(unittest.TestCase):
    def test1(self):
        solution = Solution()
        self.assertEqual(solution.number_prediction("121_"), "1212")

    def test2(self):
        solution = Solution()
        self.assertEqual(solution.number_prediction("121_343_1_1_3_"), "12123434121234")

    def test3(self):
        solution = Solution()
        self.assertEqual(solution.number_prediction("121_312____"), "12123123123")

    def test4(self):
        solution = Solution()
        self.assertEqual(solution.number_prediction("13123243_"), "131232432")

    def test5(self):
        solution = Solution()
        self.assertEqual(solution.number_prediction("1234235123_"), "12342351234")

    def test6(self):
        solution = Solution()
        self.assertEqual(solution.number_prediction("70000000_"), "700000007")

    def test7(self):
        solution = Solution()
        self.assertEqual(solution.number_prediction("10000000001200000000021000000000_"), "100000000012000000000210000000001")

    def test8(self):
        solution = Solution()
        self.assertEqual(solution.number_prediction("10000000000120000000000210000000000_"), "100000000001200000000002100000000002")

    def test9(self):
        solution = Solution()
        self.assertEqual(solution.number_prediction("1_2_3_11____"), "112233112233")

    def test10(self):
        solution = Solution()
        self.assertEqual(solution.number_prediction("___"), "000")

    def test11(self):
        solution = Solution()
        self.assertEqual(solution.number_prediction("43127435926350613352415886760955388_8983743325219_168_926629293_776892_9_1_8_8049287_298_9343647_9_2334_4_6_7__57__30785__7__62_1____4_____382__1226816__04__67___0119_47__0_0_7___0___0_3__3_____06_37_"), "43127435926350613352415886760955388689837433252198168992662929327768929921981804928762981934364769323343436476957693078576760629193434364763829112268168904926760601193476307077689049204312334343060374")

    def test12(self):
        solution = Solution()
        self.assertEqual(solution.number_prediction("1059384231063272231283077963_86390_07292893174_4389407054_9205___0104__35130_3__68_67577_2_38_3_2__47255__7_34674938809759_6_5_525_5_44_56____2_9__5_0_5__153_____08________7___3_17_______0__1____8___6"), "10593842310632722312830779632863907072928931742438940705409205409010409351307307689675779203893128347255557734674938809759367575255554445675752593659015901536590108097593677346391742438940701080980986")

# Personal test cases

    def test13(self):
        solution = Solution()
        self.assertEqual(solution.number_prediction("_1_2_3_11____"), "0112233112233")

    def test14(self):
        solution = Solution()
        self.assertEqual(solution.number_prediction("7000_543215_"), "700075432154")

    def test15(self):
        solution = Solution()
        self.assertEqual(solution.number_prediction("___1_2_3_11____"), "000112233112233")

    def test16(self):
        solution = Solution()
        self.assertEqual(solution.number_prediction("700_121_312____"), "700712123123123")

    def test17(self):
        solution = Solution()
        self.assertEqual(solution.number_prediction("_121_"), "01212")
    

if __name__ == '__main__':
    unittest.main()