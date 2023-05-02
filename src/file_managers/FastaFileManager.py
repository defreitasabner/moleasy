from typing import List, Dict

from .FileManager import FileManager


class FastaFileManager(FileManager):
    """
    FastaFileManager
    ---
    Module responsable to read and write `Fasta` files. The accepted files extensions are: `.fasta` and `.fas`.
    """

    def read_file(self, input_path: str) -> None:
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
            dataset: List[Dict[str, str]] = []
            for i in range(len(taxa)):
                data = {'taxon': taxa[i], 'sequence': sequences[i]}
                dataset.append(data)
            self.data = dataset
        else:
            raise Exception('The number of taxa is different of the number of sequences')

    def write_file(self, output_path: str, output_data: List[Dict[str, str]]) -> None:
        with open(output_path, mode='w', encoding='utf-8') as fasta_file:
            for data in output_data:
                taxon, sequence = data
                output_line = f'>{data[taxon]} {data[sequence]}\n'
                fasta_file.write(output_line)
