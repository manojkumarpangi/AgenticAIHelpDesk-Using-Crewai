class BaseTool:
    def __init__(self):
        """Initialize the base tool. This can be extended in derived classes."""
        pass

    def execute(self, *args, **kwargs):
        """Execute the tool's primary function. This method should be overridden in subclasses."""
        raise NotImplementedError("Subclasses must implement this method.")
