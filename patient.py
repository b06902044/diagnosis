class Patient:
    def __init__(self, contrast, diagnosis):
        self.contrast = contrast
        self.diagnosis = diagnosis
        
    def decide(self):
        return "some pattern"
        
    def get_result(self):
        if "B" in self.contrast:
            return "s"
        elif "A" in self.contrast:
            self.result = self.decide()