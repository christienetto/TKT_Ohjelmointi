import tkinter as tk
from shared_costs.db import save_cost, load_costs
from shared_costs.auth import login

class SharedCostsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shared Costs Tracker")
        
        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()
        
        self.add_button = tk.Button(root, text="Add Cost", command=self.add_cost)
        self.add_button.pack()
        
        self.list_box = tk.Listbox(root)
        self.list_box.pack()
        self.load_costs()
        
    def add_cost(self):
        amount = self.amount_entry.get()
        if amount:
            save_cost(amount)
            self.list_box.insert(tk.END, amount)
            self.amount_entry.delete(0, tk.END)
    
    def load_costs(self):
        costs = load_costs()
        for cost in costs:
            self.list_box.insert(tk.END, cost)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = SharedCostsApp(root)
    root.mainloop()
