from app.cafe import Cafe
from app.errors import VaccineError, NotWearingMaskError


def go_to_cafe(friends: list[dict],
               cafe: Cafe) -> str:

    needed_masks = 0
    friends_are_vaccinated = True
    for friend in friends:

        try:
            cafe.visit_cafe(visitor=friend)
        except VaccineError:
            friends_are_vaccinated = False
        except NotWearingMaskError:
            needed_masks += 1

    if friends_are_vaccinated is False:
        return "All friends should be vaccinated"

    if needed_masks:
        return f"Friends should buy {needed_masks} masks"

    return f"Friends can go to {cafe.name}"
