from typing import List, Dict

from .FileManager import FileManager


class PhyFileManager(FileManager):

    @staticmethod
    def read_file(input_path: str):
        taxa: List[str] = []
        sequences: List[str] = []
        with open(input_path, mode='r', encoding='utf-8') as phy_file:
            for line in phy_file:
                taxon_sequence = line.strip()
                taxon, sequence = taxon_sequence.split()
                taxon_treated = taxon.strip()
                sequence_treated = sequence.strip()
                taxa.append(taxon_treated)
                sequences.append(sequence_treated)
            if len(taxa) == len(sequences):
                dataset = []
                for i in range(len(taxa)):
                    data = {'taxon': taxa[i], 'sequence': sequences[i]}
                    dataset.append(data)
                dataset.pop(0)
                return dataset
            else:
                Exception('The number of taxa is different of the number of sequences')

    @staticmethod
    def write_file(output_path: str, output_data: List[Dict[str, str]]):
        ...
