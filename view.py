import tkinter as tk
import tkinter.ttk as ttk



class MultiColumnListbox():
    """use a ttk.TreeView as a multicolumn ListBox"""
    car_header = ['Наименование товара', 'Количество', 'Цена', 'Сумма без НДС', 'Сумма включая НДС', 'НДС %']

    def __init__(self, master=None):
        self.master = master
        self.tree = None
        self._setup_widgets()
        self._build_tree()

    def _setup_widgets(self, ):
        self.mainframe = tk.Frame(self.master)
        self.mainframe.pack(fill='both', expand=True)
        self._create_tree()
        self.btns_fieled = tk.Frame(self.mainframe, bg="lightgray")
        self.btns_fieled.pack(expand=1, fill="both", side="right")
        # self._create_btns()

    def _create_tree(self):
        container = ttk.Frame(self.mainframe)
        container.pack(expand=1, fill="both", side="left")
        self.tree = ttk.Treeview(columns=self.car_header, show="headings", selectmode="browse")
        vsb = ttk.Scrollbar(orient="vertical",
            command=self.tree.yview)
        hsb = ttk.Scrollbar(orient="horizontal",
            command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set,
            xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=container)
        vsb.grid(column=1, row=0, sticky='ns', in_=container)
        hsb.grid(column=0, row=1, sticky='ew', in_=container)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

    def _build_tree(self):
        for col in self.car_header:
            self.tree.heading(col, text=col.title(), command=lambda c=col: self.sortby(c, 0))

    def add_field(self, field=('Сканер на кассе', '4', '4050', '16200', '19440', '20')):
    	self.tree.insert("", "end", values=field)

    def get_field(self):
    	for selection in self.tree.selection():
	    	item = self.tree.item(selection)
	    	print(item["values"])
	
    def del_fileds(self):
        for selection in self.tree.selection():
            self.tree.delete(selection)

    def open_form(self):
    	win = tk.Toplevel()
    	Form_product_info(win, fields=['Наименование', 'Количество', 'Цена', 'НДС %'], table=self)
    	win.grab_set()		

    def sortby(self, col, descending):
	    data = [(self.tree.set(child, col), child) \
	        for child in self.tree.get_children('')]

	    data.sort(reverse=descending)
	    for ix, item in enumerate(data):
	        self.tree.move(item[1], '', ix)

	    self.tree.heading(col, command=lambda col=col: self.sortby(col, \
	        int(not descending)))


class Form_product_info(tk.Frame):
	def __init__(self, master=None, fields=[], table=None, *args, **kwargs):
		super().__init__(master=master, *args, **kwargs)
		self.master = master
		self.fields = fields
		self.table = table
		self.ents = []
		self._setup_widgets()
		self.pack(expand=1, fill="both")

	def _setup_widgets(self):
		if self.fields:
			for field in self.fields:
				self._create_field(field)
		self.btn_ok = tk.Button(self, text="OK")
		self.btn_ok.config(command=self.click_ok)
		self.btn_ok.pack()

	def get(self):
		ent_values = []
		for ent in self.ents:
			entval = ent.get()
			ent_values.append(entval)

		return dict(zip(self.fields,ent_values))

	def click_ok(self):
		if self.table:
			data = self.get()
			name = data["Наименование"]
			num = data["Количество"]
			price = data["Цена"]
			NDSproc = data["НДС %"]
			
			data = self.canculation(name, num, price, NDSproc)
			print(data)
			self.table.add_field(field=data)

	def canculation(self, name, num, price, NDSproc):
		sum_price = float(num)*float(price)
		NDS = sum_price / 100 * float(NDSproc)
		print(NDS)
		sum_priceNDS = sum_price + NDS
		data = (name, num, price, sum_price, sum_priceNDS, NDSproc)
		return data

	def _create_field(self, field_name):			
		conteiner = tk.Frame(self)
		conteiner.pack()
		tk.Label(conteiner, text=field_name, width=12, anchor="w").pack(side="left", pady=2)
		ent = tk.Entry(conteiner)
		ent.pack(side="right", fill="x", expand=1)
		self.ents.append(ent)


class Main_panel_widget():
	fields = ["Поставщик", "Накладная", "Дата"]
	
	def __init__(self, win=None):
		self.win = win
		self._setup_widgets()

	def _setup_widgets(self):
		self.mainframe = tk.Frame(self.win, pady=8, padx=100)
		self.mainframe.pack(expand=1, fill="both")
		self._create_form()
		self._create_btns_field()

	def _create_form(self):
		self.container_for_form = tk.Frame(self.mainframe, pady=6)
		self.container_for_form.pack(fill="both", side="left")
		self.ents = []
		for field in self.fields:
			container = tk.Frame(self.container_for_form, pady=2)
			container.pack(anchor="w")
			tk.Label(container, text=field, anchor="w", width=10, font="11").pack(side="left")
			ent = tk.Entry(container)
			ent.pack(side="right")
			self.ents.append(ent)

	def _create_btns_field(self):
		self.btns_fieled = tk.Frame(self.mainframe)
		self.btns_fieled.pack(expand=1, fill="both", side="right", padx=40, pady=2)

	def get(self):
		ent_value = [ent.get() for ent in self.ents]
		return dict(zip(self.fields, ent_value))
		





if __name__ == '__main__':
    root = tk.Tk()
    root.title("Multicolumn Treeview/Listbox")
    listbox = MultiColumnListbox()
    root.mainloop()

