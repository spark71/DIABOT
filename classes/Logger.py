import logging

class Logger:
    def __init__(self, log_file):
        self.log_file = log_file
        logging.basicConfig(filename=log_file, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def log_user_action(self, user_id, action):
        self.logger.info(f"User {user_id} performed action: {action}")

