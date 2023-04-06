from flask import Flask,request
import schedule
import datetime
import time
import requests


app = Flask(__name__)

@app.route("/")
@app.route('/index')
def hello_world():
    requests.get("https://www.google.com/")
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))
    return "Hello world!"


@app.route('/start')
def teststart():
    # run_schedule()
    # requests.get("https://www.google.com/")
    print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))
    return 'Schedule is running'
# 
# app.run('127.0.0.1', port=5500)

nowtime = str(datetime.datetime.now())

def job(t):
    print("I'm working...", str(datetime.datetime.now()), t)

for i in ["15:00", "09:00", "12:00", "15:00", "18:00"]:
    schedule.every().monday.at(i).do(job, i)
    schedule.every().tuesday.at(i).do(job, i)
    schedule.every().wednesday.at(i).do(job, i)
    schedule.every().thursday.at(i).do(job, i)
    schedule.every().friday.at(i).do(job, i)

def run_schedule():
    while True:
        schedule.run_pending()
        #time.sleep(30)

# @app.route('/start', methods =["GET", "POST"])
# def teststart():
#     # run_schedule()
#     # requests.get("https://www.google.com/")
#     print(time.strftime("%A, %d. %B %Y %I:%M:%S %p"))
#     return 'Schedule is running'

if __name__ == '__main__':
    app.run()
































# from apscheduler.schedulers.blocking import BlockingScheduler

# def job_function():
#     print("Hello World")

# sched = BlockingScheduler()

# # Runs from Monday to Friday at 5:30 (am) until
# # sched.add_job(job_function, 'cron', day_of_week='mon-fri', hour=5, minute=30)
# sched.add_job(job_function, 'cron', minute=1)
# sched.start()

# import schedule
# import datetime
# import time

# nowtime = str(datetime.datetime.now())

# def job(t):
#     print("I'm working...", str(datetime.datetime.now()), t)

# for i in ["15:00", "09:00", "12:00", "15:00", "18:00"]:
#     schedule.every().monday.at(i).do(job, i)
#     schedule.every().tuesday.at(i).do(job, i)
#     schedule.every().wednesday.at(i).do(job, i)
#     schedule.every().thursday.at(i).do(job, i)
#     schedule.every().friday.at(i).do(job, i)

# while True:
#     schedule.run_pending()
#     time.sleep(30)