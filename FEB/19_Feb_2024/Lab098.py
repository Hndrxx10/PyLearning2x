class Cal:
    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


object_ref = Cal()
result = object_ref.sum(3, 4)
object_ref.div(10,5)
object_ref.sub(10,5)
object_ref.mul(10,5)
print(result)