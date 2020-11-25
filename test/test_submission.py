import unittest
import scheduler
import surfex
import os
import json
from datetime import datetime


class TestSubmit(unittest.TestCase):

    @staticmethod
    def _create_exp(wd):
        os.makedirs(wd, exist_ok=True)
        argv = [
            "setup",
            "--wd", wd,
            "-rev", wd,
            "-conf", os.getcwd(),
            "-host", "unittest",
            "--domain_file", "test/settings/conf_proj_test.json"
        ]
        kwargs = scheduler.parse_surfex_script(argv)
        scheduler.surfex_script(**kwargs)

    def test_submission(self):

        exp = "test_submission"
        hm_wd = "/tmp/host0/hm_wd/" + exp
        self._create_exp(hm_wd)

        # Set progress
        dtg = datetime(2020, 6, 9, 9)
        progress = {"DTG": dtg.strftime("%Y%m%d%H")}
        progress_pp = {"DTGPP": dtg.strftime("%Y%m%d%H")}
        progress = scheduler.Progress(progress, progress_pp)

        sfx_exp = scheduler.ExpFromFiles(exp, hm_wd, progress=progress)

        ecf_name = "/" + exp + "/Forecasting/Forecast"
        ecf_tryno = 1
        ecf_pass = "dummy_password"

        task = scheduler.EcflowTask(ecf_name, ecf_tryno, ecf_pass, ecf_rid=int(os.getpid()),
                                    submission_id=None)
        os.makedirs("/tmp/host1/job/" + exp + "/Forecasting/", exist_ok=True)
        fh = open("/tmp/host1/job/" + exp + "/Forecasting/Forecast.job1", "w")
        fh.write("My job generated by ecflow")
        fh.close()

        exceptions = {
            "complete": {
                "task": {
                    "Forecast": "is_coldstart"
                },
                "family": {
                    "Forecasting": "is_coldstart"
                }
            }
        }

        env_file = "/tmp/host1/job/" + exp + "/Forecasting/Env"
        fh = open(env_file, "w")
        fh.write("print(\"Oh my environment\n\")")
        fh.close()

        hosts = sfx_exp.system.hosts
        joboutdir = {}
        for host in range(0, len(hosts)):
            joboutdir.update({str(host): sfx_exp.system.get_var("JOBOUTDIR", str(host))})
        submit = scheduler.EcflowSubmitTask(task, sfx_exp.env_submit, sfx_exp.server, joboutdir,
                                            submit_exceptions=exceptions, env_file=env_file)
        submit.write_job()

    def test_slurm(self):

        exp = "test_slurm"

        ecf_name = "/" + exp + "/Forecasting/Forecast"
        ecf_tryno = 1
        ecf_pass = "dummy_password"

        task = scheduler.EcflowTask(ecf_name, ecf_tryno, ecf_pass, ecf_rid=int(os.getpid()),
                                    submission_id=None)
        os.makedirs("/tmp/host1/job/" + exp + "/Forecasting/", exist_ok=True)
        fh = open("/tmp/host1/job/" + exp + "/Forecasting/Forecast.job1", "w")
        fh.write("My job generated by ecflow")
        fh.close()

        joboutdirs = {
            "0": "/tmp/host0/job/",
            "1": "/tmp/host1/job/"
        }

        env_submit = {
            "submit_types": ["background", "scalar"],
            "default_submit_type": "scalar",
            "background": {
                "HOST": "0",
                "OMP_NUM_THREADS": "import os\nos.environ.update({\"OMP_NUM_THREADS\": \"1\"})",
                "tasks": [
                    "InitRun",
                    "LogProgress",
                    "LogProgressPP"
                ]
            },
            "scalar": {
                "HOST": "1",
                "SUBMIT_TYPE": "slurm",
                "SSH": "ssh " + os.environ["USER"] + "@localhost",
                "INTERPRETER": "#!/usr/bin/env python3",
                "WRAPPER": "wrapper",
                "Not_existing_task": {
                    "DR_HOOK": "print(\"hei\")"
                }
            }
        }

        task_settings = scheduler.TaskSettings(task, env_submit, joboutdirs)
        sub = scheduler.SlurmSubmission(task, task_settings, sub=os.getcwd() + "/test/bin/sbatch")
        sub.set_submit_cmd()
        sub.submit_job()
        sub.set_jobid()
        self.assertEqual(sub.job_id, "slurm.12345")
        if not os.path.exists("/tmp/host1/job/" + exp + "/Forecasting/Forecast.job1.sub"):
            raise Exception("Expected sub file mot found")

        task = scheduler.EcflowTask(ecf_name, ecf_tryno, ecf_pass, ecf_rid=int(os.getpid()),
                                    submission_id=sub.job_id)
        sub = scheduler.get_submission_object(task, task_settings)
        sub.status()
        if not os.path.exists("/tmp/host1/job/" + exp + "/Forecasting/Forecast.job1.stat"):
            raise Exception("Expected status file mot found")
        sub.kill()
        if not os.path.exists("/tmp/host1/job/" + exp + "/Forecasting/Forecast.job1.kill"):
            raise Exception("Expected kill file mot found")

    def test_pbs(self):
        exp = "test_pbs"

        ecf_name = "/" + exp + "/Forecasting/Forecast"
        ecf_tryno = 1
        ecf_pass = "dummy_password"

        task = scheduler.EcflowTask(ecf_name, ecf_tryno, ecf_pass, ecf_rid=int(os.getpid()),
                                    submission_id=None)
        os.makedirs("/tmp/host1/job/" + exp + "/Forecasting/", exist_ok=True)
        fh = open("/tmp/host1/job/" + exp + "/Forecasting/Forecast.job1", "w")
        fh.write("My job generated by ecflow")
        fh.close()

        joboutdirs = {
            "0": "/tmp/host0/job/",
            "1": "/tmp/host1/job/"
        }

        env_submit = {
            "submit_types": ["background", "scalar"],
            "default_submit_type": "scalar",
            "background": {
                "HOST": "0",
                "OMP_NUM_THREADS": "import os\nos.environ.update({\"OMP_NUM_THREADS\": \"1\"})",
                "tasks": [
                    "InitRun",
                    "LogProgress",
                    "LogProgressPP"
                ]
            },
            "scalar": {
                "HOST": "1",
                "SUBMIT_TYPE": "pbs",
                "Not_existing_task": {
                    "DR_HOOK": "print(\"hei\")"
                }
            }
        }

        task_settings = scheduler.TaskSettings(task, env_submit, joboutdirs)
        sub = scheduler.get_submission_object(task, task_settings)
        sub.set_submit_cmd()
        sub.submit_job()
        sub.set_jobid()
        self.assertEqual(sub.job_id, "pbs.12345")
        if not os.path.exists("/tmp/host1/job/" + exp + "/Forecasting/Forecast.job1.sub"):
            raise Exception("Expected sub file mot found")

        task = scheduler.EcflowTask(ecf_name, ecf_tryno, ecf_pass, ecf_rid=int(os.getpid()),
                                    submission_id=sub.job_id)
        sub = scheduler.PBSSubmission(task, task_settings)
        sub.status()
        if not os.path.exists("/tmp/host1/job/" + exp + "/Forecasting/Forecast.job1.stat"):
            raise Exception("Expected status file mot found")
        sub.kill()
        if not os.path.exists("/tmp/host1/job/" + exp + "/Forecasting/Forecast.job1.kill"):
            raise Exception("Expected kill file mot found")

    def test_grid_engine(self):
        exp = "test_grid_engine"

        ecf_name = "/" + exp + "/Forecasting/Forecast"
        ecf_tryno = 1
        ecf_pass = "dummy_password"

        task = scheduler.EcflowTask(ecf_name, ecf_tryno, ecf_pass, ecf_rid=int(os.getpid()),
                                    submission_id=None)
        os.makedirs("/tmp/host1/job/" + exp + "/Forecasting/", exist_ok=True)
        fh = open("/tmp/host1/job/" + exp + "/Forecasting/Forecast.job1", "w")
        fh.write("My job generated by ecflow")
        fh.close()

        joboutdirs = {
            "0": "/tmp/host0/job/",
            "1": "/tmp/host1/job/"
        }

        env_submit = {
            "submit_types": ["background", "scalar"],
            "default_submit_type": "scalar",
            "background": {
                "HOST": "0",
                "OMP_NUM_THREADS": "import os\nos.environ.update({\"OMP_NUM_THREADS\": \"1\"})",
                "tasks": [
                    "InitRun",
                    "LogProgress",
                    "LogProgressPP"
                ]
            },
            "scalar": {
                "HOST": "1",
                "SUBMIT_TYPE": "grid_engine",
                "SUBMIT": "qsub_sge",
                "Not_existing_task": {
                    "DR_HOOK": "print(\"hei\")"
                }
            }
        }

        task_settings = scheduler.TaskSettings(task, env_submit, joboutdirs)
        # Test default
        scheduler.get_submission_object(task, task_settings)
        # Make my own test SGE
        sub = scheduler.GridEngineSubmission(task, task_settings, sub="qsub_sge", stat="qacct_sge -j", kill="qdel_sge")
        sub.set_submit_cmd()
        sub.submit_job()
        sub.set_jobid()
        self.assertEqual(sub.job_id, "sge.12345")
        if not os.path.exists("/tmp/host1/job/" + exp + "/Forecasting/Forecast.job1.sub"):
            raise Exception("Expected sub file mot found")

        task = scheduler.EcflowTask(ecf_name, ecf_tryno, ecf_pass, ecf_rid=int(os.getpid()),
                                    submission_id=sub.job_id)
        sub = scheduler.GridEngineSubmission(task, task_settings, sub="qsub_sge", stat="qacct_sge -j", kill="qdel_sge")
        sub.status()
        if not os.path.exists("/tmp/host1/job/" + exp + "/Forecasting/Forecast.job1.stat"):
            raise Exception("Expected status file mot found")
        sub.kill()
        if not os.path.exists("/tmp/host1/job/" + exp + "/Forecasting/Forecast.job1.kill"):
            raise Exception("Expected kill file mot found")
