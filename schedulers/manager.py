# -*- coding:utf8 -*-
from apscheduler.schedulers.background import BackgroundScheduler

# from apps.szgbidding.jobs.szzfcg import Szzfcg
# from szgbidding.jobs.szzfcg import Szzfcg
from apps.szgbidding.jobs.szzfcg import Szzfcg


def start_schedulers():
    sched = BackgroundScheduler()
    # TODO : add your job here
    sched.add_job(Szzfcg.run, trigger='cron', second='*/5', max_instances=5)
    # sched.add_job(Szzfcg.run, trigger='cron', minute='*/5', max_instances=5)
    # sched.add_job(Szzfcg.run, trigger='cron', second='*/5', max_instances=5)


    sched.start()
