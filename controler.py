from view import Main_window


BTNs = ["OK"]


class Button_controler():
	def __init__(self, btnframe):
		self.view = btnframe
		self.btn_list = []

	def create_btn(self, btn_name):
		btn = self.view.set_btn(btn_name)
		self.btn_list.append(btn)
		return btn


def click_ok(fields):
	data = {}
	for field_name, field_val in fields.items():
		# data.append(field_val.get())
		data[field_name] = field_val.get()
	print(data)


def runapp():
	win = Main_window()
	win.geometry("600x600")
	form_view = win.get_form()
	
	btn_control = Button_controler(form_view.btnframe)
	btn_ok = btn_control.create_btn(BTNs[0])
	btn_ok.config(command=lambda: click_ok(form_view.get_fields()))


	win.mainloop()



