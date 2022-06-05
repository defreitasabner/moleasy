from typing import List, Dict
import re

from sqlalchemy import false

from ..FileManager import FileManager


class NexusFileManager(FileManager):

    @staticmethod
    def read_file(input_path: str): # Need to implement yet, some difficults with complex nexus file
        
        regex_patterns = {
            'interleave': '(interleave)=([a-z]*)[;]',
            'taxa': '[a-zA-Z0-9]+[_]+[a-zA-Z0-9]+[_a-zA-Z0-9]*',
            'end_data': '[;]',
            'line_break': '\n'
        }
        taxa = []
        sequences = []
        dataset = []
        
        with open(input_path, mode='r', encoding='utf-8') as nexus_file:
            
            for line in iter(nexus_file.readline, ''): # doing this the loop do not call next and not disable tell
                interleave = NexusFileManager.check_interleave(regex_patterns['interleave'], line)
                if interleave == 'yes' or interleave == 'no':
                    break

            for line in iter(nexus_file.readline, ''):
                if re.match(regex_patterns['taxa'], line):
                    first_taxon = nexus_file.tell() - len(line)
                    break

            nexus_file.seek(first_taxon)
            
            if interleave == 'yes':
                interleave_blocks = 1
                inside_block = False # this value will be altered when \n to False and re.match to True

            for line in nexus_file:
                
                if interleave == 'yes':
                    # inside a block of data
                    if re.match(regex_patterns['taxa'], line):
                        line_splitted = line.split()
                        taxon = line_splitted[0]
                        taxa.append(taxon)
                        sequence = line_splitted[1]
                        sequences.append(sequence)
                        inside_block = True
                    # entering in a interleave
                    elif re.match(regex_patterns['line_break'], line) and inside_block == True:
                        inside_block = False
                        print('entrou')
                        sequence_number = f'sequence_{interleave_blocks}'
                        if len(dataset) == 0:
                            for i in range(len(taxa)):
                                data = {'taxon': taxa[i], sequence_number: sequences[i]}
                                dataset.append(data)
                            taxa.clear()
                            sequences.clear()
                            interleave_blocks += 1
                        else:
                            sequence_number = f'sequence_{interleave_blocks}'
                            for i in range(len(taxa)):
                                if dataset[i]['taxon'] == taxa[i]:
                                    new_update = {sequence_number: sequences[i]}
                                    dataset[i].update(new_update)
                                else:
                                    Exception('Fudeu!')
                            taxa.clear()
                            sequences.clear()
                            interleave_blocks += 1
                    # inside a interleave yet
                    elif re.match(regex_patterns['line_break'], line) and inside_block == False:
                        pass
                    # reaching the and of data block
                    elif re.match(regex_patterns['end_data'], line):
                        break

                elif interleave == 'no':
                    if re.match(regex_patterns['taxa'], line):
                        line_splitted = line.split()
                        taxon = line_splitted[0]
                        sequence = line_splitted[1]
                        data = {'taxon': taxon, 'sequence': sequence}
                        dataset.append(data)
        print(len(taxa), len(sequences))
        return print(len(dataset), dataset[0].keys())

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
