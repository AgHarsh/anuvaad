#!/bin/python
import logging

from anuvaad_auditor.errorhandler import post_error

log = logging.getLogger('file')
from utilities.wfmutils import WFMUtils
from configs.wfmconfig import is_sync_flow_enabled
from configs.wfmconfig import is_async_flow_enabled
from configs.wfmconfig import tool_translator

wfmutils = WFMUtils()


class TranslatorValidator:
    def __init__(self):
        pass

    # Validator that validates the input request for initiating translation through wf
    def validate_wf(self, data):
        if 'jobID' not in data.keys():
            return post_error("JOBID_NOT_FOUND", "jobID is mandatory", None)
        else:
            error = self.validate_input_files(data)
            if error is not None:
                return error

    # Validator that validates the input request for translation
    def validate_input_files(self, data):
        if 'files' not in data.keys():
            return post_error("FILES_NOT_FOUND", "files are mandatory", None)
        else:
            if len(data["files"]) == 0:
                return post_error("FILES_NOT_FOUND", "Input files are mandatory", None)
            else:
                for file in data["files"]:
                    if 'path' not in file.keys():
                        return post_error("FILES_PATH_NOT_FOUND", "Path is mandatory for all files in the input", None)
                    if 'type' not in file.keys():
                        return post_error("FILES_TYPE_NOT_FOUND", "Type is mandatory for all files in the input", None)
                    if 'locale' not in file.keys():
                        return post_error("FILES_LOCALE_NOT_FOUND", "Locale is mandatory for all files in the input", None)
                    if 'model' not in file.keys():
                        return post_error("MODEL_NOT_FOUND", "Model details are mandatory for this wf.", None)
                    else:
                        model = file["model"]
                        if 'model_id' not in model.keys():
                            return post_error("MODEL_ID_NOT_FOUND", "Model Id is mandatory.", None)
                        if 'url_end_point' not in model.keys():
                            return post_error("MODEL_URLENDPOINT_NOT_FOUND", "Model url end point is mandatory.", None)
        if 'metadata' not in data.keys():
            return post_error("METADATA_NOT_FOUND", "Metadata is mandatory", None)
        else:
            metadata = data["metadata"]
            if 'bearer' not in metadata.keys():
                return post_error("BEARER_TOKEN_NOT_FOUND", "Bearer token is mandatory", None)