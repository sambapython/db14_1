#!/bin/bash
gunicorn --bind 0.0.0.0:8002 warehouse.wsgi