from typing import List, Dict

from ..file_manager.fasta.FastaFileManager import FastaFileManager
from ..file_manager.phy.PhyFileManager import PhyFileManager
from ..file_manager.nexus.NexusFileManager import NexusFileManager
from ..exceptions.InvalidFileExtensionError import InvalidFileExtensionError

class FileConverter:
    '''
    File Converter
    --------------
    This class manage file conversion using file manager modules (`FastaFileManager`, `PhyFileManager`, and `NexusFileManager`). Each possibility of conversion are static methods. The main static method `convert()` receive `input_path`, `required_output`, and `output path` to decide which static methods will be called.
    '''
    @staticmethod
    def convert(input_path: str, required_output: str, output_path: str = None):

        if input_path.endswith(('.fasta', '.fas')):
            if required_output == 'phyllip':
                FileConverter.fas_to_phy(input_path, output_path)
            elif required_output == 'nexus':
                FileConverter.fas_to_nex(input_path, output_path)

        elif input_path.endswith(('.phyllip', '.phy')):
            if required_output == 'fasta':
                FileConverter.phy_to_fas(input_path, output_path)
            elif required_output == 'nexus':
                FileConverter.phy_to_nex(input_path, output_path)

        elif input_path.endswith(('.nexus','.nex')):
            if required_output == 'fasta':
                FileConverter.nex_to_fas(input_path, output_path)
            elif required_output == 'phyllip':
                FileConverter.nex_to_phy(input_path, output_path)

        else:
            raise InvalidFileExtensionError('Unsupported file extension, try again with fasta, phyllip or nexus file.')

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