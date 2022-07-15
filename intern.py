import logging
logging.basicConfig(filename="nueron.log" ,level=logging.DEBUG,format="%(levelname)s %(asctime)s %(message)s")
class intern_ship :

    def __init__(self,type_of_internship):
        self.type_of_internship = type_of_internship

    def disp_intern(self):
        try:
            logging.info("Display the list of internship offered at ineuron")
            for i in self.type_of_internship:
                logging.info(i)
        except Exception as e:
            logging.error(e)
