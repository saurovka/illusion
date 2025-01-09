print('illusion.py: ', __name__)

''' this function is used to create an illusion of a list of numbers '''
def create_illusion():
    print('Illusion created')
    return [1, 2, 3, 4, 5]


''' this function is used to destroy the illusion of a list of numbers '''
def destroy_illusion():
    print('Illusion destroyed') 
    return None 

create_illusion()
destroy_illusion()

