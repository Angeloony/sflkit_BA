import enum

from sflkit.runners.run import Runner, VoidRunner, PytestRunner, UnittestRunner


class RunnerType(enum.Enum):
    def __init__(self, runner: Runner):
        self.runner = runner

    VOID_RUNNER = VoidRunner
    PYTEST_RUNNER = PytestRunner
    UNITTEST_RUNNER = UnittestRunner
