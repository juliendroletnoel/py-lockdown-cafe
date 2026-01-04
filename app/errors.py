class VaccineError(Exception):
    pass


class NotVaccinatedError(VaccineError):
    pass


class OutdatedVacineError(VaccineError):
    pass


class NotWearingMaskError(Exception):
    pass
