from fastapi import HTTPException


def handler_exception(exception: Exception, status_code: int):
    e = HTTPException(status_code=status_code, detail=str(exception))

    raise e
