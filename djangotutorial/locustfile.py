from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("http://localhost:8000/Klients/")
        self.client.get("http://localhost:8000/Klients/")