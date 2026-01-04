from datetime import date
from app.errors import NotVaccinatedError
from app.errors import OutdatedVacineError
from app.errors import NotWearingMaskError


class Cafe:
    def __init__(self,
                 name: str) -> None:
        self.name = name

    def visit_cafe(self,
                   visitor: dict) -> str:

        if "vaccine" not in visitor:
            raise NotVaccinatedError

        vaccine = visitor["vaccine"]
        if "expiration_date" not in vaccine:
            raise OutdatedVacineError

        vaccine_expiration_date = vaccine["expiration_date"]
        today = date.today()

        if today > vaccine_expiration_date:
            raise OutdatedVacineError

        if "wearing_a_mask" not in visitor:
            raise NotWearingMaskError

        if visitor["wearing_a_mask"] is False:
            raise NotWearingMaskError

        return f"Welcome to {self.name}"
