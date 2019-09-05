"""Application definition."""
from bocadillo import App, discover_providers

app = App()
discover_providers("base.providerconf")

# Create routes here.
