appl_revenues = {
    'USA':{
        'iPhone': 1199,
        'iPad': 799,    
        'Macbook': 1299
    },
    'China':{
        'iPhone': 999,
        'iPad': 699,    
        'Macbook': 1099
    },
    'India':{
        'iPhone': 899,
        'iPad': 599,    
        'Macbook': 999
    }
}
for country in appl_revenues:
    # print(appl_revenues[country]['Macbook'])
    print(country, appl_revenues[country])

for country, product_data in appl_revenues.items():
    for product, revenue in product_data.items():
        print(f"{country}: {product} : {revenue}")

