from typing import List, Dict
import re

from ..FileManager import FileManager


class NexusFileManager(FileManager):

    @staticmethod
    def read_file(input_path: str): # Need to implement yet, some difficults with complex nexus file
        
        regex_patterns = {
            'interleave': '(interleave)=([a-z]*)[;]',
            'taxa': '[a-zA-Z0-9]+[_]+[a-zA-Z0-9]+[_a-zA-Z0-9]*',
            'morphological_matrix': '\d'
        }
        taxa = []
        sequences = []
        morphology = []
        dataset = []
        
        with open(input_path, mode='r', encoding='utf-8') as nexus_file:
            
            for line in nexus_file:
                interleave = NexusFileManager.check_interleave(regex_patterns['interleave'], line)
                if interleave == 'yes' or interleave == 'no':
                    break

            for line in nexus_file:
                
                if interleave == 'yes':
                    if re.match(regex_patterns['taxa'], line):
                        line_splitted = line.split()
                        taxon = line_splitted[0]
                        taxa.append(taxon)
                        if re.search(regex_patterns['morphological_matrix'], line_splitted[1]):
                            morph = line_splitted[1]
                            morphology.append(morph)
                        else:
                            sequence = line_splitted[1]
                            sequences.append(sequence)
                
                elif interleave == 'no':
                    if re.match(regex_patterns['taxa'], line):
                        line_splitted = line.split()
                        taxon = line_splitted[0]
                        sequence = line_splitted[1]
                        data = {'taxon': taxon, 'sequence': sequence}
                        dataset.append(data)

        return dataset

    @staticmethod
    def write_file(output_path: str, output_data: List[Dict[str, str]]):
        number_taxa, number_characters, symbols, missing, gap = NexusFileManager.extract_info_to_header(output_data)
        with open(output_path, mode='w', encoding='utf-8') as nexus_file:
            first_line = '#NEXUS\n\n'
            begin_data = 'BEGIN DATA;\n'
            data_first_line = f'    DIMENSIONS NTAX={number_taxa} NCHAR={number_characters};\n'
            data_second_line = f'    FORMAT SYMBOLS="{symbols}" MISSING={missing} GAP={gap} interleave=no;\n\n'
            matrix = 'MATRIX\n\n'
            header = [first_line, begin_data, data_first_line, data_second_line, matrix]
            for line in header:
                nexus_file.write(line)
            for data in output_data:
                line_string = f'{data["taxon"]} {data["sequence"]}\n'
                nexus_file.write(line_string)
            nexus_file.write('\n;\nEND;\n')

    @staticmethod
    def extract_info_to_header(output_data: List[Dict[str, str]]):
            number_taxa = len(output_data)
            number_characters = len(output_data[0]['sequence'])
            all_sequences = ''
            for data in output_data:
                all_sequences += data['sequence']
            extracted_symbols = list(set(list(all_sequences)))
            symbols = ''
            for item in extracted_symbols:
                if (item != 'N') and (item != '-'):
                    symbol = f'{item} '
                    if extracted_symbols.index(item) == len(extracted_symbols) - 1:
                        symbol = symbol.replace(' ', '')
                    symbols += symbol
            header_info = (number_taxa, number_characters, symbols, 'N', '-')
            return header_info

    @staticmethod
    def check_interleave(regex_pattern: str, line: str) -> str:
        if re.search(regex_pattern, line):
            interleave = re.search(regex_pattern, line)
            return interleave.group(2)
        else:
            return None
