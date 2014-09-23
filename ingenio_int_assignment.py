
categories = {}

def add_category(category_id, parent_category_id, name, keywords = None):
    categories.update({category_id : {'parent_category_id' : parent_category_id, 'name' : name, 'keywords' : keywords}})

def print_parent_category_id_and_name(parent_category_id, name):
    print 'ParentCategoryId = ', parent_category_id, ',', 'Name =', name, ',',

def find_keywords(category_id):
    while categories[category_id]['keywords'] == None:
        parent_category_id = categories[category_id]['parent_category_id']
        category_id = parent_category_id
    return categories[category_id]['keywords']

def print_keywords(category_id):
    print  'Keywords =', find_keywords(category_id)



add_category(100, -1, 'Business', 'Business keywords')
add_category(200, -1, 'Tutoring', 'Tutoring keywords')
add_category(101, 100, 'Accounting', 'Accounting keywords')
add_category(102, 100, 'Taxation')
add_category(201, 200, 'Computer')
add_category(103, 101, 'Corporate Tax')
add_category(202, 201, 'Operating system')
add_category(108, 101, 'Ent. Tax', 'Ent. Tax keyword')
add_category(109, 101, 'Small business Tax')

category_id = int(raw_input('Input the number of category: \n'))

print_parent_category_id_and_name(categories[category_id]['parent_category_id'], categories[category_id]['name'])
print_keywords(category_id)

