
from fastapi import APIRouter
from .service import get_depression
from .schema import DepressionRequest

router = APIRouter()

@router.post('/depression', tags=['Depression'])
def assess_depression(data: DepressionRequest):
    return get_depression()

@router.get('/info', tags=['Depression'])
def get_depression_info():
    return {"status": "Depression assessment endpoint", "version": "1.0"}

@router.delete('/depression', tags=['Depression'])
def delete_depression_assessment(record_id: int):
    return {"status": "delete", "record_id": record_id}

@router.put('/depression', tags=['Depression'])
def update_depression_assessment(record_id: int, data: DepressionRequest):
    return {"status": "update", "record_id": record_id, "data": data}

@router.patch('/depression', tags=['Depression'])
def partial_update_depression_assessment(record_id: int, data: DepressionRequest):
    return {"status": "partially update", "record_id": record_id, "data": data}