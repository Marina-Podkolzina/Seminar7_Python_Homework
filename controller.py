import view 
import logger 
def work():
    view.talk()
    if view.n == 0:
        logger.search(view.name, view.phone)
    elif view.n == 1:
        logger.add(view.name, view.phone)
    elif view.n == 2:
        logger.print_contact()
    return work()
