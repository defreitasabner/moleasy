from typing import List, Dict
import os.path

from file_manager.fasta.FastaFileManager import FastaFileManager
from file_manager.phy.PhyFileManager import PhyFileManager
from file_manager.nexus.NexusFileManager import NexusFileManager

class FileConverter:

    @staticmethod
    def convert(input_path: str, queried_output: str):

        output_path: str = FileConverter.extracting_output_data_path(input_path, queried_output)

        if input_path.endswith(('.fasta', '.fas')):
            if queried_output == 'phyllip':
                FileConverter.fas_to_phy(input_path, output_path)
            elif queried_output == 'nexus':
                FileConverter.fas_to_nex(input_path, output_path)

        elif input_path.endswith(('.phyllip', '.phy')):
            if queried_output == 'fasta':
                FileConverter.phy_to_fas(input_path, output_path)
            elif queried_output == 'nexus':
                FileConverter.phy_to_nex(input_path, output_path)

        elif input_path.endswith(('.nexus','.nex')):
            if queried_output == 'fasta':
                FileConverter.nex_to_fas(input_path, output_path)
            elif queried_output == 'phyllip':
                FileConverter.nex_to_phy(input_path, output_path)

        else:
            raise Exception('Unsupported file extension, try again with fasta, phyllip or nexus file.')

    @staticmethod
    def extracting_output_data_path(input_path: str, queried_output: str) -> str:
        input_filename, _ = os.path.basename(input_path).split('.')
        print(input_filename)
        input_path_dir = os.path.dirname(input_path)
        print(input_path_dir)
        output_extension = None
        if queried_output == 'fasta':
            output_extension = '.fasta'
        elif queried_output == 'phyllip':
            output_extension = '.phy'
        elif queried_output == 'nexus':
            output_extension = '.nex'
        output_filename = f'{input_filename}{output_extension}'
        output_path = os.path.join(input_path_dir, output_filename)
        return output_path

    @staticmethod
    def fas_to_phy(input_path: str, output_path: str) -> None:
        fasta_data: List[Dict[str, str]] = FastaFileManager.read_file(input_path)
        PhyFileManager.write_file(output_path, fasta_data)
    
    @staticmethod
    def fas_to_nex(input_path: str, output_path: str) -> None:
        fasta_data: List[Dict[str, str]] = FastaFileManager.read_file(input_path)
        NexusFileManager.write_file(output_path, fasta_data)

    @staticmethod
    def phy_to_fas(input_path: str, output_path: str) -> None:
        phyllip_data: List[Dict[str, str]] = PhyFileManager.read_file(input_path)
        FastaFileManager.write_file(output_path, phyllip_data)
    
    @staticmethod
    def phy_to_nex(input_path: str, output_path: str):
        phyllip_data: List[Dict[str, str]] = PhyFileManager.read_file(input_path)
        NexusFileManager.write_file(output_path, phyllip_data)

    @staticmethod
    def nex_to_fas(input_path: str, output_path: str):
        nexus_data: List[Dict[str, str]] = NexusFileManager.read_file(input_path)
        FastaFileManager.write_file(output_path, nexus_data)
    
    @staticmethod
    def nex_to_phy(input_path: str, output_path: str):
        nexus_data: List[Dict[str, str]] = NexusFileManager.read_file(input_path)
        PhyFileManager.write_file(output_path, nexus_data)