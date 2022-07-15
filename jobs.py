import logging
logging.basicConfig(filename="nueron.log" ,level=logging.DEBUG,format="%(levelname)s %(asctime)s %(message)s")

class job :

    def __init__(self,job_dict):
        self.job_dict = job_dict


    def job_info(self):
        try:
            logging.info('this function provides job role and annual salary expectations ')
            for k,v in self.job_dict.items():
                logging.info("The Job Role is %s and Salary is %s",k ,v)
        except Exception as e:
            logging.error(e)





