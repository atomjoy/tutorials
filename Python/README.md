# Python3 
Tutorials

## Install python3 and modules

```sh
sudo apt install python3 python3-pil python3-tk python3-pyotp python3-openpyxl -y
sudo apt install python3-pip python3-full python3-dev python3-tools -y
sudo apt install python3-torch python3-torchvision -y
```

## Install customtkinter

Dziwacznie, się nie instaluje trzeba cudować ... Debian 12

```sh
# Check Debian 12
sudo which python3
sudo python3 --version
sudo pip3 --version
sudo pipx --version

# Virtual env python3 Debian 12 with python3-full python3-pip
sudo python3 -m venv ~/tutorial-venv
# Add
sudo ~/venv/bin/pip3 install Pillow
sudo ~/venv/bin/pip3 install darkdetect
sudo ~/venv/bin/pip3 install customtkinter

# Run virtual env
source tutorial-venv/bin/activate

# Run script
python3 ~/tutorial-venv/main.py

# Deactivate virtual env
deactivate
```
## Exxamples

### List Comprehension
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

## About

- Tkinter słabe te okienka
- Na windowsie CustomTkinter śmiga a na Debianie CustomTkinter się nie chce instalować poludzku 🤯
- Do operacji na plikach, obrazkach i aplikacji do konwertowania
- Chyba lepiej przekierować zainteresowania na WebDev, C# WPF lub Unity3d / Unreal Engine 🙂
