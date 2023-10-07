from transformers import pipeline
import tensorflow
#import argparse

'''def main():
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
    #print(selection)
    #input_select()
    #x=nlp()
    #print(x)'''
    
selection="""
        WELCOME TO THE HUGGING FACE NLP SYSTEM \n
        1~PREDICT WHICH TOP IS DISCUSSED IN  A SENTENCE \n
        2~CLASSIFY WHETHER A SENTENCE IS POSITIVE OR NEGATIVE \n
        3~PREDICTING MISSING WORDS IN A SENTENCE \n
        4~GENERATE TEXT \n
        5~IDENTIFY ENTITIES SUCH AS ORGANIZATION,PERSONS OR LOCATIONS \n
        6~SUMMARIZATION \n
        7~TRANSLATION \n
        8~GET VE9CTOR EXTRACTION OF A TEXT\n
        9~ANSWERING QUESTIONS\n

        """    
    
'''def input_select():  
    global input_selection  
    try:
        input_selection=int(input('ENTER OPTION>>'))
    except ValueError:
            print('CHECK YOUR VALUE \n ENTER AN INTEGER')
    return input_selection        
input_select_ion=input_select()

def add(x):
    return x + 1 '''
         


def nlp(input_selection,txt):
    global answer
    
    '''try:
        input_selection=int(input('ENTER OPTION>>'))
    except ValueError:
            print('CHECK YOUR VALUE \n ENTER AN INTEGER')

    try :            
        txt=str(input('ENTER TEXT>>'))
    except ValueError:
            print('CHECK VALUES')'''    
    
    
    match input_selection:
        case 1:
            generator=pipeline('zero-shot-classification')
            answer=generator(txt)
            return answer
        case 2:
            generator=pipeline('sentiment-analysis')
            answer=generator(txt)
            return answer
        case 3:
            generator=pipeline('fill-mask')
            answer=generator(txt)
            return answer
        case 4:
            generator=pipeline('text-generation')
            answer=generator(txt)
            return answer
        case 5:
            generator=pipeline('ner')
            answer=generator(txt)
            return answer
        case 6:
            generator=pipeline('summarization')
            answer=generator(txt)
            return answer
        case 7:
            generator=pipeline('translation')
            answer=generator(txt)
            return answer
        case 8:
            generator=pipeline('feature_extraction')
            answer=generator(txt)
            return answer
        case 9:
            generator=pipeline('question_answering')
            answer=generator(txt)
            return answer
    #return answer
    
    #except ValueError:
            #print('CHECK VALUES')
'''def command_li():            
    parser=argparse.ArgumentParser(description='Hugging Face is an \
                               #application to do some NATURAL LANGUAGE\
                                #PROCESSING tasks such as summarization, \
                               #translation, text generation, text vector \
                               #extration, answering questions etc')     
    parser.add_argument("--main",help="This will perform various tasks",action="store_true") 
    args=parser.parse_args()
    return args'''
  
#if __name__=="__command_li__":
    #command_li()
             

#if __name__=="__main__":
    #main()

                    

                    
                    