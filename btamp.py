#!/usr/bin/env python
import base64

def tamper(payload, **kwargs):
    return base64.b64encode(payload.encode()).decode()


# By nexzy - t.me/cruzes - github.com/nexzydev