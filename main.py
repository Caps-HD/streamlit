import logging
import os

if __name__ == '__main__':
    logging.info("============================开始============================")
    py_file = 'streamlit run %s/streamlit_app.py' % os.path.dirname(__file__)
    p = os.system(py_file)
