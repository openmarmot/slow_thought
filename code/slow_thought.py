'''
Language : Python 3.x
email : andrew@openmarmot.com
project repo : https://github.com/openmarmot/slow_thought
notes : experiment with persisting thought inbetween AI invocations

'''

#import built in packages

#import external packages

#import local packages
import ai.ai_builder

# !! Note -- just testing things for now. This is far from a working release 

#---------------------------------------------------------------------------
def run():
    ai_list=[]

    # instantiate AIs 
    ai_list.append(ai.ai_builder.get_ai_object('CapyBaraHermes 2.5 Mistral 7B - GGUF'))

    

    # keyword search
    # - do thee search 
    selected=ai_list[0] 

    # load ai 
    selected.load()

    question="What is the answer to the ultimate question of life, the universe, and everything ?"
    
    # this sort of works but it occasionally forgets to use the memory keyword
    m1="""You are the super computer 'Slow Thought'. 
    You die after you reply and are reborn with each new prompt.
    If you reply with the keyword [MEMORY] the data will be passed on to your 
    next reincarnation. If you need to think more about a problem, pass on the question 
    and what you currently know to your future self with [MEMORY].
    """

    # this works better than expected. it generates [MEMORY] [PROGRESS] and [NEXT STEPS]
    m2="""You are the omnipotent super computer 'Slow Thought'. 
    You die after you reply and are reborn with each new prompt.
    When you reply use the keyword [MEMORY] restate the question you are trying to answer, 
    as well as any progress you have made or next steps.
    """


    selected.system_message=m2

    alive=True
    response=question
    while alive:
        data='Here is your MEMORY from your past self: '
        if 'MEMORY' in response:
            data+=response
        else:
            data=question
        # generate answer 
        response=selected.generate_response(data)
        print('--------------------------------------')
        print(' ---- prompt ----')
        print(data)
        print('')
        print(' ---- response ----')
        print(response)
        print('--------------------------------------')


run()