#!/bin/bash
python download_tests.py
python init_tests.py
python run_tests.py
python collate_data.py