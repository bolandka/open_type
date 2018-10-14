#!/usr/bin/env python3

import json

def get_predictions(filename):
    return json.load(open(filename, "r"))

def print_type_labels(prediction_dict):
    for k, v in prediction_dict.items():
        print("%s (key): %s" %(k,v['pred']))
        
def get_types_for_mention(prediction_dict, mention_annotation_id):
    return prediction_dict.get(mention_annotation_id)

def get_predicted_types_for_mention(prediction_dict, mention_annotation_id):
    try:
        return prediction_dict.get(mention_annotation_id).get('pred')
    except AttributeError as e:
        print(e)
        print(mention_annotation_id)
        print(prediction_dict.get(mention_annotation_id))
        return ""

def get_gold_types_for_mention(prediction_dict, mention_annotation_id):
    return prediction_dict.get(mention_annotation_id).get('gold')


if __name__=="__main__":
    import sys
    prediction_fname = sys.argv[1]
    #print(print_type_labels(get_predictions(prediction_fname)))
    mention_annotation_id = sys.argv[2]
    print(get_predicted_types_for_mention(get_predictions(prediction_fname), mention_annotation_id))
