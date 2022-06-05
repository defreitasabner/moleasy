from typing import List, Dict

from ..file_manager.fasta.FastaFileManager import FastaFileManager
from ..file_manager.phy.PhyFileManager import PhyFileManager
from ..file_manager.nexus.NexusFileManager import NexusFileManager

class FileConverter:

    @staticmethod
    def convert(input_path: str, output_file_extension: str):

        if input_path.endswith(('.fasta', '.fas')):
            if output_file_extension == 'phyllip':
                FileConverter.fas_to_phy(input_path)
            elif output_file_extension == 'nexus':
                FileConverter.fas_to_nex(input_path)

        elif input_path.endswith(('.phyllip', '.phy')):
            if output_file_extension == 'fasta':
                FileConverter.phy_to_fas(input_path)
            elif output_file_extension == 'nexus':
                FileConverter.phy_to_nex(input_path)

        elif input_path.endswith(('.nexus','.nex')):
            if output_file_extension == 'fasta':
                FileConverter.nex_to_fas(input_path)
            elif output_file_extension == 'phyllip':
                FileConverter.nex_to_phy(input_path)

        else:
            raise Exception('Unsupported file extension, try again with fasta, phyllip or nexus file.')

    @staticmethod
    def fas_to_phy(input_path: str) -> None:
        fasta_data: List[Dict[str, str]] = FastaFileManager.read_file(input_path)
        PhyFileManager.write_file(fasta_data)
    
    @staticmethod
    def fas_to_nex(input_path: str) -> None:
        fasta_data: List[Dict[str, str]] = FastaFileManager.read_file(input_path)
        NexusFileManager.write_file(fasta_data)

    @staticmethod
    def phy_to_fas(input_path: str) -> None:
        phyllip_data: List[Dict[str, str]] = PhyFileManager.read_file(input_path)
        FastaFileManager.write_file(phyllip_data)
    
    @staticmethod
    def phy_to_nex(input_path: str):
        phyllip_data: List[Dict[str, str]] = PhyFileManager.read_file(input_path)
        NexusFileManager.write_file(phyllip_data)

    @staticmethod
    def nex_to_fas(input_path: str):
        nexus_data: List[Dict[str, str]] = NexusFileManager.read_file(input_path)
        FastaFileManager.write_file(nexus_data)
    
    @staticmethod
    def nex_to_phy(input_path):
        nexus_data: List[Dict[str, str]] = NexusFileManager.read_file(input_path)
        PhyFileManager.write_file(nexus_data)