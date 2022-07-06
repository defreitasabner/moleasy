import pytest

from ..src.moleasy_cli.MoleasyCLI import MoleasyCLI
from ..src.exceptions.TooMuchArgsError import TooMuchArgsError
from ..src.exceptions.InvalidMethodError import InvalidMethodError
from ..src.exceptions.MissingArgsError import MissingArgsError


class TestMoleasyCLI:

    @pytest.fixture
    def sys_args_convert_with_more_than_five_args(self):
        pass

    @pytest.fixture
    def sys_args_with_invalid_method(self):
        pass

    @pytest.fixture
    def sys_args_with_less_than_four_args(self):
        sys_args = [
            'path_to_script',
            'convert',
            './tests/example_data/example.phy'
        ]
        return sys_args

    def test_MoleasyCLI_TooMuchArgsError(self):
        pass

    def test_MoleasyCLI_InvalidMethodError(self):
        pass

    def test_MoleasyCLI_MissingArgsError(self, sys_args_with_less_than_four_args):
        with pytest.raises(MissingArgsError):
            moleasy = MoleasyCLI(sys_args_with_less_than_four_args)
            moleasy.start()