from models.Parser import Parser

path = input("enter the file path: ")
p = Parser()
p.parse_file(path)


# p._parse_class("class SomeSubclass: SomeSuperclass, protocol {")