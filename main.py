from sqlalchemy import orm
from typing import TYPE_CHECKING, List
import fastapi
import schemas
import services

if TYPE_CHECKING:
    from sqlalchemy.orm import Session

app = fastapi.FastAPI()

@app.post("/api/contacts", response_model=schemas.Contact)
async def create_contact(
    contact: schemas.CreateContact, 
    db: orm.Session = fastapi.Depends(services.get_db)
):
    return await services.create_contact(contact=contact, db=db)

@app.get("/api/contacts", response_model=List[schemas.Contact])
async def get_contacts(
        db: orm.Session = fastapi.Depends(services.get_db)
):
    return await services.get_all_contacts(db=db)

@app.get("/api/contacts/{contact_id}/", response_model = schemas.Contact)
async def get_contact(
        contact_id: int,
        db: orm.Session = fastapi.Depends(services.get_db)
):
    return await services.get_contact(contact_id = contact_id, db=db)

@app.delete("/api/contacts/{contact_id}/")
async def delete_contact(
        contact_id: int,
        db: orm.Session = fastapi.Depends(services.get_db)
):
    contact = await services.get_contact(db=db, contact_id=contact_id)
    if contact is None:
        raise fastapi.HTTPException(
            status_code = 404,
            detail = f"Contact {contact_id} does not exist."
        )
    await services.delete_contact(contact, db=db)

    return "Successfully deleted user."

@app.put("/api/contacts/{contact_id}/", response_model = schemas.Contact)
async def update_contact(
        contact_id: int,
        contact_data: schemas.CreateContact,
        db: orm.Session = fastapi.Depends(services.get_db)
):  
    contact = await services.get_contact(db=db, contact_id=contact_id)
    if contact is None:
        raise fastapi.HTTPException(
            status_code = 404,
            detail = f"Contact {contact_id} does not exist."
        )
    return await services.update_contact(contact_data=contact_data, contact=contact, db=db)

