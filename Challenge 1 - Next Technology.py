class ShoppingBag:

    def calculate_bag_total(self, items, discounts):
        # Dictionary of item codes matched to their price
        items_parsed = {}

        # Dictionary of item codes matched to their discounted price
        discounted_items = {}
        
        # Dictionary of discounts and their data
        discounts_parsed = {}
        
        # Dictionary to store the number of each item
        item_count = {}

        # Parses shopping bag items
        for item in items:
            try: # Attempts to parse valid item codes
                item_code = item[0:3]
                if item_code not in item_count:
                    item_count[item_code] = 1
                else:
                    item_count[item_code] += 1

                #print(f"Item count: {item_count}")

                if item not in items_parsed:
                    item_cost = int(item[3:6])
                    items_parsed[item_code] = item_cost
                    discounted_items[item_code] = item_cost # Initialises discounted items dict

                    #print(f"Item code: {item_code}, Item cost: {item_cost}, Items parsed: {items_parsed}")
            except: # Item code is not in valid format
                continue

        #print(item_count)
        #print(items_parsed)

        # Parses discount codes
        for discount in discounts:
            discount_item_exists = True

            try: # Attempts to parse valid discount codes
                item_code = discount[0:3]
                min_items = int(discount[3])
                discount_category = discount[4]
                discount_amount = int(discount[5:7])
            except: # Discount is not in valid format
                continue

            try:
                no_of_items = int(item_count[item_code])
                item_cost = int(items_parsed[item_code])
            except:
                discount_item_exists = False # Item to discount doesn't exist

            if discount_item_exists == False:
                continue

            #print(f"Number of items: {no_of_items}, item cost: {item_cost}")
            #print(f"Discount category: {discount_category}, Discount amount: {discount_amount}")

            if no_of_items >= min_items and discount_amount > 0:
                if discount_category == 'P':
                    percentage_discount = item_cost * (discount_amount/100)
                    #print(f"1: {percentage_discount}")
                    discounted_cost = (item_cost - percentage_discount)
                    #print(f"1: {discounted_cost}")
                elif discount_category == 'C': 
                    discounted_cost = item_cost - discount_amount
                    #print(f"2: {discounted_cost}")
                else:
                    continue
            else:
                discounted_cost = item_cost
                #print(f"3: {discounted_cost}")

            best_price = int(discounted_items[item_code])

            if discounted_cost < 0:
                discounted_cost = 0

            if discounted_cost < best_price: #Change to compare with discounted amounts
                discounted_items[item_code] = discounted_cost

        # Updates the item costs if their is a better discounted price
        for item in items_parsed:
            if int(items_parsed[item]) > int(discounted_items[item]):
                items_parsed[item] = discounted_items[item]

        #print(item_count)
        #print(items_parsed)

        total_cost = 0

        # Calculates basket total
        for item in item_count:
            total_items = (item_count[item])

            try: 
                price = float(items_parsed[item])
            except:
                continue

            cost = total_items * price

            total_cost += cost

        print(total_cost)



solution = ShoppingBag()

"""
solution.calculate_bag_total([ "ABC123" ], [ "ABC1P10" ]) #110.7
solution.calculate_bag_total([ "ABC123" ], [ "ABC1C10" ]) #113
solution.calculate_bag_total([ "ABC010", "DEF020", "ABC010" ], [ "ABC2P50", "DEF1C05" ]) #25.0
solution.calculate_bag_total([ "ABC123" ], [ "ABC1P00" ]) #123 Discount is entered as 0
solution.calculate_bag_total([ "ABC200" ], [ "ABC1P50", "ABC1C90" ]) #100 P discount value is smaller than C but is a greater discount
solution.calculate_bag_total([ "ABC123" ], [ "DEF1P10" ]) #123

solution.calculate_bag_total([ "GHK123", "ABC010", "DEF020", "ABC010" ], [ "GHK1P10", "ABC2P50", "DEF1C05" ]) #135.7
solution.calculate_bag_total([ "000123" ], [ "0001P10" ]) #110.7 Item code includes numbers
solution.calculate_bag_total([ "ABC123" ], [ "ABC2P10" ]) #123 Basket doesn't qualify for discount
solution.calculate_bag_total([ "ABC123" ], [ "ABC0P10" ]) #110.7 Min items for discount is 0
solution.calculate_bag_total([ "ABC010" ], [ "ABC1C50" ]) #0.0 Discount brings item price to 0

solution.calculate_bag_total([ "ABC010" ], [ "ABC1Q50" ]) #10 Discount category is invalid
"""

# Official test cases

solution.calculate_bag_total(["ABC123"], ["ABC1P10"]) #110.7
solution.calculate_bag_total(["ABC123"], ["ABC1C10"]) #113
solution.calculate_bag_total(["ABC010","DEF020","ABC010"], ["ABC2P50","DEF1C05"]) #25
solution.calculate_bag_total(["ABC123","ABC123"], ["ABC1P10"]) #221.4
solution.calculate_bag_total(["ABC008"], ["ABC1P05"]) #7.6
solution.calculate_bag_total(["ABC123","ABC123"], ["ABC1C10"]) #226
solution.calculate_bag_total(["ABC008"], ["ABC1C05"]) #3
solution.calculate_bag_total(["ABC123"], ["DEF1P10"]) #123
solution.calculate_bag_total(["ABC123"], [""]) #123
solution.calculate_bag_total([""], ["ABC1P10"]) #0
solution.calculate_bag_total([""], [""]) #0
solution.calculate_bag_total(["ABC123","ABC123"], ["ABC2P10"]) #221.4
solution.calculate_bag_total(["ABC123","ABC123"], ["ABC3P10"]) #246
solution.calculate_bag_total(["ABC123","ABC123"], ["ABC2C10"]) #226
solution.calculate_bag_total(["ABC123","ABC123"], ["ABC3C10"]) #246
solution.calculate_bag_total(["ABC123","BCD012"], ["ABC1P10","BCD1C10"]) #112.7
solution.calculate_bag_total(["ABC005","BCD020"], ["ABC1C10"]) #20
solution.calculate_bag_total(["ABC200"], ["ABC1C10","ABC1C20"]) #180
solution.calculate_bag_total(["ABC200"], ["ABC1P10","ABC1P20"]) #160
solution.calculate_bag_total(["ABC200"], ["ABC1C10","ABC1P10"]) #180
solution.calculate_bag_total(["ABC050"], ["ABC1C10","ABC1P10"]) #40
solution.calculate_bag_total(["ABC050","BCD020","BCD020","ABC050","BCD020","CDE020","EFG200","EFG200"], ["ABC3C40","ABC3P50","ABC2P10","BCD2C30","ABC2C05","ABC1P20","ABC1C05","DEF1C10","EFG3C40","EFG3P50","EFG2P10","EFG2C05","EFG1P20","EFG1C50"]) #400

"""
TEST CASES
- If an item qualifies for multiple discounts, only the highest discount should apply
- An item cannot be discounted to be less than £0
- Any matching discount should apply to all matching items
- No discount code exists for the item
- The % discount is better than the cash discount but the cash number is bigger
- Item code includes numbers
- Basket does not qualify for any discounts

- Discount category is invalid
"""