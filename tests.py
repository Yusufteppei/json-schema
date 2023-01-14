import pytest, json
from jsonschema import JsonSchema

class TestJsonSchema():

	sc = JsonSchema("data/data_1.json", "test_schema.json")


	def test_datatype(self):

		assert self.sc.datatype("tres") == "string"
		assert self.sc.datatype(["essd", "fgd", "gtegehth"]) == "enum"
		assert self.sc.datatype([{"ER": "tgtr"}, {"werdsf":"fdht"}]) == "array"


	def test_list_is_dtype(self):

		assert self.sc.list_is_dtype(str, ["asd", "fdg", "ytyjh"]) == True
		assert self.sc.list_is_dtype(dict, [{"s":"gfhj"}, {"s":7}]) == True


	def test_sniff_schema(self):
		pass


	def test_traverse_dict(self):
		assert self.sc.traverse_dict(TEST_DATA)["message"]["battle"]["id"]["type"] == "string"
		assert self.sc.traverse_dict(TEST_DATA)["message"]["battle"]["participants"]["type"] == "array"
		assert self.sc.traverse_dict(TEST_DATA)["message"]["participantIds"]["type"] == "enum"


	def test_write_json_to_file(self):
		pass


TEST_DATA = {
    "attributes": {
      "appName": "ABCDEFG",
    },
    "message": {
      "battle": {
        "id": "ABCDEFGHIJKLMNOPQR",
        "name": "ABCDEFGHIJKLMNOPQRSTUVWX",
        "orientation": "ABCDEFGHIJKLMNO",
        "settings": {
          "minParticipants": 942,
          "duration": 200,
          "archetype": {
            "name": "ABCDEFGHIJKLMNOPQRS",
            "iconId": "ABCDEFGHIJKLMNOPQRST"
          }
        },
        "status": "ABCDEFGHIJKL",
        "creator": {
          "id": "ABCDEFGHIJKLMNOPQRSTUVWXYZA",
          "nickname": "ABCDEFGHI"
        },
        "participants": [
          {
            "user": {
              "id": "ABCDEFGHIJKLMN",
              "nickname": "ABCDEFGHIJKLMN",
              "title": "ABCDEFGHIJK",
            },
            "creator": False,
            "performance": "ABCDEFGHIJKLMNOPQRSTUVW"
          }
        ]
      },
      "joiner": {
        "id": "ABCDEFGHIJKLMNOPQRSTUVWXYZAB",
        "nickname": "ABCDEFGHIJKLMNO",
      },
      "participantIds": [
        "ABCDEFGHIJKLMNOPQRST",
      ]
    }
  }