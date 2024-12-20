import json
import os

class FileManager:
    """
    파일 관리 유틸리티 클래스
    """
    @staticmethod
    def _check_file_exists(file_path):
        """
        파일 존재 여부 확인
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

    @staticmethod
    def load_json(file_path):
        """
        JSON 파일 로드
        """
        FileManager._check_file_exists(file_path)
        with open(file_path, 'r') as file:
            return json.load(file)

    @staticmethod
    def save_json(file_path, data):
        """
        JSON 파일 저장
        """
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"JSON saved at {file_path}")

    @staticmethod
    def load_text(file_path):
        """
        텍스트 파일 로드
        """
        FileManager._check_file_exists(file_path)
        with open(file_path, 'r') as file:
            return file.read()

    @staticmethod
    def save_text(file_path, content):
        """
        텍스트 파일 저장
        """
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"Text saved at {file_path}")
