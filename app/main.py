from app.cafe import Cafe
from app.errors import NotVaccinatedError
from app.errors import OutdatedVaccineError
from app.errors import NotWearingMaskError


def go_to_cafe(friends: list[dict],
               cafe: Cafe) -> str:

    needed_masks = 0
    friends_are_vaccinated = True
    for friend in friends:

        try:
            cafe.visit_cafe(visitor=friend)
        except NotVaccinatedError:
            friends_are_vaccinated = False
        except OutdatedVaccineError:
            friends_are_vaccinated = False
        except NotWearingMaskError:
            needed_masks += 1

    if friends_are_vaccinated is False:
        return "All friends should be vaccinated"

    if needed_masks != 0:
        return f"Friends should buy {needed_masks} masks"

    return f"Friends can go to {cafe.name}"
