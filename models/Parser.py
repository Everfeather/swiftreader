from enum import Enum
import re

#when finding a enum,struct,class,protocol, create a parsed_object, add to stack, and store. (one in stack is ref to one in store, same instance)
#parsed_object on top of stack is the focused object, add vars, ext to that object
#maintain stack of parsed_objects, when scope decreases (exception of var or func) pop from the stack and 
class Line_Type(Enum):
    VAR = r'\b(?:let|var)\b'
    CLASS = r'class'
    STRUCT = r'struct'
    PROTOCOL = r'protocol'
    METHOD = r'func'
    ENUM = r'enum'
    EXTENSION = r'extension'
    CLOSE_SCOPE = r'}'



class Parser:
    
    def __init__(self):
        self.depth = 0
        self.is_nested = False
        self.parse_functions = { #used as a switch case because python doesn't have those :)
            Line_Type.VAR           : self._parse_var,
            Line_Type.CLASS         : self._parse_class,
            Line_Type.STRUCT        : self._parse_struct,
            Line_Type.PROTOCOL      : self._parse_protocol,
            Line_Type.METHOD        : self._parse_method,
            Line_Type.ENUM          : self._parse_enum,
            Line_Type.EXTENSION     : self._parse_extension,
            Line_Type.CLOSE_SCOPE   : self._parse_extension 
        }

    def parse_file(self,path):
        with open(path, 'r') as file:
            for line in file:
                self.parse_line(line)                

    def parse_line(self,line: str):
        type = self._get_line_type(line)
        if type:
            self.parse_functions.get(type)(line)
        
    def _get_line_type(self, line: [str]) -> Line_Type:
        for type in Line_Type:
            if re.search(type.value,line):
                return type
        return None
        
    def _parse_class(self,line):
        class_name = re.search(r'\b(\w+)\s*:(?=\s)',line)
        class_implements = re.findall(r'(?<=[:,])\s*\w+',line.replace(" ",""))
        print(class_name.group(1))
        print(class_implements)
        return
    
    def _parse_var(self,line):
        #determine static,private,public
        return
    
    def _parse_struct(self,line):
        struct_name = re.search(r'\b(\w+)\s*:(?=\s)',line)
        struct_implements = re.findall(r'(?<=[:,])\w+',line.replace(" ","")) #only protocol
        print(struct_name.group(1))
        print(struct_implements)
        return
    
    def _parse_protocol(self,line):
        return
    
    def _parse_method(self,line):
        return
    
    def _parse_enum(self,line):
        return
    
    def _parse_extension(self,line):
        return
    