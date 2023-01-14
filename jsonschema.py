import json

class JsonSchema():

	STRING = "string"
	INTEGER = "integer"
	DICTIONARY = "dictionary"


	SNIFFED = {}

	def __init__(self, input_file_path, output_file_name):
		self.input_file_path = input_file_path
		self.output_file_name = output_file_name


	def sniff_schema(self):
		#	OPEN AS FILE OBJECT
		json_file = open(self.input_file_path, 'r')

		#	CONVERT TO DICTIONARY
		data = json.load(json_file)["message"]

		
		sniffed_data = self.traverse_dict(data)

		self.write_json_to_file(sniffed_data, self.output_file_name)


	def list_is_dtype(self, dtype, list__):
			len__ = len(list__)
			sum_ = 0
			for i in list__:
				if type(i) == dtype:
					sum_ += 1
			if sum_ == len__:
				return True 
			return False

	def list_type(self, list_):
		types = [self.datatype(i) for i in list_]
		len_ = len(types)

		

		if self.list_is_dtype(str, list_):
			return "enum"

		elif self.list_is_dtype(dict, list_):
			return "array"

		else:
			return "list"



	def datatype(self, val):
		datatype = type(val)
		if datatype == str:
			return self.STRING
		elif datatype == int:
			return self.INTEGER
		elif datatype == list:
			return self.list_type(val)
		elif datatype == dict:
			return self.DICTIONARY

		else:
			return 0


	def traverse_dict(self, dict_):

		val = {}

		for i in dict_.items():
			if type(i[1]) == dict:
				val[i[0]] = self.traverse_dict(i[1])
				
			else:

				val[i[0]] =  { "type": self.datatype(i[1]), "tag": "", "description":"", "required": False }



		return val

	def write_json_to_file(self, dict_, filename):
		sniffed_json = json.dumps(dict_, indent=4)

		with open(f"schema/{filename}", "w") as outfile:
		    outfile.write(sniffed_json)


sc1 = JsonSchema('data/data_1.json', 'schema_1.json')
sc2 = JsonSchema('data/data_2.json', 'schema_2.json')

sc1.sniff_schema()
sc2.sniff_schema()