from fastapi import APIRouter, HTTPException, status

import main
from schemas import TestSchema

test_router = APIRouter()


@test_router.post("/test/input")
def test_input(data: TestSchema):
    try:
        main.cursor.execute("""INSERT INTO testtable 
                        (name,email,count) VALUES (%s,%s,%s) """,
                            (data.name, data.email, data.count))
        main.conn.commit()
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
