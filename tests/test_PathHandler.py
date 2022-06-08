import pytest
import os.path

from ..src.path_handler.PathHandler import PathHandler

class TestPathHandler:

    @pytest.fixture
    def input_path(self) -> str:
        return './example_data/example.fasta'

    @pytest.fixture
    def queried_output(self) -> str:
        return 'phy'

    @pytest.fixture
    def output_path(self) -> str:
        return './example_data/example.phy'

    def test_instance_without_output_path_to_return_output_path_same_directory_as_input_path(self, input_path, queried_output):
        path_handler = PathHandler(input_path, queried_output)
        assert os.path.dirname(path_handler.output_path) == os.path.dirname(path_handler.input_path)

    def test_create_instace_with_output_path_to_return_defined_output_path(self):
        ...

    def test_set_input_path_after_instance_creation(self):
        ...

    def test_set_queried_output_after_instance_creation(self):
        ...
    
    def test_set_output_path_after_instance_creation(self):
        ...