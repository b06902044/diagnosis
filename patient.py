class Patient:
    def __init__(self, contrast, diagnosis):
        self.contrast = contrast 
        self.diagnosis = diagnosis
        self.result = ""
        
    def read_diagnosis(self):
        return "some pattern"
        
    def write_result(self):
        if "B" in self.contrast:
            self.result = "s"
        elif "A" in self.contrast:
            self.result = self.read_diagnosis()
    
    def get_result(self):
        return self.result