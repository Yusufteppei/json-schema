##	THE PROGRAM CAN BE RUN ON THE TERMINAL OR AS A LIBRARY

##	TO RUN ON THE TERMINAL, RUN python main.py AND FOLLOW THE PROMPT




##	TO USE AS A LIBRARY

##	IMPORT jsonschema

import jsonschema



##	CREATE A JSONSCHEMA OBJECT

##	THE FIRST ARGUMENT MUST BE THE PATH TO THE JSON FILE

js = JsonSchema(input_file, output_file)




##	EXECUTE THE sniffschema() METHOD
 
js.sniff_schema()



##	THE OUTPUT FILE WILL BE STORED IN THE 'schema" DIRECTORY

