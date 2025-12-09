a = 100
b = 50
c = 25
d = 4
weight_of_book = a * b * c * d
Mb = 1.44
Mb_to_b = Mb * 1024**2
books = Mb_to_b // weight_of_book
print("Количество книг, помещающихся на дискету:", round(books, ))
