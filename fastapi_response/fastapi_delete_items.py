import json

from . import router
from tortoise_models.basemodel import User


@router.get("/delete")
async def fastapi_delete(filters) -> dict:
    filters = json.loads(filters)
    if await User.filter(**filters).first() is not None:
        await User.filter(**filters).delete()
        return {'success': True, 'data': None}
    else:
        return {'success': False, 'data': None}