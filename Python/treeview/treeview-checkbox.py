# sudo apt install python3 python3-pyotp python3-tk python3-openpyxl

# https://copyprogramming.com/howto/how-to-create-a-tree-view-with-checkboxes-in-python
# https://pythonassets.com/posts/treeview-in-tk-tkinter
# https://web.archive.org/web/20150321101604/http://effbot.org/tkinterbook/tkinter-events-and-bindings.htm

import tkinter as tk
import tkinter.ttk as ttk

class CheckboxTreeview(ttk.Treeview):
    """
        Treeview widget with checkboxes left of each item.
        The checkboxes are done via the image attribute of the item, so to keep
        the checkbox, you cannot add an image to the item.
    """
    def __init__(self, master=None, cols=None, **kw):
        if cols == None:
            cols=("Id", "Name")
        ttk.Treeview.__init__(self, master, **kw, columns=cols)
        # checkboxes are implemented with pictures
        self.im_checked = tk.PhotoImage(file='checked.png')
        self.im_unchecked = tk.PhotoImage(file='unchecked.png')
        self.im_tristate = tk.PhotoImage(file='tristate.png')
        self.tag_configure("unchecked", image=self.im_unchecked)
        self.tag_configure("tristate", image=self.im_tristate)
        self.tag_configure("checked", image=self.im_checked)
        # check / uncheck boxes on click
        self.bind("<Button-1>", self.box_click, True)
        # headings
        self.heading("#0", text="Action", anchor='w')
        self.heading("#1", text="Id", anchor='w')
        self.heading("#2", text="Name", anchor='w')

    def insert(self, parent, index, iid=None, **kw):
        """ same method as for standard treeview but add the tag 'unchecked'
            automatically if no tag among ('checked', 'unchecked', 'tristate')
            is given """
        if not "tags" in kw:
            kw["tags"] = ("unchecked",)
        elif not ("unchecked" in kw["tags"] or "checked" in kw["tags"]
                  or "tristate" in kw["tags"]):
            kw["tags"] = ("unchecked",)
        ttk.Treeview.insert(self, parent, index, iid, **kw)

    def check_descendant(self, item):
        """ check the boxes of item's descendants """
        children = self.get_children(item)
        for iid in children:
            self.item(iid, tags=("checked",))
            self.check_descendant(iid)

    def check_ancestor(self, item):
        """ check the box of item and change the state of the boxes of item's
            ancestors accordingly """
        self.item(item, tags=("checked",))
        parent = self.parent(item)
        if parent:
            children = self.get_children(parent)
            b = ["checked" in self.item(c, "tags") for c in children]
            if False in b:
                # at least one box is not checked and item's box is checked
                self.tristate_parent(parent)
            else:
                # all boxes of the children are checked
                self.check_ancestor(parent)
    def tristate_parent(self, item):
        """ put the box of item in tristate and change the state of the boxes of
            item's ancestors accordingly """
        self.item(item, tags=("tristate",))
        parent = self.parent(item)
        if parent:
            self.tristate_parent(parent)
    def uncheck_descendant(self, item):
        """ uncheck the boxes of item's descendant """
        children = self.get_children(item)
        for iid in children:
            self.item(iid, tags=("unchecked",))
            self.uncheck_descendant(iid)
    def uncheck_ancestor(self, item):
        """ uncheck the box of item and change the state of the boxes of item's
            ancestors accordingly """
        self.item(item, tags=("unchecked",))
        parent = self.parent(item)
        if parent:
            children = self.get_children(parent)
            b = ["unchecked" in self.item(c, "tags") for c in children]
            if False in b:
                # at least one box is checked and item's box is unchecked
                self.tristate_parent(parent)
            else:
                # no box is checked
                self.uncheck_ancestor(parent)
    def box_click(self, event):
        """ check or uncheck box when clicked """
        x, y, widget = event.x, event.y, event.widget
        elem = widget.identify("element", x, y)        
        if "image" in elem:
            # a box was clicked
            item = self.identify_row(y)
            tags = self.item(item, "tags")
            if ("unchecked" in tags) or ("tristate" in tags):
                self.check_ancestor(item)
                self.check_descendant(item)
            else:
                self.uncheck_descendant(item)
                self.uncheck_ancestor(item)
        self.get_checked()

    def get_checked(self, attr="checked"):
        children = ttk.Treeview.get_children(self)
        # Syntax: newList = [ expression(element) for element in oldList if condition ] 
        # ck = ["checked" in self.item(c, "tags") for c in children] # [True, False]
        ck = [c for c in children if attr in self.item(c, "tags")] # [1,2,4]
        print(attr.capitalize(), ck)
        # ck = []
        # for c in children:
        #     if "checked" in self.item(c, "tags"):
        #         ck.append(c)
        # print("Checked", ck)
        return ck

    def key(event):
        print("pressed", repr(event.char))

if __name__ == '__main__':
    root = tk.Tk()
    t = CheckboxTreeview(root, show=["tree", "headings"], cols=("Age", "Name"))
    t.pack()
    # Items
    t.insert('', tk.END, id="0", values=("18", "Max"))
    t.insert('', tk.END, id="1", values=("23", "Alex"))
    t.insert('', tk.END, id="2", values=("17", "Alice"))
    t.insert('', tk.END, id="3", values=("34", "john"))
    # Items and Subitems
    # t.insert("", 0, "1", text="1")
    # t.insert("1", "end", "11", text="1")
    # t.insert("1", "end", "12", text="2")
    # t.insert("12", "end", "121", text="1")
    # t.insert("12", "end", "122", text="2")
    # t.insert("122", "end", "1221", text="1")
    # t.insert("1", "end", "13", text="3")
    # t.insert("13", "end", "131", text="1")
    root.mainloop()
