from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from producer import Dem
import json
from app.utils.file import write_file

router = APIRouter()


@router.post('/')
def demotivator(top_text: str, bottom_text: str, pic: UploadFile = File()):
    if pic.content_type != 'image/jpeg':
        raise HTTPException(400, detail="File is not an image")
    dem = Dem()
    pic = (pic.file.read()).decode('ISO-8859-1')
    body = json.dumps({'top_text': top_text, 'bottom_text': bottom_text, 'pic': pic})
    res = dem.call(body)
    write_file(res)
    return FileResponse('dem.png')
