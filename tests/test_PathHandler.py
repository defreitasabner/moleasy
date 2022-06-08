import pytest
import os.path

from ..src.path_handler.PathHandler import PathHandler

class TestPathHandler:

    @pytest.fixture
    def input_path(self) -> str:
        return './example_data/example.fasta'

    @pytest.fixture
    def required_output(self) -> str:
        return 'phy'

    @pytest.fixture
    def output_path(self) -> str:
        return './example_data/example.phy'

    def test_instance_without_output_path_to_return_output_path_same_directory_as_input_path(self, input_path, required_output):
        path_handler = PathHandler(input_path, required_output)
        assert os.path.dirname(path_handler.output_path) == os.path.dirname(path_handler.input_path)

    def test_instace_with_output_path_to_return_the_defined_output_path(self, input_path, required_output, output_path):
        expected_output_path = output_path
        path_handler = PathHandler(input_path, required_output, output_path)
        assert path_handler.output_path == expected_output_path

    def test_set_input_path_after_instance_creation(self, input_path, required_output):
        new_input_path = './example_data/example.nex'
        path_handler = PathHandler(input_path, required_output)
        path_handler.input_path = new_input_path
        assert path_handler.input_path == new_input_path

    def test_set_required_output_after_instance_creation(self, input_path, required_output):
        new_required_output = 'fasta'
        path_handler = PathHandler(input_path, required_output)
        path_handler.required_output = new_required_output
        assert path_handler.required_output == new_required_output
    
    def test_set_a_valid_output_path_after_instance_creation(self, input_path, required_output, output_path):
        new_output_path = './example_data/example.nex'
        path_handler = PathHandler(input_path, required_output, output_path)
        path_handler.output_path = new_output_path
        assert path_handler.output_path == new_output_path

    def test_set_empty_output_path_after_instance_creation_return_output_path_directory_equal_input_directory(self, input_path, required_output, output_path):
        new_output_path = ''
        path_handler = PathHandler(input_path, required_output, output_path)
        path_handler.output_path = new_output_path
        assert os.path.dirname(path_handler.output_path) == os.path.dirname(path_handler.input_path)