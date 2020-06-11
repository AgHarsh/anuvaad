#!/bin/python
import logging
import os

from flask import Flask, jsonify, request
import datetime as dt
from logging.config import dictConfig
from service.wfmservice import WFMService

wfmapp = Flask(__name__)
context_path = os.environ.get('ANU_ETL_WFM_CONTEXT_PATH', '/anuvaad-etl/wf-manager')


# REST endpoint to initiate the workflow.
@wfmapp.route(context_path + '/v1/workflow/initiate', methods=["POST"])
def initiate_workflow():
    service = WFMService()
    data = request.get_json()
    response = service.register_job(data)
    return response


# REST endpoint to fetch workflow jobs.
@wfmapp.route(context_path + '/v1/workflow/jobs/search/<job_id>', methods=["GET"])
def searchjobs(job_id):
    service = WFMService()
    response = service.get_job_details(job_id)
    return jsonify(response)


# Health endpoint
@wfmapp.route('/health', methods=["GET"])
def health():
    response = {"code": "200", "status": "ACTIVE"}
    return jsonify(response)