import logging, time
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logging.info("booting")
t0 = time.time(); time.sleep(0.01)
logging.info("done in %.3fs", time.time() - t0)