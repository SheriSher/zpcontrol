import tkinter as tk
from view import MultiColumnListbox, Main_panel_widget
from xls_creater import Xlsx_creater


class Controler:
	def __init__(self, win):
		self.win = win
		Main_panel(self.win)


class Main_panel:
	def __init__(self, win):
		self.win = win
		self._setup_widgets()
		self.product = Product_info(self.win)

	def _setup_widgets(self):
		self.frame = Main_panel_widget(self.win)
		tk.Button(self.frame.btns_fieled, text="Import Xlsx", command=self.import_xlsx, relief="flat").pack(anchor="w", padx=10)

	def import_xlsx(self):
		Xlsx_creater(data=self.get())


	def get(self):
		data = self.frame.get()
		products_name = self.product.get_all_fields()
		data.update({"Продукт":products_name}) 
		print(f"[RETURN] {data}")
		return data


class Product_info:
	def __init__(self, win):
		self.win = win
		self._setup_btns()

	def _setup_btns(self):
		self.table = MultiColumnListbox(self.win)
		btns_name = ["AddTest", "Add", "Delete","Print"]
		self.btns = []
		for btn_name in btns_name:
			btn = tk.Button(self.table.btns_fieled, text=btn_name, relief="flat", width=8)
			btn.pack()
			self.btns.append(btn)
		self._btn_command_setup()

	def _btn_command_setup(self):
		for btn in self.btns:
			if btn.config("text")[4] == "AddTest":
				btn.config(command=self.table.add_field)
			elif btn.config("text")[4] == "Add":
				btn.config(command=self.table.open_form)
			elif btn.config("text")[4] == "Delete":
				btn.config(command=self.table.del_fileds)
			elif btn.config("text")[4] == "Print":
				btn.config(command=self.get_selected_field)

	def get_all_fields(self):
		data = []
		for item in self.table.tree.get_children():
			data.append(self.table.tree.item(item)["values"])
		return data

	def get_selected_field(self):
		item = self.table.tree.selection()
		data = self.table.tree.item(item)["values"]
		print(f"[RETURN] {data}")
		return data


if __name__ == '__main__':
	root = tk.Tk()
	cotroler = Controler(root)
	root.mainloop()




"""
    def _create_btns(self):
        container = tk.Frame(self.master)
        container.pack(side="right")
"""