# display_python_dictionaries
Library for displaying dictionaries in python vs. >= 3

### Dictionaries in readable format

**usage:** pdict.detail(obj, level=0, space=3, metric=[0], sign="-")

```python
>>> import pdict  
>>> myDict = {12.98675:  [{1:3}], "test2": [(1,{1:'qrest1',2:'qrest2'}), (3,4)], }  
>>> pdict.displ(myDict, space=5) ```

**optional arguments:**  
    -h, --help  show this help message and exit  
    space=3     determine what width to use for the levels in detail function  
    level=0     determine starting level  

**Description:**  
This file can be used as a module with 2 methods: detail() and summary()  
The file can be used also as a stand alone code for further exploring dicts
