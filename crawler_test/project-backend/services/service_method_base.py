# -*- coding: utf-8 -*-
#
# Copyright (c) 2021-2021 Jaehoon Lee (dioscuroi@kaist.ac.kr)

import sys
import json
import traceback

class ServiceMethodBase:
    def __init__(self):
        pass

    @classmethod
    def run(cls, event, _):
        try:
            results = cls().process(event)

            return cls.api_response(200, results)

        except Exception as e:
            print(event)
            print(sys.exc_info())
            traceback.print_exc()

            return cls.api_response(500, e)

    def process(self, event):
        raise NotImplementedError()

    # decorator
    @classmethod
    def api_response(cls, status_code, results):
        if results is None:
            body = ''
        elif isinstance(results, (list, dict)):
            body = json.dumps(results, default=str)
        else:
            body = json.dumps({
                'message': str(results)
            })

        return {
            'statusCode': status_code,
            'body': body,
            'headers': {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Credentials": True,
                "Content-Type": "application/json"
            }
        }

