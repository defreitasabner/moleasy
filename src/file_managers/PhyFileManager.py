from typing import List, Dict

from .FileManager import FileManager


class PhyFileManager(FileManager):

    @staticmethod
    def read_file(input_path: str) -> List[Dict[str, str]]:
        taxa: List[str] = []
        sequences: List[str] = []
        with open(input_path, mode='r', encoding='utf-8') as phy_file:
            for line in phy_file:
                taxon_sequence = line.strip()
                taxon, sequence = taxon_sequence.split()
                taxa.append(taxon)
                sequences.append(sequence)
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
    def write_file(output_path: str, output_data: List[Dict[str, str]]) -> None:
        with open(output_path, mode='w', encoding='utf-8') as phy_file:
            taxa_quantity = len(output_data)
            sequence_length = len(output_data[0]['sequence'])
            output_header = f'{taxa_quantity} {sequence_length}\n'
            phy_file.write(output_header)
            for data in output_data:
                taxon, sequence = data
                output_line = f'{data[taxon]} {data[sequence]}\n'
                phy_file.write(output_line)
