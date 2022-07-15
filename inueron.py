import logging
logging.basicConfig(filename="nueron.log" ,level=logging.DEBUG,format="%(levelname)s %(asctime)s %(message)s")
import students
import course
import jobs
from Internship.intern import intern_ship

logging.info('creating student class object')
stu_obj =students.student("Anil" ,"Kumar" ,30 ,1991,101)
logging.info(stu_obj.get_student_data())

logging.info("creating object for course class")
course_obj = course.courses()
logging.info(course_obj.fee_structure("FSDS"))
logging.info(course_obj.fee_structure("Big Data"))

logging.info('creating object for jobs class')
job_obj = jobs.job({'Data Scientist' : 1200000 ,'SQL Developer':100000 ,'Data Engineer' : 130000 ,'Data Analyst' :900000})
logging.info(job_obj.job_info())

logging.info("creating object for internship class")
int_obj = intern_ship(['Machine Learning Project','Python project','Deep Learning Project' ,'NLP Project','Time Series Project','Data Analytics Project'])
logging.info(int_obj.disp_intern())



