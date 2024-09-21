import json

from . import router
from tortoise_models.basemodel import User


@router.get("/update")
async def fastapi_update(filters, params) -> dict:
    filters = json.loads(filters)
    params = json.loads(params)
    if await User.filter(**filters).first() is not None:
        await User.filter(**filters).update(**params)
        return {'success': True, 'data': None}
    else:
        return {'success': False, 'data': None}