#!/usr/bin/env python3
import json

def toDict(input_quad):
    left_context, target_mention, right_context, annot_id = input_quad
    obj = {}
    obj["left_context_token"] = left_context
    obj["y_str"] = []
    obj["right_context_token"] = right_context
    obj["y"] = []
    obj["y_type"] = []
    obj["goal_y_str"] = []
    obj["y_type_str"] = []
    obj["goal_y"] = []
    obj["annot_id"] = annot_id
    obj["mention_span"] = target_mention
    return obj

def toJson(obj):
    return json.dumps(obj)

def writeToFile(filename, jsonObjList):
    with open(filename, "w") as f:
        f.write("\n".join(jsonObjList))
    print("Wrote %s" %filename)

def generateJsonObjects(inputList):
    return [toJson(toDict(inputQuad)) for inputQuad in inputList]

def main(outputFilename, inputList):
    writeToFile(outputFilename, generateJsonObjects(inputList))

if __name__=="__main__":
    import sys
    inputList = [(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])]
    main("test.json", inputList)
