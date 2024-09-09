from pdf_extract_kit.registry.registry import TASK_REGISTRY


@TASK_REGISTRY.register("layout_detection-layoutlmv3")
class LayoutDetectionTask:
    def __init__(self, model):
        self.model = model

    def run(self, input_data):
        # Perform layout detection on input_data
        return self.model.predict(input_data)
