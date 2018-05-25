# -*- coding: utf-8 -*-
"""Extensions module. Each extension is initialized in the app factory located in app.py."""
from flask_jsonrpc import JSONRPC

jsonrpc = JSONRPC(service_url="/api", enable_web_browsable_api=True)