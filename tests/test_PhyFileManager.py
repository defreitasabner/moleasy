import pytest

from ..src.file_manager.phy.PhyFileManager import PhyFileManager


class TestPhyFileManager:

    @pytest.fixture
    def example_phy_path(self):
        path = 'tests/example_data/example.phy'
        return path

    @pytest.fixture
    def correct_output_to_example_phy(self):
        correct_output = [{'taxon': 'H_sapiens', 'sequence': 'ACCGGTTGGCCGTTCAGGGTACAGGTTGGCCGTTCAGGGTAA'}, {'taxon': 'Chimp', 'sequence': 'AAACCCTTGCCGTTACGCTTAAACCGAGGCCGGGACACTCAT'}, {'taxon': 'Gorilla', 'sequence': 'AAACCCTTGCCGGTACGCTTAAACCATTGCCGGTACGCTTAA'}]
        return correct_output

    def test_read_file_method_with_correct_input(self, example_phy_path, correct_output_to_example_phy):
        output_data = PhyFileManager.read_file(example_phy_path)
        assert output_data == correct_output_to_example_phy