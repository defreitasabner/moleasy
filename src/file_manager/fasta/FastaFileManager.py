from typing import List, Dict

from ..FileManager import FileManager


class FastaFileManager(FileManager):
    """
    FastaFileManager
    ---
    Module responsable to read and write `Fasta` files. The accepted files extensions are: `.fasta` and `.fas`.
    """

    @staticmethod
    def read_file(input_path: str) -> List[Dict[str, str]]:
        taxa: List[str] = []
        sequences: List[str] = []
        with open(input_path, mode='r', encoding='utf-8') as fasta_file:
            for line in fasta_file:
                if '>' in line:
                    taxon: str = line
                    taxon_treated: str = taxon.replace('>', '').strip()
                    taxa.append(taxon_treated)
                else:
                    sequence: str = line.strip()
                    sequences.append(sequence)
        if len(taxa) == len(sequences):
            dataset: List[Dict[str:str]] = []
            for i in range(len(taxa)):
                data = {'taxon': taxa[i], 'sequence': sequences[i]}
                dataset.append(data)
            return dataset
        else:
            raise Exception('The number of taxa is different of the number of sequences')

    @staticmethod
    def write_file(output_path: str, output_data: List[Dict[str, str]]):
        with open(output_path, mode='w', encoding='utf-8') as fasta_file:
            for data in output_data:
                taxon, sequence = data
                output_line = f'>{data[taxon]} {data[sequence]}\n'
                fasta_file.write(output_line)
