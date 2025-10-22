import logging
from httpx import Request
from random_key_auth import RandomKeyAuth  # adjust import path if needed

# Setup logger to show DEBUG output in console
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("TestLogger")

# Create dummy keys (no real API keys!)
keys = ["ghp_FAKEKEY1234567890", "ghp_ANOTHERFAKE999999"]

# Create instance
auth = RandomKeyAuth(list_of_keys=keys, header_name="Authorization", logger=logger, key_format="token {0}")

# Create a dummy request (no actual HTTP)
req = Request("GET", "https://example.com/api/test")

# Run the generator manually
flow = auth.auth_flow(req)
prepared_request = next(flow)  # first yield

print("\n=== HEADER RESULT ===")
print(prepared_request.headers)
