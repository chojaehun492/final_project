import logging
import os

class Logger:
    def __init__(self, log_file="logs/project.log", log_level=logging.INFO):
        os.makedirs(os.path.dirname(log_file), exist_ok=True)

        self.logger = logging.getLogger("ProjectLogger")
        if self.logger.hasHandlers():
            self.logger.handlers.clear()  # 중복 핸들러 제거
        self.logger.setLevel(log_level)

        file_handler = logging.FileHandler(log_file)
        console_handler = logging.StreamHandler()

        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

    def warning(self, message):
        self.logger.warning(message)
