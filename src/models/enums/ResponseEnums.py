from enum import Enum

class ResponseSignal(Enum):

    FILE_TYPE_NOT_SUPPORTED = "File type not supported"
    FILE_SIZE_EXCEEDED = "file size exceeded"
    FILE_UPLOAD_SUCCESS = "file upload success"
    FILE_UPLOAD_FAILED = "file upload failed"
    FILE_VALIDATED_SUCCESS = "file validated success"
    FILE_VALIDATED_FAILED = "file validated failed"
    PROCESSING_SUCCESS = "processing success"
    PROCESSING_FAILED = "processing failed"
    NO_FILES_ERROR = "no files found"
    FILE_ID_ERROR = "no file found with this id"

    
