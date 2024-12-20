import time

class Profiler:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        if self.start_time is not None:
            raise RuntimeError("Profiler is already running.")
        self.start_time = time.time()

    def stop(self):
        if self.start_time is None:
            raise RuntimeError("Profiler has not been started.")
        self.end_time = time.time()
        elapsed = self.end_time - self.start_time
        self.start_time = None
        self.end_time = None
        return elapsed

    def profile(self, func, *args, **kwargs):
        self.start()
        result = func(*args, **kwargs)
        elapsed_time = self.stop()
        return result, elapsed_time