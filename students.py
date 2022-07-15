import logging
logging.basicConfig(filename="nueron.log" ,level=logging.DEBUG,format="%(levelname)s %(asctime)s %(message)s")

class student :

    def __init__(self,name,surname,age,dob,studentid):
        try:
            logging.info("This is a student class constructor")
            self.name = name
            self.surname = surname
            self.age = age
            self.dob = dob
            self.studentid = studentid
        except Exception as e :
            logging.error(e)




    def get_student_data(self):
        try:
            logging.info('this function provides all the details of Student data')
            logging.info('Name is %s '+' %s' ,self.name , self.surname)
            logging.info('age is %s',self.age)
            logging.info('dob is %s',self.dob)
            logging.info('student_id is %s' ,self.studentid)
        except Exception as e:
            logging.error(e)



















