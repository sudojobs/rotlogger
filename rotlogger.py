import glob
import logging
import logging.handlers
import sys

count =0 
LOG_FILENAME = 'app.log'

# Set up a specific logger with our desired output level
sys_logger = logging.getLogger('LOG')
sys_logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(
              LOG_FILENAME, maxBytes=100000, backupCount=5)
#10000000
handler.setFormatter(formatter)

sys_logger.addHandler(handler)

# Log some messages
#for i in range(2000):
#    sys_logger.debug('i = %d' % i)

# See what files are created


while True:
    count = count + 1
    if(count > 33000):
       logfiles = glob.glob('%s*' % LOG_FILENAME)
       for filename in logfiles:
           print(filename)
           sys.exit()
    sys_logger.info('count = %d',count)
