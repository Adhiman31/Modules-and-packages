import logging
logging.basicConfig(filename="nueron.log" ,level=logging.DEBUG,format="%(levelname)s %(asctime)s %(message)s")

class courses :

    def fee_structure(self,course_name):
        logging.info("this function gives the fee description as per chosen course")
        try:
            if course_name == 'FSDS':
                logging.info('the fees for FSDS course is 15000 INR')
            elif course_name == 'Big Data' :
                logging.info('the fees for Big Data course is 10000 INR')
            elif course_name == 'SQL':
                logging.info("the fees for Big Data course is 5000 INR")
            else:
                logging.info("Sorry , currently we do not have the course you are looking for")
        except Exception as e :
            logging.info(e)



