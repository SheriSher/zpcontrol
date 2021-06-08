import xlsxwriter


class Xlsx_creater:
	vert_names = ["Дата документа", "Номер документа", "Описание", "Поставщик"]
	hor_names = ["Наименование товара", "Единица измерения",
				"Количество", "Цена", "Сумма без НДС", 
				"Сумма включая НДС", "НДС %", 
				"ГТД", "Страна", "Категория", 
				"Группа", "Учетная Группа", "Для магазина"]

	def __init__(self, data):
		self.data = self.data_validation(data)
		self.workbook, self.worksheet = self.create_xlsx()
		self.add_fields()
		self.workbook.close()

	def create_xlsx(self):
		workbook = xlsxwriter.Workbook('filename.xlsx')
		worksheet = workbook.add_worksheet()
		return workbook, worksheet

	def data_validation(self, data):
		data_vert = [data["Дата"], data["Накладная"], f'{data["Накладная"]} {data["Дата"]}', data["Поставщик"]]
		data_products = [products for products in data["Продукт"]]
		data_hor = []
		for product in data_products:
			new_data = [product[0], "Шт.",
						product[1], product[2], 
						product[3], product[4], 
						product[5], 0, "Россия",
						"104.ТМЦ прочие", None, 
						"ТМЦ10-0420",None]
			data_hor.append(new_data)
		return data_vert, data_hor

	def add_fields(self):
		self._setup_fields_vert(0, 0)
		self._setup_fields_hor(5, 0)

	def _setup_fields_vert(self, x=0, y=0):
		for name in self.vert_names:
			self.worksheet.write(x, y , name)
			x += 1
		x, y = 0, 1
		for val in self.data[0]:
			self.worksheet.write(x, y , val)
			x += 1

	def _setup_fields_hor(self, x=5, y=0):	
		for name in self.hor_names:
			self.worksheet.write(x, y , name)
			y += 1
		x, y = 5, 0
		for products in self.data[1]:
			x += 1
			for product in products:
				self.worksheet.write(x, y , product)
				y += 1
			y = 0

if __name__ == '__main__':
	data = {'Поставщик': '1', 
			'Накладная': '123',
			'Дата': '10.02.1996',
			'Продукт': [['Сканер на кассе', 4, 4050, 16200, 19440, 20],
						['Сканер на кассе', 4, 4050, 16200, 19440, 20]]}
	testcreater = Xlsx_creater(data)