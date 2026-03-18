from collections import deque

# 1. Initialize
application_inbox = deque()   # Queue (FIFO)
processed_history = []        # Stack (LIFO)

# 2. Ingest Data
raw_applications = [" TechCorp ", "bio-gen", "  AlphaWorks", "InnoVent  "]

for app in raw_applications:
    clean_app = app.strip().lower()
    application_inbox.append(clean_app)

# 3. Process (FIFO)
while application_inbox:
    current = application_inbox.popleft()
    print(f"Approving: {current}")
    processed_history.append(current)

# 4. Undo (LIFO)
if processed_history:
    last = processed_history.pop()
    print(f"Reverting approval for: {last}")