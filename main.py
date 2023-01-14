import json
import sys
from jsonschema import JsonSchema



def main():
	input_data = str(input("Input the path of the input data : "))
	output_file_name = str(input("Input the name of the output file : "))

	sc = JsonSchema(input_data, output_file_name)
	sc.sniff_schema()

	print(f"Schema available in schema/{output_file_name}")

if __name__ == "__main__":
	main()