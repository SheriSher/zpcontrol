import tkinter as tk

class Main_window(tk.Tk):
	def __init__(self):
		super().__init__()
		self.form = Form(self, fields_name=["Num", "Provider","Data"])
		self.form.pack(expand=0, fill="both")

	def get_form(self):
		return self.form


class Form(tk.Frame):
	def __init__(self, master=None, fields_name=[], **kwargs):
		super().__init__(master=master, **kwargs)
		self.fields_name = fields_name
		self.fields = {}
		self.set_fields()
		self.set_btnframe()

	def set_fields(self):
		if self.fields_name:
			for field in self.fields_name:
				self.create_field(field)

	def get_fields(self):
		return self.fields

	def set_btnframe(self):			
		self.btnframe = Btnframe(self)
		self.btnframe.pack()

	def create_field(self, field_name):			
		conteiner = tk.Frame(self)
		conteiner.pack()
		tk.Label(conteiner, text=field_name, width=8, anchor="w").pack(side="left", pady=2)
		ent = tk.Entry(conteiner)
		ent.pack(side="right", fill="x", expand=1)
		self.fields[field_name] = ent


class Btnframe(tk.Frame):
	def __init__(self, master=None, **kwargs):
		super().__init__(master=master, **kwargs)

	def set_btn(self, btn_name):
		btn = tk.Button(self, text=btn_name)
		btn.pack(side="right")
		return btn



if __name__ == '__main__':
	win = Main_window()

	win.mainloop()