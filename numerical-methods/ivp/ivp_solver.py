from ivp.ivp_strategy import IVPStrategy


class IVPSolver:
    def __init__(self, strategy:IVPStrategy):
        self._strategy = strategy
