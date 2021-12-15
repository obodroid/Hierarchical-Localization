import logging
import sys

logging.basicConfig(stream=sys.stdout,
                    format='[%(asctime)s.%(msecs)03dZ] %(levelname)s] %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S',
                    level=logging.INFO)
