# Python3 tutorials

## How to

Install python3 and modules

```sh
# Check
which python3

# Install
sudo apt install python3 python3-tk python3-pyotp python3-openpyxl -y
```


## List Comprehension
- https://docs.python.org/3/tutorial/datastructures.html
- https://github.com/atomjoy/tutorials/tree/main/Python/treeview
- https://www.geeksforgeeks.org/python-list-comprehension

```python
def get_checked(self, attr="checked"):
    # List items
    children = ttk.Treeview.get_children(self)
    
    # List syntax
    # Syntax: newList = [ expression(element) for element in oldList if condition ]
    # Sample (2 x for): lt = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
    
    # Boolean array [True, False]
    ck = ["checked" in self.item(c, "tags") for c in children]
    print(attr.capitalize(), ck)
    
    # Ids array [1,2,4]
    ck = [c for c in children if attr in self.item(c, "tags")] 
    print(attr.capitalize(), ck)
    
    # For loop
    ck = []
    for c in children:
        if "checked" in self.item(c, "tags"):
            ck.append(c)
    print(attr.capitalize(), ck)
    
    # Return array
    return ck
```
