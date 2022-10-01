import pandas

squirrel_table = pandas.read_csv('../../Downloads/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

gray_squirrels_count = len(squirrel_table[squirrel_table['Primary Fur Color'] == 'Gray'])

black_squirrels_count = len(squirrel_table[squirrel_table['Primary Fur Color'] == 'Black'])

cinnamon_squirrels_count = len(squirrel_table[squirrel_table['Primary Fur Color'] == 'Cinnamon'])

# gray_squirrels = squirrel_table['Primary Fur Color'] == 'Black'

# cinnamon_squirrels = squirrel_table['Primary Fur Color'] == 'Cinnamon'

# black_squirrels = squirrel_table['Primary Fur Color'] == 'Black'

squirrel_dictionary = {
    'Fur Colour': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray_squirrels_count, black_squirrels_count, cinnamon_squirrels_count]
}

df = pandas.DataFrame(squirrel_dictionary)
df.to_csv('squirrel_count.csv')

