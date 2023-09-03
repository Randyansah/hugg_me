from transformers import pipeline
import tensorflow
import argparse

def main():
    selection="""
        WELCOME TO THE HUGGING FACE NLP SYSTEM
        1==PREDICT WHICH TOP IS DISCUSSED IN  A SENTENCE
        2==CLASSIFY WHETHER A SENTENCE IS POSITIVE OR NEGATIVE
        3==PREDICTING MISSING WORDS IN A SENTENCE
        4==GENERATE TEXT
        5==IDENTIFY ENTITIES SUCH AS ORGANIZATION,PERSONS OR LOCATIONS
        6==SUMMARIZATION
        7==TRANSLATION
        8==GET VE9CTOR EXTRACTION OF A TEXT
        9==ANSWERING QUESTIONS

        """
    print(selection)
    input_select()
    x=nlp()
    print(x)
    
    
def input_select():  
    global input_selection  
    try:
        input_selection=int(input('ENTER OPTION>>'))
    except ValueError:
            print('CHECK YOUR VALUE \n ENTER AN INTEGER')
    
         


def nlp():

    try :            
        txt=str(input('ENTER TEXT>>'))
    except ValueError:
            print('CHECK VALUES')    
    match input_selection:
                        case 1:
                            generator=pipeline('zero-shot-classification')
                            answer=generator(txt)
                        case 2:
                            generator=pipeline('sentiment-analysis')
                            answer=generator(txt)
                        case 3:
                            generator=pipeline('fill-mask')
                            answer=generator(txt)
                        case 4:
                            generator=pipeline('text-generation')
                            answer=generator(txt)
                        case 5:
                            generator=pipeline('ner')
                            answer=generator(txt)
                        case 6:
                            generator=pipeline('summarization')
                            answer=generator(txt)
                        case 7:
                            generator=pipeline('translation')
                            answer=generator(txt)
                        case 8:
                            generator=pipeline('feature_extraction')
                            answer=generator(txt)
                        case 9:
                            generator=pipeline('question_answering')
                            answer=generator(txt)
    return answer
    #except ValueError:
            #print('CHECK VALUES')
parser=argparse.ArgumentParser(description='Hugging Face is an \
                               application to do some NATURAL LANGUAGE\
                                PROCESSING tasks such as summarization, \
                               translation, text generation, text vector \
                               extration, answering questions etc')     
parser.add_argument("--main",help="This will perform various tasks",action="store_true") 
args=parser.parse_args()      

if __name__=="__main__":
     main()

                    

                    
                    