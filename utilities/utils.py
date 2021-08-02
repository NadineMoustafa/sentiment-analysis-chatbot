
import csv
import json
import codecs
import pandas as pd
# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):
     
    # create a dictionary
    data = {"dataset": []}
    data_sample = {
    }
    # Open a csv reader called DictReader
    str_context_ = 2
    str_pattern_ = 4
    str_response_ = 7
    numberOFRows = 100
    # with open(csvFilePath) as csvf:
    # csvReader = csv.DictReader(csvf)
    
    csvReader =csv.reader(codecs.open(csvFilePath, 'rU', 'utf-16'))
    print(csvReader)
        
    # Convert each row into a dictionary
    # and add it to data
    # c = True
    rowIndex = 0
    for rows in csvReader:
        rowIndex += 1
        # Assuming a column named 'No' to
        # be the primary key
        if rowIndex> 1:
            print(rows)
            context = rows[str_context_]
            pattern = rows[str_pattern_]
            response = rows[str_response_]
            if(context in data_sample and len(data_sample[context]['patterns'])>0):
                
                patterns_ = data_sample[context]['patterns']
                responses_ = data_sample[context]['responses']
                patterns_.append(pattern.replace("_comma_", ","))
                responses_.append(response.replace("_comma_", ","))
                context_={}
                context_['patterns']= patterns_
                context_['responses']= responses_
                data_sample[context] = context_
            else:
                patterns_ =[]
                responses_ = []
                print(context)
                print(pattern)

                if context is not None:
                    patterns_.append(pattern.replace("_comma_", ","))
                    responses_.append(response.replace("_comma_", ","))
                    context_={}
                    context_['patterns']= patterns_
                    context_['responses']= responses_
                    data_sample[context] = context_
            if rowIndex > numberOFRows:
                break

    for context in data_sample:
        sample = {}
        sample['context'] = context
        sample['patterns'] = data_sample[context]['patterns']
        sample['responses'] = data_sample[context]['responses']
        data["dataset"].append(sample)

    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


def make_json_v2(csvFilePath, jsonFilePath):
     
    # create a dictionary
    data = {"dataset": []}
    context_dict={}
    data_sample = {
    }
    # Open a csv reader called DictReader
    str_context_ = "context"
    str_pattern_ = "translated_prompt"
    str_response_ = "translated_utterance"
    numberOFRows = 100
    # with open(csvFilePath) as csvf:
    # csvReader = csv.DictReader(csvf)
    
    csvfile = open(csvFilePath, 'r')
    f = pd.read_csv(csvfile, usecols = [str_context_,str_pattern_,str_response_])
    # print(f.head())


    for index, rows in f.iterrows():
        # print(rows['context'], rows['translated_prompt'])
        context = rows[str_context_]
        pattern = rows[str_pattern_]
        response = rows[str_response_]
        if(context in data_sample and len(data_sample[context]['patterns'])>0):
            context_dict[context] = context_dict[context] + 1 
            patterns_ = data_sample[context]['patterns']
            responses_ = data_sample[context]['responses']
            patterns_.append(pattern)
            responses_.append(response)
            context_={}
            context_['patterns']= patterns_
            context_['responses']= responses_
            data_sample[context] = context_
        else:
            patterns_ =[]
            responses_ = []
            # print(context)
            # print(pattern)

            if context is not None:
                context_dict[context] = 1
                patterns_.append(pattern)
                responses_.append(response)
                context_={}
                context_['patterns']= patterns_
                context_['responses']= responses_
                data_sample[context] = context_

    print(context_dict)
    for context in data_sample:
        sample = {}
        sample['context'] = context
        sample['patterns'] = data_sample[context]['patterns']
        sample['responses'] = data_sample[context]['responses']
        data["dataset"].append(sample)

    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w') as jsonf:
        jsonf.write(json.dumps(data, indent=4, ensure_ascii = False))       
# Driver Code


def make_json_v3(csvFilePath, jsonFilePath):
     
    # create a dictionary
    data = {"dataset": []}
    context_dict={}
    data_sample = {
    }
    # Open a csv reader called DictReader
    str_context_ = "context"
    str_pattern_ = "translated_prompt"
    str_response_ = "translated_utterance"
    numberOFRows = 100
    # with open(csvFilePath) as csvf:
    # csvReader = csv.DictReader(csvf)
    
    csvfile = open(csvFilePath, 'r')
    f = pd.read_csv(csvfile, usecols = [str_context_,str_pattern_,str_response_], encoding="utf-16")
    # print(f.head())
    fillter_context =["joyful", "sad"]
    old_context = ""
    old_patteren = ""
    for index, rows in f.iterrows():
        # print(rows['context'], rows['translated_prompt'])
       
        context = rows[str_context_]
        if context in fillter_context:
            if context not in context_dict:
                context_dict[context] = 1
            # context += str(1)

            pattern = rows[str_pattern_]
            response = rows[str_response_]
            if context == old_context and old_patteren == pattern:
                patterns_ = data_sample[context + str(context_dict[context])]['patterns']
                responses_ = data_sample[context + str(context_dict[context])]['responses']
                patterns_.append(pattern)
                responses_.append(response)
                context_={}
                context_['patterns']= patterns_
                context_['responses']= responses_
                data_sample[context+str(context_dict[context])] = context_ 
            else:
                patterns_ =[]
                responses_ = []
                if context is not None:
                    if not old_context == "":
                        # print(context_dict, old_context)
                        context_dict[old_context] = context_dict[old_context] + 1
                    patterns_.append(pattern)
                    responses_.append(response)
                    context_={}
                    context_['patterns']= patterns_
                    context_['responses']= responses_
                    data_sample[context + str(context_dict[context])] = context_
            old_context = context
            old_patteren = pattern
    
    for context in data_sample:
        sample = {}
        sample['context'] = context
        sample['patterns'] = data_sample[context]['patterns']
        sample['responses'] = data_sample[context]['responses']
        data["dataset"].append(sample)


    with open(jsonFilePath, 'w') as jsonf:
        jsonf.write(json.dumps(data, indent=4, ensure_ascii = False))       

 
# Decide the two file paths according to your
# computer system
csvFilePath = r'/Users/abdelrahman/Desktop/Abdelrahman/Python/Chatbot/Dataset/Train/fil.csv'
jsonFilePath = r'/Users/abdelrahman/Desktop/Abdelrahman/Python/Chatbot/Dataset/Train/train_V1.json'
 
make_json_v3(csvFilePath,jsonFilePath)
