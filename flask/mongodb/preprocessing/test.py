# Helps convert nouns into singular form (used to compare user ingredients with recipe ingredients)
        p = inflect.engine()
        
        # Convert all items in the inventory to singular form
        for i, item in enumerate(curInv):
            if p.singular_noun(item) == False:
                curInv[i] = item
            else:
                curInv[i] = p.singular_noun(item)