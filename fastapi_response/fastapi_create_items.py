import json

from . import router
from tortoise_models.basemodel import User


@router.get("/create")
async def fastapi_create(filters, params) -> dict:
    filters = json.loads(filters)
    params = json.loads(params)
    if await User.filter(**filters).first() is None:
        await User.create(**params)
        return {'success': True, 'data': None}
    else:
        return {'success': False, 'data': None}