
from locust import HttpUser, TaskSet, task, between

class APIUser(HttpUser):
    wait_time = between(1, 3)
    host = "http://127.0.0.1:8000"

    @task
    class UserTasks(TaskSet):
        @task
        def get_status(self):
            self.client.get("/status/") 

        @task
        def do_compute(self):
            self.client.get("/compute?n=100") 
