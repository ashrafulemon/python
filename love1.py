from apscheduler.schedulers.blocking import BlockingScheduler
from love import send_love

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(send_love, 'interval', seconds=100)

sched.start()