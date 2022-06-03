from typing import List, Dict

from .FileManager import FileManager


class FastaManager(FileManager):

    @staticmethod
    def read_file(path: str) -> List[Dict[str, str]]:
        taxa: List[str] = []
        sequences: List[str] = []
        with open(path, mode='r', encoding='utf-8') as fasta_file:
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
    def write_file(path: str, data: List[Dict[str, str]]):
        with open(path, mode='w', encoding='utf-8') as fasta_file:
            for item in data:
                taxon, sequence = item
                output_line = f'>{item[taxon]} {item[sequence]}\n'
                fasta_file.write(output_line)
