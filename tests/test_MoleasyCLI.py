import pytest

from src.moleasy_cli.MoleasyCLI import MoleasyCLI


class TestMoleasyCLI:

    @pytest.fixture
    def sys_args_convert_with_more_than_five_args(self):
        pass

    @pytest.fixture
    def sys_args_with_invalid_method(self):
        pass

    @pytest.fixture
    def sys_args_with_less_than_four_args(self):
        pass

    def test_MoleasyCLI_TooMuchArgsError(self):
        pass

    def test_MoleasyCLI_InvalidMethodError(self):
        pass

    def test_MoleasyCLI_MissingArgsError(self):
        pass