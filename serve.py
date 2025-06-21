#!/usr/bin/env python3

import os
import threading
import uvicorn
from cog.config import Config
from cog.server.http import create_app
from cog.mode import Mode

def main():
    # Load cog config
    config = Config()
    
    # Create shutdown event
    shutdown_event = threading.Event()
    
    # Create the FastAPI app
    app = create_app(
        cog_config=config,
        shutdown_event=shutdown_event,
        mode=Mode.PREDICT
    )
    
    # Run the server
    uvicorn.run(app, host="0.0.0.0", port=5000)

if __name__ == "__main__":
    main()