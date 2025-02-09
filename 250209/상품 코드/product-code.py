class product:
    def __init__(self, name="codetree", code=50):
        self.name = name
        self.code = code
product0 = product()
print(f"product {product0.code} is {product0.name}")
name1, code1 = input().split()
code1 = int(code1)
product1 = product(name1, code1)

print(f"product {product1.code} is {product1.name}")