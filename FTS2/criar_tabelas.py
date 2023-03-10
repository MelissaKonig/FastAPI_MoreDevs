from core.configs import settings
from core.database import engine


print('execuntando documento criar_tabelas')
async def create_tables() -> None:
    print("entrando na funcao")

    import models.all_models

    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print('Tabela Criada Com Sucesso')

if __name__ == '__main__':
    import asyncio
    asyncio.run(create_tables())