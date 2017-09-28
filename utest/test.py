

import sys
sys.path.insert(0,"../..")
print sys.path
import liteLogging


logger = liteLogging.getLogger()
handler = liteLogging.StreamHandler()
formatter = liteLogging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(liteLogging.DEBUG)

logger.debug('often makes a very good meal of %s', 'visiting tourists')