from src.triangle import Triangle

# Проверяем, что если треугольник создать нельзя, то возврящаетя None
triangle = Triangle(1, 2, 3)
if triangle is None:
    print(f'Triangle is None, type = {type(triangle)}')
else:
    print(f"Not None, type = {type(triangle)}")
