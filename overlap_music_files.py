from pydub import AudioSegment

def overlap(file1_path, file2_path,overlapped_filename):
    
    file1 = AudioSegment.from_file(file1_path)
    file2 = AudioSegment.from_file(file2_path)
    
    overlapped_file = file1.overlay(file2)
    
    overlapped_file.export(overlapped_filename)
    
    
    