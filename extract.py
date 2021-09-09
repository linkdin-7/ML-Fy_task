# Your imports go here
import logging
import json
import os
import re


logger = logging.getLogger(__name__)

'''
    Given a directory with receipt file and OCR output, this function should extract the amount

    Parameters:
    dirpath (str): directory path containing receipt and ocr output

    Returns:
    float: returns the extracted amount

'''
def extract_amount(dirpath: str) -> float:

    logger.info('extract_amount called for dir %s', dirpath)
    # your logic goes here

    # Reading of the json file
    with open(os.path.join(dirpath,'ocr.json'), mode='r', encoding="utf-8") as f:
        data = (json.load(f)).get("Blocks")
    
    # Intialisation of the variable
    text = []
    amount = 0.0
    main_amount = 0.0


    # We have all our Required Data in the Text 
    for i in data:
        try:
            # Conversion to upper 
            text.append(i['Text'].upper()) 
        except KeyError:
            continue


    # To extract the amount
    for k in text:
        if "," in k:
            k = k.replace(",",'')

        value = re.findall(r"[+-]?\d+\.\d+", k)

        # We want the total price and in every bill the maximum float value will the amount
        if len(value) > 0:
            amount = float(value[0])
            main_amount = max( main_amount,amount)
    return  main_amount
