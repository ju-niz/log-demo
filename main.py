from flask import Flask
import logging

app = Flask(__name__)
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 콘솔 핸들러
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
app.logger.addHandler(console_handler)
logger.setLevel(logging.DEBUG)
